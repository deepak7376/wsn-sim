import matplotlib.pyplot as plt
import csv

x=[]
y_mad=[]
y_qn=[]
y_sn=[]
y_iqr=[]
y_sd=[]

with open('exp5_new_RT.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y_mad.append(float(row[1]))
        y_qn.append(float(row[2]))
        y_sn.append(float(row[3]))
        y_iqr.append(float(row[4]))
        y_sd.append(float(row[5]))

plt.plot(x,y_mad,label='mad'.format(1),color='r')
plt.plot(x,y_qn,label='Qn'.format(2),color='b')
plt.plot(x,y_sn,label='Sn'.format(3),color='g')
plt.plot(x,y_iqr,label='IQR'.format(4),color='black')
plt.plot(x,y_sd,label='SD'.format(5),color='yellow')
plt.grid()

plt.xlabel('Number of neighbourhood nodes')
plt.ylabel('Running time')
plt.title('Running Time')
plt.legend(loc='best')
plt.show()