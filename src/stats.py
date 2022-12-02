import statistics
import robustbase


class Stats:
    def calculate(self, method, node_data, data_list):
        if method=='MAD':
            return Stats.median_absolute_deviation(node_data, data_list) if len(data_list)>0 else 1.5

        if method=="QN":
            return Stats.qn_scale(node_data, data_list) if len(data_list)>0 else 1.5

        if method=="SN":
            return Stats.sn_scale(node_data, data_list) if len(data_list)>0 else 1.5

        if method=="SD":
            return Stats.sd(node_data, data_list) if len(data_list)>0 else 1.5

    @staticmethod
    def median_absolute_deviation(val, data):
        median = statistics.median(data)
        nmad = robustbase.mad(data)
        return abs(val - median) / nmad if nmad!=0 else 0

    @staticmethod
    def qn_scale(val, data):
        median = statistics.median(data)
        Qn = robustbase.Qn(data)
        return abs(val - median) / Qn if Qn!=0 else 0

    @staticmethod
    def sn_scale(val, data):
        median = statistics.median(data)
        Sn = robustbase.Sn(data)
        return abs(val - median) / Sn if Sn!=0 else 0

    @staticmethod
    def sd(val, data):
        if len(data)<=2:
            return 0
            
        mean = statistics.mean(data)
        sd = statistics.stdev(data)
        return abs(val - mean) / sd if sd!=0 else 0

if __name__ == "__main__":
    import numpy as np

    np.random.seed(0)
    data = np.random.randint(-10, 10, 50)
    val = 4.0

    s = Stats()
    print(s.median_absolute_deviation(val, data))
    print(s.qn_scale(val, data))
    print(s.sn_scale(val, data))
    print(s.sd(val, data))