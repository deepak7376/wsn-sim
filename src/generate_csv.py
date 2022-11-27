import csv
from datetime import datetime



class Generate_csv:
    def __init__(self, config) -> None:
        self.config = config
        self.header = ['Date/Time', 'Stat. Method', 'Total Nodes', 'Total Faulty Nodes', 'Node Avg. Value Range', 'Faulty Value Range', 'Detection Acc.', 'False Alaram Rate', 'False Positive Rate', 'Avg. Stat Cal. Time', 'Energy']

    def generate_result_csv(self, det_acc, false_alaram_rate, false_positive_rate, avg_time, energy_consume_by_each_node):   
        start_time = datetime.now()
        data = [start_time, self.config.get_stat_method, self.config.get_no_of_nodes, self.config.get_no_of_faulty_nodes, self.config.get_node_avg_value,
        self.config.get_no_of_faulty_nodes, self.config.get_no_of_faulty_nodes, self.config.get_node_faulty_value, det_acc, false_alaram_rate, false_positive_rate, avg_time, energy_consume_by_each_node]
        
        with open(f'results/results-{start_time}.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            # write the header
            writer.writerow(self.header)

            # write the data
            writer.writerow(data)
