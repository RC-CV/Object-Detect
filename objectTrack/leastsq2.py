from scipy.optimize import leastsq
import numpy as np
import matplotlib.pyplot as plt
from math import *
from mpl_toolkits.mplot3d import Axes3D




# create function
'''
z=v*sin(a)*t-0.5*10*t^2
y=v*sin(a)*cos(b)*t + b
x=v*cos(a)*cos(b) + c
'''
def curve_function(p,y,z):
    v,q,a,b,d=p
    ty=(y-b)/(v*sin(a)*cos(q))
    
    remain=0
    remain+=(v*sin(q)*ty-5*(ty**2)+d-z)**2

    return remain
def line_func(p,x):
	k,b=p#[1,20]
	y=k*((x))+b
	return y


def error_curve(p,y,z,r):
    return (z-curve_function(p,y,z))**2
def error_line(p,x,y):
	return y-line_func(p,x)


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
	p0=[100,1.4,1.5,136,100]
	p1=[1,-20]

	result=leastsq(error_curve,p0,args=(Yi,Zi,Ri))
	v,q,a,b,d=result[0]

	lineResult=leastsq(error_line,p1,args=(Yi,Xi))
	k,c=lineResult[0]

	print(v,q,a,b,d)
	print(k,c)
	# show result
	ax.scatter(Xi,Yi,Zi,color="blue",label="Data Points",linewidth=2)
	x=[]
	y=[]
	z=[]

	startT=(Yi[0]-b)/(v*sin(a)*cos(q))
	for item in range(150):
		t=startT+item/20
		z1=v*sin(q)*t-5*(t**2)+d
		y1=v*sin(a)*cos(q)*t+b
		x1=y1*k+c
		z.append(z1)
		y.append(y1)
		x.append(x1)
	#print(x,y,z)
	ax.scatter(x,y,z,color="red",label="Data Points",linewidth=2)
	'''
	ax.plot(x,y,z,color="red",label="Fitting Result",linewidth=2)
	'''
	plt.show()
