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

def calRectCoordin(xAngle,yAngle,distance):
	x=distance*math.cos(yAngle)*math.sin(xAngle)
	y=distance*math.cos(yAngle)*math.cos(xAngle)
	z=distance*math.sin(yAngle)

	return [x,y,z]