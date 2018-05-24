from scipy.optimize import leastsq
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = Axes3D(fig)
plt.xlabel("X")
plt.ylabel("Y")

print("Finish import")
# obtain data
points=[[-20.62573626,471.46892911,255.19380456],
 [-21.15098849,483.03048066,192.05824746],
 [-21.33263301,389.89186117,178.1625532 ],
 [-21.42655663,424.80617862,152.29688707],
 [-19.14068066,455.9973543,138.286151  ],
 [-13.38885987,537.40892326,133.09385216]]
points=np.array(points)
print(points.shape)

Xi=np.array(points[:,0:1]).flatten()
Yi=np.array(points[:,1:2]).flatten()
Zi=np.array(points[:,2:3]).flatten()

# create function z=ax+by^2+c
def curve_function(p,x,y):
    a,b,c=p#[1,20]
    z=a*x+b*(y**2)*(-1)+c
    return z
def error(p,x,y,z):
    return (z-curve_function(p,x,y))**2
# generate line
p0=[1,10,500]
result=leastsq(error,p0,args=(Xi,Yi,Zi))
a,b,c=result[0]
print(a,b,c)
# show result

ax.scatter(Xi,Yi,Zi,color="blue",label="Data Points",linewidth=2)
'''
x =np.linspace(0,1000,20)
y = np.linspace(0,1000,20)
z = np.linspace(0,1000,20)
z=a*x+(-b)*(y**2)+c
ax.plot(x,y,z,color="red",label="Fitting Result",linewidth=2)
'''
plt.show()
