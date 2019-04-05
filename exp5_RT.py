import statistics
import math
import numpy as np
import random
import timeit
import csv
import robustbase


#parameters
Neg=60 # number of neighbourhood nodes
x1=24.4 # lower threshold
x2=26.3 #upper threshold

sensor_val=np.array([round(random.uniform(x1,x2),2) for i in range(0,Neg) ])


start1 = timeit.default_timer()
print(robustbase.mad(sensor_val))
stop1 = timeit.default_timer()
print('Time: ', stop1 - start1)

start2 = timeit.default_timer()
print(robustbase.Qn(sensor_val))
stop2 = timeit.default_timer()
print('Time: ', stop2 - start2)

start3 = timeit.default_timer()
print(robustbase.Sn(sensor_val))
stop3 = timeit.default_timer()
print('Time: ', stop3 - start3)

start4 = timeit.default_timer()
print(robustbase.iqr(sensor_val))
stop4 = timeit.default_timer()
print('Time: ', stop4 - start4)

start5 = timeit.default_timer()
print(robustbase.sd(sensor_val))
stop5 = timeit.default_timer()
print('Time: ', stop5 - start5)

# for writing in csv file
row =[Neg,stop1-start1,stop2-start2,stop3-start3,stop4-start4,stop5-start5]

with open('exp5_new_RT.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)
csvFile.close()
