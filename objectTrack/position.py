import cv2
import numpy as np
import houghCircle
import cutImage
import ballDetect
import angle

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
	
	points=points[:,2:4]
	
	
	#calculate f
	distance=calDistance(700,240)
	f=fCalculate(distance,40,r)
	for i in points:
		
		#calculate distance
		pixRadius=max(abs(i))/2
		#print(i)
		print("pixRadius:",pixRadius)
		z=calZ(f,6,pixRadius)
		print("Ball distance:",z/100,"m")
		

if __name__ == '__main__':
	main()