# Statistical Method Based Algorithm for Fault Detection in Wireless Sensor Networks (WSNs)
> Using distributed self-fault diagnosis (DSFD) method, faults in wireless sensor networks (WSNs) can be
easily detected. In this method, each sensor node collects its neighbourhood sensor node data
and uses the statistical-based method for detecting its own fault status. Discussed various statistical-based method such as standard deviation, interquartile range, median
absolute deviation (MAD), Sn and Qn scale estimator for detection of the fault in WSNs. The
result of the experiment shows that standard deviation and interquartile range fails to detect the
fault, if multiple nodes are faulty, while MAD, Sn and Qn scale estimator detects the fault even
20-30% of the nodes are faulty.

## Installation

OS X , Windows & Linux:

* Clone the repository
* Install dependencies
   * pip3 install -r requirements.txt

## Usage example

modify the ```config.yaml``` file with your testing parameters then run ```python main.py```. 
Go to resources folder to see the different file for more analysis. currently four different statistical method is supported. this repo is under development, you may see many updates in future. 

```python
from src.config import Config
from src.dsfd import DSFD

def main():
    config = Config("config.yaml")
    dsfd = DSFD(config)
    print(dsfd.run())

if __name__ == "__main__":
    main()
```

## Result Comparison with different Statistical Method

|Date/Time                 |Method|Total Nodes|Total Faulty Nodes|Node Avg. Value Range|Faulty Value Range|Detection Acc.|False Alaram Rate|False Positive Rate|Avg. Stat Cal. Time|Energy|
|--------------------------|------|-----------|------------------|---------------------|------------------|--------------|-----------------|-------------------|-------------------|------|
|2022-12-05 21:28:10.513992|SD    |1000       |90                |(23.5, 25.3)         |(53.2, 80.2)      |0.93          |0.97             |0.57               |0.0                |0     |
|2022-12-05 21:31:08.852516|QN    |1000       |90                |(23.5, 25.3)         |(53.2, 80.2)      |0.9           |0.89             |0.97               |0.0                |0     |
|2022-12-05 21:32:06.578734|SN    |1000       |90                |(23.5, 25.3)         |(53.2, 80.2)      |0.83          |0.83             |0.89               |0.0                |0     |
|2022-12-05 21:35:27.070568|MAD   |1000       |90                |(23.5, 25.3)         |(53.2, 80.2)      |0.88          |0.88             |0.88               |0.0                |0     |


## For Detailed Information

Read the paper. [Read More.](https://github.com/deepak7376/wsnFault/blob/master/assets/finalConferancePaper.pdf)


## Contributing

1. Fork it (<https://github.com/deepak7376/wsnFault/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
