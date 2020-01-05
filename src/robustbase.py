import statistics
import math
import numpy as np


#Author Deepak Yadav
#E-mail: dky.united@gmail.com
#This method is based on Rousseeuw and Croux

# Median absolute deviation (MAD), Gaussian efficiency 37%
def mad(data):
    if (len(data)==0):
        return None
    elif len(data)==1:
        return 0
    amd=[]                             #absolute median deviation
    median=statistics.median(data)
    for x in data:
        amd.append(abs(x-median))
    return (1.4826*statistics.median(amd))

# Sn scale estimator , Gaussian efficiency 58%
def Sn(data):

    if (len(data)==0):
        return None
    elif len(data)==1:
        return 0
    med=[]
    for i in data:
        diff=[]
        for j in data:
            diff.append(abs(i-j))
        med.append(statistics.median(diff))
    return(1.1926*(statistics.median(med)))

# Standard deviation, non-robust method
def sd(data):

    if len(data)==0:
        return None
    elif len(data)==1:
        return 0
    return (statistics.stdev(data))

# Interquartile range
def iqr(data):

    if len(data)==0:
        return None
    elif len(data)==1:
        return 0
    q75,q25=np.percentile(data,[75,25])
    return (q75,q25)

# Qn scale estimator, Gaussian effieciency 82%
def Qn(data):

    if (len(data)==0):
        return None
    elif len(data)==1:
        return 0
    diff = []
    h=0
    k=0
    for i in range(0,len(data)):
        for j in range(0,len(data)):
            if i<j:
                diff.append(abs(data[i]-data[j]))

    diff.sort()
    h=int(math.floor(len(data)/2)+1)   #h=[n/2]+1
    k=int(h*(h-1)/2)                    #k=h(h-1)/2
    return 2.2219*diff[k-1]





