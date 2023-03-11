import numpy as np
import matplotlib.pyplot as plt

# this sets up the Matplotlib interactive windows:
%matplotlib widget

# this changes the default date converter for better interactive plotting of dates:
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (7, 10),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
plt.rcParams.update(params)


#   Note the use of datetimes in the file complicate loading a bit.
#   We recommend using pandas or xarray for more elegant solutions
#   to handling complex timeseries data. 

from pandas import read_csv
 
d = read_csv('struct.csv',delimiter='\t')
a = d.to_numpy()
struc = a[:,1:]
# print(struc)

d = read_csv('prop.csv',delimiter='\t')
a = d.to_numpy()
prop = a[:,1:]
# print(prop)

d = read_csv('inter.csv',delimiter='\t')
a = d.to_numpy()
inter = a[:,1:]
# print(inter)


prop=[]
struc=[]
inter=[]
for i in range(4):
    struc.append(struc1[(i+1)%4])
    prop.append(prop1[(i+1)%4])
    inter.append(inter1[(i+1)%4])
    # print(a)



fig =plt.figure()
lables= ["L1D","L2","L3","DRAM"]
applications=['bfs','bc','cc','pr','sssp']
ax1=fig.add_subplot(3,1,1)
ax2=fig.add_subplot(3,1,2)
ax3=fig.add_subplot(3,1,3)
ax = [ax1,ax2,ax3]
l=[0,0,0]
data_types=['struc','prop','inter']

ax[0].bar(applications, struc[0], color='c')
ax[0].bar(applications, struc[1],bottom=struc[0], color='m')
ax[0].bar(applications, struc[2],bottom=struc[1]+struc[0], color='y')
l[0]=ax[0].bar(applications, struc[3],bottom=struc[2]+struc[1]+struc[0], color='k')


ax[1].bar(applications, prop[0], color='c')
ax[1].bar(applications, prop[1],bottom=prop[0], color='m')
ax[1].bar(applications, prop[2],bottom=prop[1]+prop[0], color='y')
l[1]=ax[1].bar(applications, prop[3],bottom=prop[2]+prop[1]+prop[0], color='k')


ax[2].bar(applications, inter[0], color='c')
ax[2].bar(applications, inter[1],bottom=inter[0], color='m')
ax[2].bar(applications, inter[2],bottom=inter[1]+inter[0], color='y')
l[2]=ax[2].bar(applications, inter[3],bottom=inter[2]+inter[1]+inter[0], color='k')


# plt.legend(["L1D","L2","L3","DRAM"],loc="lower right")
    #plt.gca().set_title(data_types[i])
ax[0].set_ylabel("{} (%)".format(data_types[0]))
ax[1].set_ylabel("{} (%)".format(data_types[1]))
ax[2].set_ylabel("{} (%)".format(data_types[2]))
fig.legend(labels=lables,loc="upper center",ncol=4)
plt.savefig('grace_stack.eps', format='eps',bbox_inches='tight')
plt.show()



y = np.array([35297725.4, 52687780, 108663369.8])
total=y.sum()

mylabels = ["18%", "27%", "55%"]
fig =plt.figure()
plt.pie(y, labels = mylabels, shadow = True,textprops={'fontsize': 20})
plt.legend(["Structure","Property","intermediate"],loc="lower right")
plt.savefig('access_dist.eps', format='eps',bbox_inches='tight')
plt.show()

expt=["Baseline","Structure","Property"]
values=[1,1.42530294,1.194071821]
fig=plt.figure(figsize = (8, 5))
plt.gca().grid(zorder=0)
plt.gca().bar(expt, values, width=0.4, align='center', color='maroon', zorder=3)

# plt.bar(expt, values, color ='maroon',width = 0.4)
plt.gca().set_ylabel("Speedup")
plt.savefig('perfect_L1_cache.eps', format='eps',bbox_inches='tight')
plt.show()




base=np.asarray([1,1,1,1,1])
Property=np.asarray([1.066162547,1.044160982,1.015406397,0.9749009943,1.024007194])
struct=np.asarray([1.011388614,1.005252561,0.9754951561,0.9319993078,0.9800085373])
data=[[base],[Property],[struct]]
labels=["Baseline","Property","Structure"]
expt=["32KB_8way","64KB_16way","128KB_32way","256KB_64way","AVG speedup"]
fig=plt.figure(figsize = (8, 5))

N = 5
ind = np.arange(N) 
width = 0.25


plt.gca().grid(zorder=0)
bar1=plt.gca().bar(ind, base, width=width, label="base",zorder=3)
bar2=plt.gca().bar(ind+width, Property, width=width,  label="Property",zorder=3)
bar3=plt.gca().bar(ind+2*width, struct, width=width,  label="Structure",zorder=3)

plt.xticks(ind+width,expt)
plt.gca().set_ylabel("Speedup")

plt.legend( (bar1, bar2, bar3), labels ,loc="upper right")
plt.ylim((0.8,1.1))
plt.savefig('sensitivity.eps', format='eps',bbox_inches='tight')
plt.show()