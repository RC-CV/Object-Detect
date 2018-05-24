from scipy.optimize import leastsq
import numpy as np
import matplotlib.pyplot as plt
from math import *
from mpl_toolkits.mplot3d import Axes3D




# create function
'''
z=v*sin(b)*t-0.5*10*t^2   vz,v
y=v*sin(a)*cos(b)*t + b   vy
x=v*cos(a)*cos(b)*t + c   vx
'''
def curve_function(p,x,y,z):
    v,vx,vy,vz,b,c,d=p
    ty=(y-b)/(vy)
    tx=(x-c)/(vx)

    remain=0
    remain+=(vz*ty-5*(ty**2)+d-z)**2
    remain+=(vz*tx-5*(tx**2)+d-z)**2
    remain+=(vy*tx+b-y)**2
    remain+=(vx*ty+c-x)**2
    remain+=(v**2-vx**2+vz**2+vy**2)

    return remain
def error(p,x,y,z,r):
    return curve_function(p,x,y,z)

def draw3DLine(points):
	fig = plt.figure()
	ax = Axes3D(fig)
	plt.xlabel("X")
	plt.ylabel("Y")

	# obtain data
	#points=np.array(points)


	Xi=np.array(points[:,0:1]).flatten()
	Yi=np.array(points[:,1:2]).flatten()
	Zi=np.array(points[:,2:3]).flatten()



	Ri=np.zeros(shape=(Xi.shape[0],))
	# generate line
	sumX=sum(Xi)
	if(sumX<Xi[0]*Xi.shape[0]):
		p0=[100,-10,100,100,136,-30,100]
	else:
		p0=[100,10,100,100,136,-30,100]

	result=leastsq(error,p0,args=(Xi,Yi,Zi,Ri),maxfev=2000)
	v,vx,vy,vz,b,c,d=result[0]
	print(v,vx,vy,vz,b,c,d)
	# show result
	ax.scatter(Xi,Yi,Zi,color="blue",label="Data Points",linewidth=2)
	x=[]
	y=[]
	z=[]
	for item in range(200):
		t=item/20
		z.append(vz*t-5*(t**2)+d)
		y.append(vy*t+b)
		x.append(vx*t+c)
	#print(x,y,z)
	ax.scatter(x,y,z,color="red",label="Data Points",linewidth=2)
	'''
	ax.plot(x,y,z,color="red",label="Fitting Result",linewidth=2)
	'''
	plt.show()
