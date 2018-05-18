import cv2
import numpy as np
import houghCircle
import cutImage

def calDistance(height,length):
	return (height**2+length**2)**0.5

def fCalculate(distance,radius,pixRadius):
	return distance*pixRadius/radius

def calZ(f,radius,pixRadius):
	return f*radius/pixRadius


def main():
	imagePath="Moment_ball0.jpg"
	#Find circle
	(x,y,r)=houghCircle.detectCircle(imagePath)
	#Crop ball
	points=np.array(cutImage.cut(imagePath))

	#calculate f
	distance=calDistance(700,300)
	f=fCalculate(distance,40,r)

	#calculate distance
	pixRadius=min(abs(points[0]-points[1]))/2
	z=calZ(f,15,pixRadius)
	print("Ball distance:",z/100,"m")

if __name__ == '__main__':
	main()