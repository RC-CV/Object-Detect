import cv2
import numpy as np
import houghCircle
import cutImage
import ballDetect
import angle
import math

def calDistance(height,length):
	return (height**2+length**2)**0.5

def fCalculate(distance,radius,pixRadius):
	return distance*pixRadius/radius

def calZ(f,radius,pixRadius):
	return f*radius/pixRadius


def main():
	videoPath='jin1.avi'
	camera = cv2.VideoCapture(videoPath)
	res,image=camera.read()
	res,image=camera.read()
	if not res:
		print("Image not captured!")
		return

	camera.release()
	#cv2.imshow("output", image)
	#Find circle
	(x,y,r)=houghCircle.detectCircle(image)
	#Crop ball,x,y,w,h
	points=np.array(ballDetect.detect_video(videoPath))
	
	#coordinate in image
	pointPos=np.array(points[:,0:3],dtype='float64',copy=True)

	#Fetch width and height
	points=points[:,2:4]
	
	
	disHor=700
	disVer=240
	ringActual=40

	#calculate ring distance
	distance=calDistance(disHor,disVer)
	
	#calculate f
	f=fCalculate(distance,ringActual,r)
	for (i,j) in zip(points,pointPos):
		
		#calculate distance
		pixRadius=max(abs(i))/2
		#print(i)
		print("pixRadius:",pixRadius)
		#calculate distance
		z=calZ(f,6,pixRadius)
		print("Ball distance:",z/100,"m")
		
		#position ---float (x,y,Z),Z-->(cm)
		#store distance
		j[2]=z
	
	

	#store rectangel coordinate
	coordinate=[]
	resolution=np.array([image.shape[1],image.shape[0]])#640,480
	rate=r/ringActual
	cameraAngle=math.pi/3# 60degree

	for p in pointPos:
		#Calculate angels
		xAngle,yAngle = angle.calAngle(cameraAngle,p[:2],resolution,rate,p[2])
		#Calcualte coordinate
		point=angle.calRectCoordin(xAngle,yAngle,p[2])
		coordinate.append(point)
	print(np.array(coordinate))


if __name__ == '__main__':
	main()