# Statistical Method Based Algorithm for Fault Detection in Wireless Sensor Networks (WSNs)
> A key issue in the wireless sensor network applications is how to accurately detect the fault status of a node when it is working in a harsh environment. The wrong detection of nodes status
can cause a lot of the damage especially when it is used for critical applications. Using distributed self-fault diagnosis (DSFD) method, faults in wireless sensor networks (WSNs) can be
easily detected. In this method, each sensor node collects its neighbourhood sensor node data
and uses the statistical-based method for detecting its own fault status. In this paper, we discussed various statistical-based method such as standard deviation, interquartile range, median
absolute deviation (MAD), Sn and Qn scale estimator for detection of the fault in WSNs. The
result of the experiment shows that standard deviation and interquartile range fails to detect the
fault, if multiple nodes are faulty, while MAD, Sn and Qn scale estimator detects the fault even
20-30% of the nodes are faulty.

## Installation

OS X , Windows & Linux:

* Clone the repository
* Install dependencies
   * pip3 install -r requirements.txt
* Run setup from the repository root directory
   * python3 setup.py install

## For Detailed Information

Read the paper. [Read More.](https://github.com/deepak7376/wsnFault/blob/master/assets/finalConferancePaper.pdf)

## Meta

Deepak Yadav – [@imdeepak_dky](https://twitter.com/imdeepak_dky) – dky.united@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/deepak7376/wsnFault/blob/master/LICENSE](https://github.com/deepak7376)

## Contributing

1. Fork it (<https://github.com/deepak7376/wsnFault/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
