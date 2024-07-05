# wsn_sim/network.py
import networkx as nx
import matplotlib.pyplot as plt
import random

class Network:
    def __init__(self):
        self.nodes = []
        self.graph = nx.Graph()
        self.node_mapping = {}

    def add_node(self, node):
        self.nodes.append(node)
        self.node_mapping[node.node_id] = node
        self.graph.add_node(node.node_id, pos=node.position)

    def add_link(self, node1_id, node2_id):
        self.graph.add_edge(node1_id, node2_id)

    def broadcast(self, node, data):
        for neighbor in self.get_neighbors(node):
            if neighbor.energy > 0:
                node.transmit(data, neighbor)
                neighbor.receive(data['content'])

    def get_neighbors(self, node):
        neighbors_ids = list(self.graph.neighbors(node.node_id))
        return [self.node_mapping[n_id] for n_id in neighbors_ids]

    def send_rreq(self, node, rreq):
        if node.energy > 0:
            node.receive_rreq(self, rreq)

    def send_route_request(self, node, route_request):
        if node.energy > 0:
            node.receive_route_request(self, route_request)

    def visualize(self):
        pos = nx.get_node_attributes(self.graph, 'pos')
        energy_levels = [node.energy for node in self.nodes]
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=[e*10 for e in energy_levels])
        plt.show()

    def run_simulation(self, steps=10, protocol='AODV'):
        for step in range(steps):
            print(f"Simulation step {step + 1}")
            for node in self.nodes:
                if node.role == 'sensor' and node.energy > 0:
                    data = f"Temperature: {random.uniform(15, 35):.2f}C"
                    node.queue_data({'destination': self.get_base_station(), 'content': data})
                node.process_data_queue(self)

    def get_base_station(self):
        return next(node for node in self.nodes if node.role == 'base_station')
