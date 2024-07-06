import tkinter as tk
from tkinter import filedialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import numpy as np
from .node import Node

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

    def generate_topology(self, topology_type, nodes, links):
        if topology_type == 'grid':
            self.generate_grid_topology(nodes)
        elif topology_type == 'random':
            self.generate_random_topology(nodes, links)
        elif topology_type == 'cluster':
            self.generate_cluster_topology(nodes, links)

    def generate_grid_topology(self, nodes):
        grid_size = int(np.ceil(np.sqrt(nodes)))
        for i in range(nodes):
            x, y = divmod(i, grid_size)
            node = Node(i, (x, y))
            self.add_node(node)

        for i in range(grid_size):
            for j in range(grid_size):
                if j < grid_size - 1:
                    self.add_link(i * grid_size + j, i * grid_size + j + 1)
                if i < grid_size - 1:
                    self.add_link(i * grid_size + j, (i + 1) * grid_size + j)

    def generate_random_topology(self, nodes, links):
        for i in range(nodes):
            node = Node(i, (random.randint(0, 100), random.randint(0, 100)))
            self.add_node(node)

        for _ in range(links):
            node1, node2 = random.sample(self.nodes, 2)
            self.add_link(node1.node_id, node2.node_id)

    def generate_cluster_topology(self, nodes, links):
        clusters = int(np.sqrt(nodes))
        nodes_per_cluster = nodes // clusters
        cluster_centers = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(clusters)]

        for cluster_id, center in enumerate(cluster_centers):
            for i in range(nodes_per_cluster):
                position = (center[0] + random.randint(-10, 10), center[1] + random.randint(-10, 10))
                node = Node(cluster_id * nodes_per_cluster + i, position)
                self.add_node(node)

        for _ in range(links):
            node1, node2 = random.sample(self.nodes, 2)
            self.add_link(node1.node_id, node2.node_id)

    def run_aodv_simulation(self, steps):
        for step in range(steps):
            print(f"Simulation step {step + 1}")
            for node in self.nodes:
                if node.role == 'sensor' and node.energy > 0:
                    data = f"Temperature: {random.uniform(15, 35):.2f}C"
                    node.queue_data({'destination': self.get_base_station(), 'content': data})
                node.process_data_queue(self)

    def run_dsr_simulation(self, steps):
        for step in range(steps):
            print(f"Simulation step {step + 1}")
            for node in self.nodes:
                if node.role == 'sensor' and node.energy > 0:
                    data = f"Temperature: {random.uniform(15, 35):.2f}C"
                    node.queue_data({'destination': self.get_base_station(), 'content': data})
                node.process_data_queue(self)

    def get_base_station(self):
        return next(node for node in self.nodes if node.role == 'base_station')

    def get_neighbors(self, node):
        neighbors_ids = list(self.graph.neighbors(node.node_id))
        return [self.node_mapping[n_id] for n_id in neighbors_ids]

    # AODV Methods
    def send_rreq(self, neighbor, rreq):
        neighbor.receive_rreq(self, rreq)

    def send_rrep(self, neighbor, rrep):
        neighbor.receive_rrep(self, rrep)

    # DSR Methods
    def send_route_request(self, neighbor, route_request):
        neighbor.receive_route_request(self, route_request)

    def send_route_reply(self, neighbor, route_reply):
        neighbor.receive_route_reply(self, route_reply)

    def visualize(self, filename='graph_visualization.png', display=True):
        pos = nx.get_node_attributes(self.graph, 'pos')
        energy_levels = [node.energy for node in self.nodes]

        plt.figure(figsize=(10, 8))
        if len(energy_levels) == len(self.graph.nodes):
            nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=[e * 10 for e in energy_levels])
        else:
            nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=100)
        
        plt.title('Wireless Sensor Network Visualization')
        plt.savefig(filename)
        if display:
            plt.show()
        else:
            plt.close()
        print(f"Graph saved to {filename}")

    def create_gui(self):
        root = tk.Tk()
        root.title("Wireless Sensor Network Simulator")

        def run_simulation():
            protocol = protocol_var.get()
            steps = int(steps_entry.get())
            nodes = int(nodes_entry.get())
            links = int(links_entry.get())
            topology = topology_var.get()
            output = output_entry.get()

            net = Network()
            net.generate_topology(topology, nodes, links)
            base_station = Node(0, (50, 50), role='base_station')
            net.add_node(base_station)

            if protocol.upper() == 'AODV':
                net.run_aodv_simulation(steps)
            elif protocol.upper() == 'DSR':
                net.run_dsr_simulation(steps)

            net.visualize(filename=output, display=False)  # Save the graph to the specified file
            messagebox.showinfo("Info", f"Simulation completed and graph saved to {output}")

        def upload_config():
            filepath = filedialog.askopenfilename(filetypes=[("Config Files", "*.json")])
            if filepath:
                # Read and display the config file
                with open(filepath, 'r') as file:
                    config = file.read()
                config_text.delete(1.0, tk.END)
                config_text.insert(tk.END, config)

        # Frame for input fields
        frame = tk.Frame(root)
        frame.pack(pady=10, padx=10, fill=tk.X)

        tk.Label(frame, text="Protocol (AODV/DSR):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        protocol_var = tk.StringVar(value='AODV')
        tk.Entry(frame, textvariable=protocol_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Steps:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        steps_entry = tk.Entry(frame)
        steps_entry.grid(row=1, column=1, padx=5, pady=5)
        steps_entry.insert(tk.END, '10')

        tk.Label(frame, text="Number of Nodes:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        nodes_entry = tk.Entry(frame)
        nodes_entry.grid(row=2, column=1, padx=5, pady=5)
        nodes_entry.insert(tk.END, '20')

        tk.Label(frame, text="Number of Links:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        links_entry = tk.Entry(frame)
        links_entry.grid(row=3, column=1, padx=5, pady=5)
        links_entry.insert(tk.END, '30')

        tk.Label(frame, text="Topology (grid/random/cluster):").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        topology_var = tk.StringVar(value='random')
        tk.Entry(frame, textvariable=topology_var).grid(row=4, column=1, padx=5, pady=5)

        tk.Label(frame, text="Output Filename:").grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        output_entry = tk.Entry(frame)
        output_entry.grid(row=5, column=1, padx=5, pady=5)
        output_entry.insert(tk.END, 'graph_visualization.png')

        tk.Button(frame, text="Run Simulation", command=run_simulation).grid(row=6, column=0, columnspan=2, pady=10)

        tk.Button(frame, text="Upload Config", command=upload_config).grid(row=7, column=0, columnspan=2, pady=10)

        tk.Label(frame, text="Config File Content:").grid(row=8, column=0, sticky=tk.W, padx=5, pady=5)
        config_text = tk.Text(frame, height=10, width=50)
        config_text.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        root.mainloop()