## wsnFault for Fault Detection in Wireless Sensor Networks (WSNs).
A key issue in the wireless sensor network applications is how to accurately detect the fault status of a node when it is working in a harsh environment. The wrong detection of nodes status can cause a lot of the damage, when it is used for critical applications. Using distributed self-fault diagnosis (DSFD) method, faults in wireless sensor networks (WSNs) can be easily detected. In this method, each sensor node collects its neighbourhood sensor node data and uses the statistical-based
method for detecting its own fault status. We propose a distributed fault detection method based on statistical Qn scale estimator. The proposed method is implemented using python language and found that Qn scale estimator shows better false alarm rate in comparison to the other statistical methods.
![WSN architecture](assets/wsn.png)

## Objective & Motivation
Wireless Sensor Networks (WSNs) are used for many critical applications such as health monitor, military purpose, fire detection and many more applications. The reliability of these applications are totally dependent on correctness of
data received by WSNs. To maintain the reliability of these applications faulty data must be detected and eliminated before sending it to base station. We designed an algorithm which is based on the statistical method which can easily detect the faulty node in the network and eliminate the faulty data. There are many algorithm based on statistical method already exists. I have done a comparison study between these statistical method based on different parameters, such as detection accuracy (DA), false alarm rate (FAR), false positive rate (FPR), total energy consumption (TEC) and running time (RT). This project is based on fault detection in WSNs using statistical methods.

## Contribution
Our proposed algorithm is based on the most robust scale estimator (Qn scale estimator). There are several other scale estimators such as median absolute deviation (MAD), interquartile range (IQR), Sn scale estimator, Hodges Lehmann estimator, etc. are present but among them, Qn scale estimator performance is more satisfactory. The Qn scale estimator having Gaussian efficiency 82%, a more efficient estimator needs fewer observations than the less efficient one to achieve a given performance. Financial companies now using these estimators on daily basis in analysis of the behaviour of stocks. The detailed analysis of Qn scale estimator is given in the subsequent section.

There are five experiment is performed 
1. Detection Accuracy (DA)
2. False Alarm Rate (FAR)
3. False Positive Rate (FPR)
4. Total Energy Consumption (TEC)
5. Running Time (RT)
 
All the reading associated with experiment are store in CSV file.

Q. How this algorithm work ?
A. There are five statistical methods are used Median Absolute Deviation (MAD), Qn scale estimator, Sn scale estimator, IQR and Standard deviation.

## Installation
1. Clone this repository
2. Install dependencies
   ```bash
   pip3 install -r requirements.txt
   ```
3. Run setup from the repository root directory
    ```bash
    python3 setup.py install
    ``` 
