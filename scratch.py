import matplotlib.pyplot as plt
import numpy as np
import random
import csv

def dist(x1,y1,x2,y2):
	return float(np.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))

# Fixing random state for reproducibility
np.random.seed(0)

#node parameter
N =1000     # total no. of nodes
n=50    # total faulty nodes in network
tr=250        # transmission range of each nodes
x1=24.4       # lower threshold
x2=26.3       # upper threshold
l1,l2=0,1000 # random position at which faulty nodes present
b=45*pow(10,-9)
a2=0.001*pow(10,-12)
a1=45*pow(10,-9)
TEC=0

sensor_val=np.array([round(random.uniform(x1,x2),2) for i in range(0,N) ])

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
f_val=[100.0,-987,3454,-232,2000]
secure_random = random.SystemRandom()
faulty=random.sample(range(l1,l2),n)
for i in faulty:
	sensor_val[i]=secure_random.choice(f_val)

Energy=[]

for i in [5]:
    Ei=0
    Etx=32*(a1+a2*pow(56,4))
    Erx=-abs(32)*b  # it substract the itself data
    node_id = []
    data = []
    #amd = []
    for j in range(0, N):
        if neigh_node_of_i[i][j] == 1:
            node_id.append(j)
            data.append(sensor_val[j])

            Erx=Erx+abs(32)*b
    Ei=Etx+Erx
    Energy.append(Ei)
    # print("node no=",i)
    # print("node id=",node_id)
    #print("data=",data)
print("no. of neighbour:")
print(len(node_id))
print(len(data))
print("total energy:")
TEC=sum(Energy)
print(TEC)

# for writing in csv file
row = [len(node_id),TEC]
with open('TEC_new.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)
csvFile.close()
'''''
#print(sensor_val)
#print(neigh_node_of_i)
# for plotting the node diagram
fig, ax = plt.subplots()
ax.scatter(x, y,color='g')
for i in faulty:
    ax.scatter(x[i], y[i],color='r')

#for i, txt in enumerate([z for z in range(0,N)]):
#    plt.annotate(txt, (x[i], y[i]))

plt.show()
'''