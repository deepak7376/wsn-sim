import matplotlib.pyplot as plt
import numpy as np
import statistics
import random
import sm
import csv

def dist(x1,y1,x2,y2):
	return float(np.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))

# Fixing random state for reproducibility
np.random.seed(0)

#node parameter
N =10     # total no. of nodes
n=3    # total faulty nodes in network
tr=4        # transmission range of each nodes
x1=24.4       # lower threshold
x2=26.3       # upper threshold
threshold=30  #
l1,l2=0,100 # random position at which faulty nodes present
t=5          #frame length

# (x,y) co-ordinate where the nodes are placed
x = np.array([round(random.uniform(l1,l2),2) for i in range(0,N)])
y = np.array([round(random.uniform(l1,l2),2) for i in range(0,N)])


distance=np.array([[0.0 for i in range(0,N)] for j in range(0,N)])          #distance between the nodes
no_of_neigh=np.array([0 for i in range(0,N)])		                        #array to store no. of neighbours of a sensor i
neigh_node_of_i=np.array([[0 for i in range(0,N)] for j in range(0,N)])		#array to store the neighbours of sensor i


#loop to calculate distance between the nodes
for i in range(0,N):
	for j in range(0,N):
		distance[i][j]=dist(x[i],y[i],x[j],y[j])

#loop to calculate neighbours and their quantity
for i in range(0,N):
	for j in range(0,N):
		if distance[i][j]<=tr:
			no_of_neigh[i]=no_of_neigh[i]+1
			neigh_node_of_i[i][j]=1

# frame of every nodes
frame=np.array([[round(random.uniform(x1,x2),2) for i in range(0,t) ] for j in range(0,N)])
sensorVal=np.array([0.0 for i in range(0,N) ])
print(frame[0])

#print(frame)
# injecting the faults in the nodes
faulty=random.sample(range(0,N),n)   # index of the faulty nodes
print(faulty)
f_val=[100.0,-987,3454,-232,2000]
secure_random = random.SystemRandom()
for i in frame:
    frame[i]=np.array([secure_random.choice(f_val) for j  in range(0,t)])


#present sensor value
for j in range(0,N):
    sensorVal[j]=frame[j][t-1]

print(sensorVal[0])

# Detection accuracy parameter
fault_count_mad=0
da_mad=0
fault_count_sd=0
da_sd=0
fault_count_iqr=0
da_iqr=0
fault_count_sn=0
da_sn=0
fault_count_qn=0
da_qn=0
f_mad=[]
f_qn=[]
f_sn=[]
f_iqr=[]
f_sd=[]

#Distributed Self Fault Diagnosis Algorithm
for i in range(0,N):
    node_id=[]
    data=[]
    for j in range(0,t):
        if frame[i][j]>threshold or frame[i][j]<0:    # check if frame value above threshold
            count=count+1
    if count==t:                # when all the frame data grater than threshold
        for j in range(0, N):
            if neigh_node_of_i[i][j] == 1:
                node_id.append(j)
                data.append(sensorVal[j])

        if len(data) > 1:

            median = statistics.median(data)

            nmad = sm.nmad(data)
            Qn = sm.qn(data)
            Sn = sm.sn(data)

            if abs(sensor_val[i] - median) / nmad > 3:

                if i in faulty:
                    da_mad = da_mad + 1
                f_mad.append(i)
                fault_count_mad = fault_count_mad + 1

            if abs(sensor_val[i] - median) / Qn > 3:
                if i in faulty:
                    da_qn = da_qn + 1
                fault_count_qn = fault_count_qn + 1
                f_qn.append(i)

            if abs(sensor_val[i] - median) / Sn > 3:
                if i in faulty:
                    da_sn = da_sn + 1
                fault_count_sn = fault_count_sn + 1
                f_sn.append(i)


print("-------------------------MAD---------------------------")
#print("faulty injected nodes=",faulty)
print("faulty nodes=",n)
#print("faulty nodes=",f_mad)
#print("fault_detected=",fault_count_mad)
print("DA=",da_mad/n)

print("---------------------------QN---------------------------")

#print("faulty injected nodes=",faulty)
#print("faulty nodes=",n)
#print("faulty nodes=",f_qn)
#print("fault_detected=",fault_count_qn)
print("DA=",da_qn/n)

print("--------------------------Sn-------------------------------")
#print("faulty injected nodes=",faulty)
#print("faulty nodes=",n)
#print("faulty nodes=",f_sn)
#print("fault_detected=",fault_count_sn)
print("DA=",da_sn/n)


row = [n,da_mad/n,da_qn/n,da_sn/n]
with open('final_algorithm_25.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)
csvFile.close()

#print(sensor_val)
#print(neigh_node_of_i)
# for plotting the node diagram
#fig, ax = plt.subplots()
#ax.scatter(x, y)

#for i, txt in enumerate([z for z in range(0,N)]):
#    plt.annotate(txt, (x[i], y[i]))

#plt.show()