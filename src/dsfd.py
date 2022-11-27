import numpy as np
import random
import time
from src.wsn import WSN
from src.stats import Stats
from src.generate_csv import Generate_csv

class DSFD:
    def __init__(self, config) -> None:
        self.config = config
        self.wsn = WSN(config)
        self.gen_csv = Generate_csv(config)
        self.node_min_val, self.node_max_val = self.config.get_node_avg_value # this is the temperature, when no event detected at the nodes.
        self.total_faulty_nodes = self.config.get_no_of_faulty_nodes
        self.total_nodes = self.config.get_no_of_nodes
        self.stat_method = self.config.get_stat_method
        self.faulty_val_min, self.faulty_val_max = self.config.get_node_faulty_value

    def run(self):
        '''Total no. of faulty nodes detected/ Total no. of faulty nodes
        '''

        # assign each nodes a normal data first.
        for node_id in range(self.total_nodes):
            self.wsn.g.nodes[node_id]['attr_dict']['data'] = random.uniform(self.node_min_val, self.node_max_val)
        
        # create randomly faulty nodes in the WSN.
        faulty_node_ids = [random.randint(0, self.total_nodes-1) for _ in range(self.total_faulty_nodes)]

        # make node faulty by assigning higher values
        

        for node_id in faulty_node_ids:
            self.wsn.g.nodes[node_id]['attr_dict']['data'] = random.uniform(self.faulty_val_min, self.faulty_val_max)

        # Now each node runs the DSFD algorithm to check wheather they are faulty nodes or not.
        # Each node collects there neighbors data to verify there status.
        avg_time_to_calculate_stat = []
        for node_id in range(self.total_nodes):
            node_data = self.wsn.g.nodes[node_id]['attr_dict']['data']
            data_list = [] # contains neigbors node values.
            for neighbor_id in self.wsn.get_neighbor_node_data(node_id):
                data_list.append(self.wsn.g.nodes[neighbor_id]['attr_dict']['data'])
            
            start = time.time()
            val = Stats.median_absolute_deviation(node_data, data_list) if len(data_list)>0 else 1.5
            end = time.time()
            avg_time_to_calculate_stat.append(end-start)

            if val>=3:
                # node consider as faulty node, assign node false value
                self.wsn.g.nodes[node_id]['attr_dict']['status'] = False

        avg_time = sum(avg_time_to_calculate_stat)/self.total_nodes

        # calculate detection accuracy
        total_faulty_nodes_detected = 0
        for node_id in range(self.total_nodes):
            if self.wsn.g.nodes[node_id]['attr_dict']['status'] == False:
                total_faulty_nodes_detected +=1

        det_acc =  total_faulty_nodes_detected/self.total_faulty_nodes

        # calculate false alaram rate
        total_faulty_nodes_detected_as_non_faulty = 0
        for node_id in range(self.total_nodes):
            if self.wsn.g.nodes[node_id]['attr_dict']['status'] == False:
                if self.node_min_val<=self.wsn.g.nodes[node_id]['attr_dict']['data']<=self.node_max_val:
                    total_faulty_nodes_detected_as_non_faulty +=1
        
        false_alaram_rate = total_faulty_nodes_detected_as_non_faulty/(self.total_nodes-self.total_faulty_nodes)

        # calculate false positive rate
        total_non_faulty_nodes_detected_as_faulty = 0
        for node_id in range(self.total_nodes):
            if self.wsn.g.nodes[node_id]['attr_dict']['status'] == True:
                if self.faulty_val_max<=self.wsn.g.nodes[node_id]['attr_dict']['data']<=self.faulty_val_min:
                    total_non_faulty_nodes_detected_as_faulty +=1

        false_positive_rate = total_non_faulty_nodes_detected_as_faulty/self.total_faulty_nodes

        # calculate total energy consumption
        # need to implement
        energy_consume_by_each_node = 0


        # generate result artifact
        self.gen_csv.generate_result_csv(det_acc, false_alaram_rate, false_positive_rate, avg_time, energy_consume_by_each_node)

        return det_acc, false_alaram_rate, false_positive_rate, avg_time
