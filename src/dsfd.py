import numpy as np
import random
from src.wsn import WSN
from src.stats import Stats

class DSFD:
    def __init__(self, config) -> None:
        self.config = config
        self.wsn = WSN(config)
        self.node_min_val = 23.5 # this is the temperature, when no event detected at the nodes.
        self.node_max_val = 27.5
        self.total_faulty_nodes = 25
        self.total_nodes = self.config.get_no_of_nodes

    def detection_accuracy(self):
        '''Total no. of faulty nodes detected/ Total no. of faulty nodes
        '''

        # assign each nodes a normal data first.
        for node_id in range(self.total_nodes):
            self.wsn.g.nodes[node_id]['attr_dict']['data'] = random.uniform(self.node_min_val, self.node_max_val)
        
        # create randomly faulty nodes in the WSN.
        faulty_node_ids = [random.randint(0, self.total_nodes-1) for _ in range(self.total_faulty_nodes)]

        # make node faulty by assigning higher values
        faulty_val_min = 50.8
        faulty_val_max = 87.2

        for node_id in faulty_node_ids:
            self.wsn.g.nodes[node_id]['attr_dict']['data'] = random.uniform(faulty_val_min, faulty_val_max)

        # Now each node runs the DSFD algorithm to check wheather they are faulty nodes or not.
        # Each node collects there neighbors data to verify there status.

        for node_id in range(self.total_nodes):
            node_data = self.wsn.g.nodes[node_id]['attr_dict']['data']
            data_list = [] # contains neigbors node values.
            for neighbor_id in self.wsn.get_neighbor_node_data(node_id):
                data_list.append(self.wsn.g.nodes[neighbor_id]['attr_dict']['data'])

            mad_val = Stats.median_absolute_deviation(node_data, data_list)

            if mad_val>=3:
                # node consider as faulty node, assign node false value
                self.wsn.g.nodes[node_id]['attr_dict']['status'] = False


        # calculate detection accuracy
        total_faulty_nodes_detected = 0
        for node_id in range(self.total_nodes):
            if self.wsn.g.nodes[node_id]['attr_dict']['status'] == False:
                total_faulty_nodes_detected +=1

        det_acc =  total_faulty_nodes_detected/self.total_faulty_nodes

        return det_acc*100


    def false_alaram_rate(self):
        pass

    def false_positive_rate(self):
        pass

    def total_energy_consumption(self):
        pass

    def running_time(self):
        pass
    
