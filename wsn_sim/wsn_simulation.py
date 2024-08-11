import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Tuple
import random
from traffic_pattern import *
from routing_protocol import *
from node import Node, BaseStation


class WSN_Simulator:
    def __init__(self, area_size: Tuple[int, int], num_nodes: int, routing_protocol: RoutingProtocol, traffic_pattern: TrafficPattern, mobility_enabled: bool = True, grid_deployment: bool = False):
        self.area_size = area_size
        self.num_nodes = num_nodes
        self.nodes: List[Node] = []
        self.base_station = BaseStation(node_id=num_nodes, position=(area_size[0] // 2, area_size[1] // 2))
        self.routing_protocol = routing_protocol
        self.traffic_pattern = traffic_pattern
        self.simulation_time = 0
        self.mobility_enabled = mobility_enabled
        self.grid_deployment = grid_deployment

        # Initialize a NetworkX graph
        self.network = nx.Graph()

        # Pass the routing protocol to the traffic pattern
        self.traffic_pattern.set_routing_protocol(self.routing_protocol)

    def deploy_nodes(self):
        if self.grid_deployment:
            self.deploy_nodes_in_grid()
        else:
            self.deploy_nodes_randomly()

    def deploy_nodes_randomly(self):
        print(f"Deploying {self.num_nodes} nodes randomly in area {self.area_size}.")
        for i in range(self.num_nodes):
            position = (random.randint(0, self.area_size[0]), random.randint(0, self.area_size[1]))
            node = Node(node_id=i, position=position)
            self.nodes.append(node)
            self.network.add_node(node.id, pos=node.position)
        self.network.add_node(self.base_station.id, pos=self.base_station.position)

        self.connect_nodes()

    def deploy_nodes_in_grid(self):
        print(f"Deploying {self.num_nodes} nodes in a grid in area {self.area_size}.")
        grid_size = int(self.num_nodes**0.5)  # Assuming a square grid for simplicity
        x_step = self.area_size[0] // (grid_size - 1)
        y_step = self.area_size[1] // (grid_size - 1)

        for i in range(grid_size):
            for j in range(grid_size):
                node_id = i * grid_size + j
                if node_id < self.num_nodes:
                    position = (i * x_step, j * y_step)
                    node = Node(node_id=node_id, position=position)
                    self.nodes.append(node)
                    self.network.add_node(node.id, pos=node.position)

        self.network.add_node(self.base_station.id, pos=self.base_station.position)

        self.connect_nodes()

    def connect_nodes(self):
        # Connect nodes randomly or based on proximity (you can refine this logic)
        for node in self.nodes:
            possible_neighbors = random.sample(self.nodes, k=random.randint(1, len(self.nodes)//2))
            for neighbor in possible_neighbors:
                if node.id != neighbor.id and not self.network.has_edge(node.id, neighbor.id):
                    self.network.add_edge(node.id, neighbor.id)
                    node.neighbors.append(neighbor)
                    neighbor.neighbors.append(node)

    # def connect_nodes(self):
    #     print("Connecting nodes based on proximity.")
    #     max_distance = 5  # Maximum distance to consider nodes as neighbors
    #     for node in self.nodes:
    #         for neighbor in self.nodes:
    #             if node.id != neighbor.id and not self.network.has_edge(node.id, neighbor.id):
    #                 distance = self.calculate_distance(node.position, neighbor.position)
    #                 if distance <= max_distance:
    #                     self.network.add_edge(node.id, neighbor.id)
    #                     node.neighbors.append(neighbor)
    #                     neighbor.neighbors.append(node)

    # @staticmethod
    # def calculate_distance(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
    #     return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    def start_simulation(self, time_steps: int):
        self.simulation_time = time_steps
        for t in range(time_steps):
            print(f"\nSimulation Step {t+1}/{time_steps}")
            self.traffic_pattern.generate_traffic(self.nodes, self.base_station)
            for node in self.nodes:
                node.move(mobility_enabled=self.mobility_enabled)

    def visualize_network(self):
        print(f"Visualizing network with {len(self.nodes)} nodes.")
        pos = nx.get_node_attributes(self.network, 'pos')
        nx.draw(self.network, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
        plt.show()

    def collect_metrics(self):
        energy_levels = [node.energy for node in self.nodes]
        total_packets_sent = sum(node.packets_sent for node in self.nodes)
        total_packets_received = sum(node.packets_received for node in self.nodes)
        total_packets_missed = sum(node.packets_missed for node in self.nodes)

        if total_packets_sent > 0:
            packet_delivery_ratio = total_packets_received / total_packets_sent
        else:
            packet_delivery_ratio = 0

        print(f"Node Energy Levels: {energy_levels}")
        print(f"Total Packets Sent: {total_packets_sent}")
        print(f"Total Packets Received: {total_packets_received}")
        print(f"Total Packets Missed: {total_packets_missed}")
        print(f"Packet Delivery Ratio: {packet_delivery_ratio:.2f}")

    def export_results(self, filename: str):
        with open(filename, 'w') as file:
            file.write("Simulation Results\n")
            file.write("Node ID, Energy Level, Packets Sent, Packets Received, Packets Missed\n")

            for node in self.nodes:
                file.write(f"{node.id}, {node.energy}, {node.packets_sent}, {node.packets_received}, {node.packets_missed}\n")

            # Aggregate metrics
            total_packets_sent = sum(node.packets_sent for node in self.nodes)
            total_packets_received = sum(node.packets_received for node in self.nodes)
            total_packets_missed = sum(node.packets_missed for node in self.nodes)

            if total_packets_sent > 0:
                packet_delivery_ratio = total_packets_received / total_packets_sent
            else:
                packet_delivery_ratio = 0

            file.write("\nAggregated Metrics\n")
            file.write(f"Total Packets Sent: {total_packets_sent}\n")
            file.write(f"Total Packets Received: {total_packets_received}\n")
            file.write(f"Total Packets Missed: {total_packets_missed}\n")
            file.write(f"Packet Delivery Ratio: {packet_delivery_ratio:.2f}\n")

        print(f"Results exported to {filename}")



# Example Usage with DSR protocol
if __name__ == "__main__":
    simulator = WSN_Simulator(area_size=(100, 100), num_nodes=16, routing_protocol=Flooding(), traffic_pattern=PeriodicTraffic(), mobility_enabled=False, grid_deployment=True)

    # Deploy nodes and start the simulation
    simulator.deploy_nodes()
    simulator.visualize_network()  # Visualize the initial network setup
    simulator.start_simulation(time_steps=5)
    simulator.collect_metrics()
    simulator.visualize_network()  # Visualize the network after the simulation
    simulator.export_results("simulation_results_dsr.txt")
