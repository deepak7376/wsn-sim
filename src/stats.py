import statistics
import robustbase

class Stats:
    @staticmethod
    def median_absolute_deviation(val, data):
        median = statistics.median(data)
        nmad = robustbase.mad(data)
        return abs(val - median) / nmad if nmad!=0 else 0