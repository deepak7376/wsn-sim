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

After cloning and installation, create config.yaml file with your setup. and from main.py put the config.yaml path. and run it. go to the result dir to export your result.

```python
from src.config import Config
from src.dsfd import DSFD

def main():
    config = Config("config.yaml")
    dsfd = DSFD(config)
    print(dsfd.detection_accuracy())

if __name__ == "__main__":
    main()
```

## For Detailed Information

Read the paper. [Read More.](https://github.com/deepak7376/wsnFault/blob/master/assets/finalConferancePaper.pdf)


## Contributing

1. Fork it (<https://github.com/deepak7376/wsnFault/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
