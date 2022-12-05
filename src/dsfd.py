import numpy as np
import random
import time
from src.wsn import WSN
from utils.stats import Stats
from utils.generate_csv import Generate_csv


class DSFD:
    def __init__(self, config) -> None:
        self.config = config
        self.wsn = WSN(config)
        self.gen_csv = Generate_csv(config)
        self.node_min_val, self.node_max_val = self.config.get_node_avg_value
        self.total_faulty_nodes = self.config.get_no_of_faulty_nodes
        self.total_nodes = self.config.get_no_of_nodes
        self.stat_method = self.config.get_stat_method
        self.faulty_val_min, self.faulty_val_max = self.config.get_node_faulty_value

    def run(self):

        # assign each nodes a normal data first.
        for node_id in range(self.total_nodes):
            self.wsn.g.nodes[node_id]["attr_dict"]["data"] = random.uniform(
                self.node_min_val, self.node_max_val
            )

        # create randomly faulty nodes in the WSN.
        faulty_node_ids = [
            random.randint(0, self.total_nodes - 1)
            for _ in range(self.total_faulty_nodes)
        ]

        # make node faulty by assigning higher values and status is False
        for node_id in faulty_node_ids:
            self.wsn.g.nodes[node_id]["attr_dict"]["data"] = random.uniform(
                self.faulty_val_min, self.faulty_val_max
            )
            self.wsn.g.nodes[node_id]["attr_dict"]["status"] = False

        # Now each node runs the DSFD algorithm to check wheather they are faulty nodes or not.
        # Each node collects there neighbors data to verify there status.
        avg_time_to_calculate_stat = []
        confusion_matrix = []
        for node_id in range(self.total_nodes):
            node_data = self.wsn.g.nodes[node_id]["attr_dict"]["data"]
            data_list = []  # contains neigbors node values.
            for neighbor_id in self.wsn.get_neighbor_node_data(node_id):
                data_list.append(self.wsn.g.nodes[neighbor_id]["attr_dict"]["data"])

            start = time.time()
            val = Stats().calculate(self.stat_method, node_data, data_list)
            end = time.time()
            avg_time_to_calculate_stat.append(end - start)

            # node consider as faulty node, assign node false value
            confusion_matrix.append(
                {
                    "node_id": node_id,
                    "actual_status": self.wsn.g.nodes[node_id]["attr_dict"]["status"],
                    "predicted_status": val <= 3,
                }
            )

        avg_time = round(sum(avg_time_to_calculate_stat) / self.total_nodes, 2)

        self.gen_csv.generate_cm_csv(confusion_matrix)

        true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
        for data in confusion_matrix:
            if data["actual_status"] == True and data["predicted_status"] == True:
                true_pos += 1
            if data["actual_status"] == False and data["predicted_status"] == False:
                true_neg += 1
            if data["actual_status"] == True and data["predicted_status"] == False:
                false_neg += 1
            if data["actual_status"] == False and data["predicted_status"] == True:
                false_pos += 1

        print(true_pos, false_pos, true_neg, false_neg)

        # Calculate final params
        # detection accuracy
        det_acc = round((true_neg + true_pos) / (true_pos + true_neg + false_neg + false_pos), 2)

        # true positive rate
        tpr = round(true_pos / (true_pos + false_neg), 2)

        # true negative rate
        tnr = round(true_neg / (true_neg + false_pos), 2)

        # calculate total energy consumption
        energy_consume_by_each_node = 0

        # generate result artifact
        self.gen_csv.generate_result_csv(
            det_acc, tpr, tnr, avg_time, energy_consume_by_each_node
        )

        return det_acc, tpr, tnr, avg_time
