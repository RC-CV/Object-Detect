from scipy.optimize import leastsq
import numpy as np
import matplotlib.pyplot as plt
from math import *
from mpl_toolkits.mplot3d import Axes3D




# create function
'''
z=v*sin(q)*t-0.5*10*t^2   vz,v
y=v*sin(a)*cos(q)*t + b   vy
x=v*cos(a)*cos(q)*t + c   vx
'''
def curve_function(p,x,y,z):
    v,vx,vy,vz,b,c,d=p
    '''
    vx=v*cos(a)*cos(q)
    vy=v*sin(a)*cos(q)
    vz=v*sin(q)
	'''
    ty=(y-b)/(vy)
    tx=(x-c)/(vx)

    remain=0
    remain+=(vz*ty-5*(ty**2)+d-z)**2
    remain+=(vz*tx-5*(tx**2)+d-z)**2
    remain+=(vy*tx+b-y)**2
    remain+=(vx*ty+c-x)**2
    remain+=(v**2-(vx**2+(vz)**2+vy**2))

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
	points2=points.copy()
	if(len(points2)<7):
		points=np.vstack((points,points2))


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

	result=leastsq(error,p0,args=(Xi,Yi,Zi,Ri))
	v,vx,vy,vz,b,c,d=result[0]
	print("v={:.2f} vx={:.2f} vy={:.2f} vz={:.2f} b={:.2f} c={:.2f} d={:.2f} ".format(v,vx,vy,vz,b,c,d));
	print("z={:.2f}*t-5*t^2+{:.2f} y={:.2f}*t+{:.2f} x={:.2f}*t+{:.2f} v={:.2f}".format(vz,d,vy,b,vx,c,v));
	#print("values:",v,vx,vy,vz,b,c,d)
	# show result
	ax.scatter(Xi,Yi,Zi,color="blue",label="Data Points",linewidth=2)
	x=[]
	y=[]
	z=[]

	startItm=(Yi[0]-b)/vy
	endItm=(Yi[-1]-b)/vy
	#print(Yi[0],Yi[-1],startItm,endItm)
	rangeItm=abs(endItm-startItm)*1.5
	iterNum=200
	for item in range(iterNum):
		t=item*(rangeItm/iterNum)+startItm
		z.append(vz*t-5*(t**2)+d)
		y.append(vy*t+b)
		x.append(vx*t+c)
	#print(x,y,z)
	#ax.scatter(x,y,z,color="red",label="Data Points",linewidth=2)
	'''
	ax.plot(x,y,z,color="red",label="Fitting Result",linewidth=2)
	'''
	ax.plot(x, y, z, label='Fitting curve',color="red")
	ax.legend()
	#plt.show()
	return (vx,vy,vz,b,c,d)

def predictBallPos(disHor,p):
	(vx,vy,vz,b,c,d)=p
	t=(disHor-b)/vy
	z=vz*t-5*(t**2)+d
	x=vx*t+c
	return x,z

def pointDistance(points,p):
	(vx,vy,vz,b,c,d)=p
	result=[]
	for point in points2:
		t=(point[1]-b)/vy
		z=vz*t-5*(t**2)+d
		x=vx*t+c
		distance = ((x-point[0])**2+0+(z-point[2])**2)**0.5
		result.append(distance)
	return distance
