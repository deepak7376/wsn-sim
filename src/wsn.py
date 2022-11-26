import itertools
import copy
import networkx as nx
import pandas as pd
import random 
import os
import matplotlib.pyplot as plt


class WSN:
    def __init__(self, config) -> None:
        self.config = config 
        self.g = nx.Graph()
        self._initalize_wsn()
        
    def _initalize_wsn(self):    
        self._create_nodelist_from_config()
        self._create_edgelist_from_config()
        self._create_edgelist_from_csv("resources/edgelist.csv")
        self._create_nodelist_from_csv("resources/nodelist.csv")
        self._visualize_graph()

    def get_neighbor_node_data(self, node_id):
        return self.g.adj[node_id]

    def _create_edgelist_from_csv(self, path):
        edgelist = pd.read_csv(path)
        # Add edges and edge attributes
        for i, elrow in edgelist.iterrows():
            if elrow[3]==True: # if node 1 and node 2 are neighbor then there is edge between them
                self.g.add_edge(elrow[0], elrow[1], attr_dict=elrow[2:].to_dict())
    
    def _create_nodelist_from_csv(self, path):
        nodelist = pd.read_csv(path)
        # Add node attributes
        for i, nlrow in nodelist.iterrows():
            self.g.add_node(nlrow['id'] , attr_dict=nlrow[1:].to_dict())
        # print(self.g.nodes.data())
        # print(self.g.number_of_nodes())
        # print(self.g.number_of_edges())

    def _save_dataframe(self, df, file_name, path="resources"):
        df.to_csv(os.path.join(path, file_name), encoding='utf-8', index=False)
    
    def _create_coordinate(self):
        x_coord, y_coord = self.config.get_area
        no_of_nodes = self.config.get_no_of_nodes
        coords = [{"id": id, "X": random.randint(0, x_coord), "Y": random.randint(0, y_coord), "data": 0, "power": self.config.get_remaining_power_of_node, "status": True} for id in range(no_of_nodes)]
        return coords
    
    def _calculate_eculidean_dist(self, node_1, node_2):
        return round(((node_1['X'] - node_2['X'])**2 + (node_1['Y'] - node_2['Y'])**2)**0.5, 2)
    
    def _create_edgelist_from_config(self):
        edgelist = []
        coords = self._create_coordinate()

        for node_1 in coords:
            for node_2 in coords:
                if node_1!=node_2:
                    dist_bt_nodes = self._calculate_eculidean_dist(node_1, node_2)
                    is_neighbor = dist_bt_nodes<self.config.get_tx_range
                    color = "green" if is_neighbor else "red"
                    edgelist.append({"node_1": node_1['id'], "node_2": node_2['id'], "distance": dist_bt_nodes, "neighbor": is_neighbor, "color": color})

        edgelist = pd.DataFrame.from_dict(edgelist)
        self._save_dataframe(edgelist, "edgelist.csv")

    def _create_nodelist_from_config(self):
        coords = self._create_coordinate()
        nodelist = pd.DataFrame.from_dict(coords)
        self._save_dataframe(nodelist, "nodelist.csv")

    def _visualize_graph(self):
        # Define node positions data structure (dict) for plotting
        node_positions = {node[0]: (node[1]['attr_dict']['X'], node[1]['attr_dict']['Y']) for node in self.g.nodes(data=True)}

        # Preview of node_positions with a bit of hack (there is no head/slice method for dictionaries).
        print(dict(list(node_positions.items())[0:5]))

        # Define data structure (list) of edge colors for plotting
        edge_colors = [e[2]['attr_dict']['color'] for e in self.g.edges(data=True)]

        # Preview first 10
        print(edge_colors[0:10])

        plt.figure(figsize=(8, 6))
        nx.draw(self.g, pos=node_positions, edge_color=edge_colors, node_size=10, node_color='black')
        plt.savefig("resources/path.png")
        plt.title('Graph Representation of Sleeping Giant Trail Map', size=15)
        # plt.show()

if __name__=="__main__":
    from src.config import Config

    c = Config("config.yaml")
    w = WSN(c)
    w._create_nodelist_from_config()
    w._create_edgelist_from_config()
    w._create_edgelist_from_csv("resources/edgelist.csv")
    w._create_nodelist_from_csv("resources/nodelist.csv")
    w._visualize_graph()