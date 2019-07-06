# Statistical Method Based Fault Detection Algorithm for Wireless Sensor Networks (WSNs).
This project is based on fault detection in WSNs using statistical methods.
There are five experiment is performed 
1. Detection Accuracy
2. False Alarm Rate
3. False Positive Rate
4. Total Energy Consumption
5. Running Time

Q. How this algorithm work ?
A. There are five statistical methods are used Median Absolute Deviation (MAD), Qn scale estimator, Sn scale estimator, IQR and Standard deviation.

All the nodes first sense the data from environment after that they collects its neighbours data for the fault detction.
if data is grater than 3*sigma then they are considered as faulty.
