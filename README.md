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

After cloning and installation, create config.yaml file with your setup. and from main.py put the config.yaml path. and run it. go to the resources dir to export your result.

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

|Date/Time                 |Stat. Method|Total Nodes|Total Faulty Nodes|Node Avg. Value Range|Faulty Value Range|Detection Acc.|False Alaram Rate|False Positive Rate|Avg. Stat Cal. Time|Energy             |FIELD12               |FIELD13|
|--------------------------|------------|-----------|------------------|---------------------|------------------|--------------|-----------------|-------------------|-------------------|-------------------|----------------------|-------|
|2022-12-03 00:18:19.226046|MAD         |100        |25                |(23.5, 25.3)         |25                |25            |(53.2, 80.2)     |0.84               |0.9487179487179487 |0.45454545454545453|2.133846282958984e-06 |0      |
|2022-12-03 00:24:04.986332|MAD         |100        |25                |(23.5, 25.3)         |25                |25            |(53.2, 80.2)     |0.79               |0.8961038961038961 |0.43478260869565216|2.2649765014648438e-06|0      |
|2022-12-03 00:24:08.447307|MAD         |100        |25                |(23.5, 25.3)         |25                |25            |(53.2, 80.2)     |0.83               |0.9230769230769231 |0.5                |2.0503997802734374e-06|0      |
|2022-12-03 00:24:10.787560|MAD         |100        |25                |(23.5, 25.3)         |25                |25            |(53.2, 80.2)     |0.79               |0.9125             |0.3                |1.8572807312011719e-06|0      |
|2022-12-03 00:24:14.048503|MAD         |100        |25                |(23.5, 25.3)         |25                |25            |(53.2, 80.2)     |0.79               |0.9102564102564102 |0.36363636363636365|2.157688140869141e-06 |0      |
|2022-12-03 00:39:55.361962|QN          |100        |25                |(23.5, 25.3)         |25                |25            |(53.2, 80.2)     |0.86               |0.9493670886075949 |0.5238095238095238 |4.084110260009765e-06 |0      |
|2022-12-03 00:39:58.558212|QN          |100        |25                |(23.5, 25.3)         |25                |25            |(53.2, 80.2)     |0.77               |0.8974358974358975 |0.3181818181818182 |2.8109550476074217e-06|0      |
|2022-12-03 00:40:59.702895|SN          |100        |25                |(23.5, 25.3)         |25                |25            |(53.2, 80.2)     |0.79               |0.8734177215189873 |0.47619047619047616|3.4165382385253906e-06|0      |
|2022-12-03 00:46:33.443979|SD          |100        |25                |(23.5, 25.3)         |25                |25            |(53.2, 80.2)     |0.8                |0.9493670886075949 |0.23809523809523808|2.1622180938720703e-05|0      |
|2022-12-03 00:46:35.883005|SD          |100        |25                |(23.5, 25.3)         |25                |25            |(53.2, 80.2)     |0.78               |0.9743589743589743 |0.09090909090909091|1.5265941619873047e-05|0      |
|2022-12-03 00:46:38.085791|SD          |100        |25                |(23.5, 25.3)         |25                |25            |(53.2, 80.2)     |0.76               |0.9743589743589743 |0.0                |1.230001449584961e-05 |0      |

## For Detailed Information

Read the paper. [Read More.](https://github.com/deepak7376/wsnFault/blob/master/assets/finalConferancePaper.pdf)


## Contributing

1. Fork it (<https://github.com/deepak7376/wsnFault/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
