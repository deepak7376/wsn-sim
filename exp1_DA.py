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
N =1000     # total no. of nodes
n=500     # total faulty nodes in network
tr=56        # transmission range of each nodes
x1=24.4       # lower threshold
x2=26.3       # upper threshold
l1,l2=0,1000  #node lies between (0,1000)

# Sensor value assignment
sensor_val=np.array([round(random.uniform(x1,x2),2) for i in range(0,N) ])

# (x,y) co-ordinate of sensor node
x = np.array([round(random.uniform(l1,l2),2) for i in range(0,N)])
y = np.array([round(random.uniform(l1,l2),2) for i in range(0,N)])



distance=np.array([[0.0 for i in range(0,N)] for j in range(0,N)])
no_of_neigh=np.array([0 for i in range(0,N)])		#array to store no. of neighbours of a sensor i
neigh_node_of_i=np.array([[0 for i in range(0,N)] for j in range(0,N)])		#array to store the neighbours of sensor i


for i in range(0,N):						#loop to calculate distance between the nodes
	for j in range(0,N):
		distance[i][j]=dist(x[i],y[i],x[j],y[j])

for i in range(0,N):						#loop to calculate neighbours and their quantity
	for j in range(0,N):
		if distance[i][j]<=tr:
			no_of_neigh[i]=no_of_neigh[i]+1
			neigh_node_of_i[i][j]=1


#fault injecting on the node
faulty=random.sample(range(l1,l2),n)
f_val=[100.0,-987,3454,-232,2000]
secure_random = random.SystemRandom()
for i in faulty:
	sensor_val[i]=secure_random.choice(f_val)


# implementattion of algorithm

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

for i in range(0,N):
    node_id = []
    data = []
    for j in range(0, N):
        if neigh_node_of_i[i][j] == 1:
            node_id.append(j)
            data.append(sensor_val[j])

    if len(data)>1:
        # print("node no=",i)
        # print("node id=",node_id)
        # print("data=",data)
        median = statistics.median(data)
        mean = statistics.mean(data)
        # print("median=",median)
        # for w in data:
        #   amd.append(abs(w-median))
        # print("med dev=",amd)
        nmad = robustbase.mad(data)
        Qn = robustbase.Qn(data)
        Sn = robustbase.Sn(data)
        q75, q25 = robustbase.iqr(data)
        SD = robustbase.sd(data)
        # print("nmad=",nmad)
        # print("seVal=",sensor_val[i])
        # print("seVal-med",abs(sensor_val[i]-median),"3*nmad=",3*nmad)
        if abs(sensor_val[i] - median) / nmad > 3:
            # print("Faulty_mad")
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

        if abs(sensor_val[i] - mean) / SD > 3:
            fault_count_sd = fault_count_sd + 1
            f_sd.append(i)
            if i in faulty:
                da_sd = da_sd + 1

        if ((q25 - 1.5 * (q75 - q25)) > sensor_val[i] or sensor_val[i] > (q25 + 1.5 * (q75 - q25))):
            fault_count_iqr = fault_count_iqr + 1
            f_iqr.append(i)
            if i in faulty:
                da_iqr = da_iqr + 1

print("faulty nodes=",n)
print("-------------------------MAD---------------------------")
#print("faulty injected nodes=",faulty)
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

print("----------------------------IQR----------------------------")
#print("faulty injected nodes=",faulty)
#print("faulty nodes=",n)
#print("faulty nodes=",f_iqr)
#print("fault_detected=",fault_count_iqr)
print("DA=",da_iqr/n)

print("-------------------------SD--------------------------------")
#print("faulty injected nodes=",faulty)
#print("faulty nodes=",n)
#print("faulty nodes=",f_sd)
#print("fault_detected=",fault_count_sd)
print("DA=",da_sd/n)

# for writing in csv file
row = [n,da_mad/n,da_qn/n,da_sn/n,da_iqr/n,da_sd/n]
with open('exp1_new_56.csv', 'a') as csvFile:
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