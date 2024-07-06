import numpy as np
import random

class Node:
    def __init__(self, node_id, position, role='sensor', protocol='AODV'):
        self.node_id = node_id
        self.position = position
        self.role = role  # 'sensor' or 'base_station'
        self.protocol = protocol  # 'AODV' or 'DSR'
        self.energy = 100  # Initial energy level
        self.data_queue = []
        self.routing_table = {}  # Routing table for AODV
        self.route_cache = {}  # Route cache for DSR
        self.rreq_cache = set()  # Cache for RREQs to prevent infinite loops

    def transmit(self, data, recipient):
        if self.energy > 0:
            self.energy -= self.calculate_transmit_cost(data, recipient)
            print(f"Node {self.node_id} transmitted data to Node {recipient.node_id}. Remaining energy: {self.energy}")

    def receive(self, data):
        if self.energy > 0:
            self.energy -= self.calculate_receive_cost(data)
            print(f"Node {self.node_id} received data. Remaining energy: {self.energy}")

    def calculate_transmit_cost(self, data, recipient):
        distance = np.linalg.norm(np.array(self.position) - np.array(recipient.position))
        return 0.1 * len(data) + 0.01 * distance  # Example energy model

    def calculate_receive_cost(self, data):
        return 0.05 * len(data)  # Example energy model

    def queue_data(self, data):
        self.data_queue.append(data)

    def process_data_queue(self, network):
        while self.data_queue and self.energy > 0:
            data = self.data_queue.pop(0)
            if self.protocol == 'AODV':
                recipient = self.find_next_hop_aodv(network, data['destination'])
            elif self.protocol == 'DSR':
                recipient = self.find_next_hop_dsr(network, data['destination'])
            if recipient:
                self.transmit(data['content'], recipient)
                recipient.receive(data['content'])

    # AODV Protocol Methods
    def find_next_hop_aodv(self, network, destination):
        if destination.node_id in self.routing_table:
            next_hop_id = self.routing_table[destination.node_id]
            return network.node_mapping.get(next_hop_id, None)
        else:
            self.send_rreq(network, destination)
            return None

    def send_rreq(self, network, destination):
        print(f"Node {self.node_id} broadcasting RREQ for Node {destination.node_id}")
        rreq = {'source': self.node_id, 'destination': destination.node_id, 'seq_num': random.randint(1, 1000)}
        self.rreq_cache.add((rreq['source'], rreq['seq_num']))  # Cache the RREQ
        for neighbor in network.get_neighbors(self):
            if (rreq['source'], rreq['seq_num']) not in neighbor.rreq_cache:
                network.send_rreq(neighbor, rreq)

    def receive_rreq(self, network, rreq):
        if (rreq['source'], rreq['seq_num']) in self.rreq_cache:
            return
        self.rreq_cache.add((rreq['source'], rreq['seq_num']))  # Cache the RREQ

        if rreq['destination'] == self.node_id:
            self.send_rrep(network, rreq)
        else:
            for neighbor in network.get_neighbors(self):
                if neighbor.node_id != rreq['source']:
                    network.send_rreq(neighbor, rreq)

    def send_rrep(self, network, rreq):
        print(f"Node {self.node_id} sending RREP to Node {rreq['source']}")
        rrep = {'source': self.node_id, 'destination': rreq['source']}
        network.node_mapping[rreq['source']].routing_table[self.node_id] = self.node_id
        network.send_rrep(network.node_mapping[rreq['source']], rrep)

    def receive_rrep(self, network, rrep):
        self.routing_table[rrep['source']] = rrep['destination']
        print(f"Node {self.node_id} received RREP from Node {rrep['source']}")

    # DSR Protocol Methods
    def find_next_hop_dsr(self, network, destination):
        if destination.node_id in self.route_cache:
            route = self.route_cache[destination.node_id]
            next_hop_id = route[1] if len(route) > 1 else None
            return network.node_mapping.get(next_hop_id, None)
        else:
            self.send_route_request(network, destination)
            return None

    def send_route_request(self, network, destination):
        print(f"Node {self.node_id} broadcasting Route Request for Node {destination.node_id}")
        route_request = {'source': self.node_id, 'destination': destination.node_id, 'path': [self.node_id]}
        for neighbor in network.get_neighbors(self):
            network.send_route_request(neighbor, route_request)

    def receive_route_request(self, network, route_request):
        if self.node_id in route_request['path']:
            return  # Prevent loop

        route_request['path'].append(self.node_id)

        if route_request['destination'] == self.node_id:
            self.send_route_reply(network, route_request)
        else:
            for neighbor in network.get_neighbors(self):
                if neighbor.node_id not in route_request['path']:
                    network.send_route_request(neighbor, route_request)

    def send_route_reply(self, network, route_request):
        print(f"Node {self.node_id} sending Route Reply to Node {route_request['source']}")
        route_reply = {'source': self.node_id, 'destination': route_request['source'], 'path': list(route_request['path'])}
        for node_id in route_reply['path']:
            network.node_mapping[node_id].route_cache[self.node_id] = list(route_reply['path'])
        network.send_route_reply(network.node_mapping[route_request['source']], route_reply)

    def receive_route_reply(self, network, route_reply):
        self.route_cache[route_reply['destination']] = route_reply['path']
        print(f"Node {self.node_id} received Route Reply from Node {route_reply['source']}")
