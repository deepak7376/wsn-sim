import csv
from datetime import datetime


class Generate_csv:
    def __init__(self, config) -> None:
        self.config = config
       
    def generate_result_csv(self, det_acc, false_alaram_rate, false_positive_rate, avg_time, energy_consume_by_each_node):   
        start_time = datetime.now()
        header = ['Date/Time', 'Stat. Method', 'Total Nodes', 'Total Faulty Nodes', 'Node Avg. Value Range', 'Faulty Value Range', 'Detection Acc.', 'False Alaram Rate', 'False Positive Rate', 'Avg. Stat Cal. Time', 'Energy']
        data = [start_time, self.config.get_stat_method, self.config.get_no_of_nodes, self.config.get_no_of_faulty_nodes, self.config.get_node_avg_value,
        self.config.get_no_of_faulty_nodes, self.config.get_no_of_faulty_nodes, self.config.get_node_faulty_value, det_acc, false_alaram_rate, false_positive_rate, avg_time, energy_consume_by_each_node]
        
        with open(f'resources/results.csv', 'a', encoding='UTF8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)

    def generate_cm_csv(self, data):
        field_names = ['node_id', 'actual_status', 'predicted_status']
        with open('resources/confusion_matrix.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = field_names)
            writer.writeheader()
            writer.writerows(data)
