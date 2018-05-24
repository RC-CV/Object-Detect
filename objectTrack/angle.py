import math
import numpy as np
def calAngle(cameraAngle,pointPos,resolution,rate,distance):
	'''
	Argument:
	cameraAngle ---摄像机昂角
	pointPos	---像素坐标(x,y)
	resolution	---分辨率(x,y) np.array
	rate		---比率：像素/实际
	distance	---距离
	'''
	#Extract info
	x,y=pointPos
	xMid,yMid=resolution/2
	d=distance*rate

	xMinus=x-xMid
	yMinus=yMid-y


	#calculate xAngle
	xAngle=math.asin(xMinus/d)
	#calculate yAngle
	yAngle=cameraAngle+math.asin(yMinus/d)

	'''
	xAngle,yAngle ---弧度
	'''
	return xAngle,yAngle

def calRectCoordin(xAngle,yAngle,distance,camHight):
	x=distance*math.cos(yAngle)*math.sin(xAngle)
	y=distance*math.cos(yAngle)*math.cos(xAngle)
	z=distance*math.sin(yAngle)+camHight

	return [x,y,z]

def calCamerAngle(pointPos,resolution,rate,distance,disVer,camHight):
	'''
	Argument:
	pointPos	---像素坐标(x,y)
	resolution	---分辨率(x,y) np.array
	rate		---比率：像素/实际
	distance	---直线实际距离
	disHor		---水平实际距离
	'''
	#Extract info
	_,y=pointPos
	_,yMid=resolution/2
	d=distance*rate

	yMinus=yMid-y

	#calculate yAngle
	yAngle = math.asin((disVer-camHight)/distance)
	cameraAngle=yAngle-math.asin(yMinus/d)

	'''
	cameraAngle ---弧度
	'''
	return cameraAngle