import matplotlib.pyplot as plt
import numpy as np
import statistics
import random
import robustbase
import csv

def dist(x1,y1,x2,y2):
	return float(np.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))

# Fixing random state for reproducibility
np.random.seed(0)

#node parameter
N =20     # total no. of nodes
n=6    # total faulty nodes in network
tr=5        # transmission range of each nodes
x1=24.4       # lower threshold
x2=26.3       # upper threshold
threshold=30  #
l1,l2=0,50 # random position at which faulty nodes present
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

# injecting the faults in the nodes
faulty=random.sample(range(0,N),n)   # index of the faulty nodes
f_val=[100.0,-987,3454,-232,2000]
secure_random = random.SystemRandom()
for i in faulty:
    frame[i]=np.array([secure_random.choice(f_val) for j  in range(0,t)])


#present sensor value
for j in range(0,N):
    sensorVal[j]=frame[j][t-1]

print(sensorVal)

# Detection accuracy parameter
fault_count_mad=0
da_mad=0

f_mad=[]


#Distributed Self Fault Diagnosis Algorithm
for i in range(0,N):
    node_id=[]
    data=[]
    status = []
    no_of_ones=0
    for j in range(0, N):
        if ((neigh_node_of_i[i][j] == 1) & i!=j):
            node_id.append(j)
            data.append(sensorVal[j])

    median = statistics.median(data)

    qn = robustbase.Qn(data)

    print(frame[i])
    for k in frame[i]:
        if abs(k - median) / qn > 3:
            status.append(1)
            no_of_ones=no_of_ones+1
        else:
            status.append(0)
    print(status)
    print(no_of_ones)
    if no_of_ones==t:
        if i in faulty:
            da_mad=da_mad+1
        f_mad.append(i)
        fault_count_mad = fault_count_mad + 1




print("-------------------------MAD---------------------------")
#print("faulty injected nodes=",faulty)
print("faulty nodes=",n)
#print("faulty nodes=",f_mad)
#print("fault_detected=",fault_count_mad)
print("DA=",da_mad/n)



row = [n,da_mad/n]
with open('test.csv', 'a') as csvFile:
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