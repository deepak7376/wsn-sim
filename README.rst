Fault Detection in Wireless Sensor Networks (wsnFault).
==============
A key issue in the wireless sensor network applications is how to accurately detect the fault status of a node when it is working in a harsh environment. The wrong detection of nodes status can cause a lot of the damage, when it is used for critical applications. Using distributed self-fault diagnosis (DSFD) method, faults in wireless sensor networks (WSNs) can be easily detected. In this method, each sensor node collects its neighbourhood sensor node data and uses the statistical-based
method for detecting its own fault status. We propose a distributed fault detection method based on statistical Qn scale estimator. The proposed method is implemented using python language and found that Qn scale estimator shows better false alarm rate in comparison to the other statistical methods.
.. image:: /assets/wsn.png


Installation
==============
- Clone this repository
- Install dependencies
   ```bash
   pip3 install -r requirements.txt
   ```
- Run setup from the repository root directory
    ```bash
    python3 setup.py install
    ``` 
