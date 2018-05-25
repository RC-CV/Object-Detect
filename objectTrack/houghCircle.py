import numpy as np
import cv2

def detectCircle(image,disHor):
	output = image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	img = cv2.medianBlur(gray, 3)

	
	if(image.shape[0]>700):
		cirDis=800
		rate=2
	elif(image.shape[0]>400):
		cirDis=400
		rate=1
	else:
		cirDis=200
		rate=0.5

	print('image.shape[0]',image.shape[0],'rate:',rate)

	if(disHor>=500):
		minR=int(40*rate)
		maxR=int(80*rate)
	else:
		minR=int(60*rate)
		maxR=int(120*rate)

	print('minR:',minR,"maxR:",maxR)

	circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, cirDis,
	                                   param1=50, param2=30, minRadius=minR, maxRadius=maxR)
	if circles is not None:
		# convert the (x, y) coordinates and radius of the circles to integers
		circles = np.round(circles[0, :]).astype("int")
	 
		# loop over the (x, y) coordinates and radius of the circles
		for (x, y, r) in circles:
			# draw the circle in the output image, then draw a rectangle
			# corresponding to the center of the circle
			cv2.circle(output, (x, y), r, (0, 255, 0), 4)
			cv2.circle(output, (x, y), 2, (0, 128, 255), -1)
	 
		# show the output image
		cv2.imshow("output", output)
		cv2.waitKey(0)
	else:
		print("Circle not found!")

	return circles[0]

if __name__ == '__main__':
	disHor=600
	#videoPath='/mnt/hgfs/Virtural Share doc/data/7m/In3.avi'
	#videoPath='/mnt/hgfs/Virtural Share doc/rc_data_5.24/single_eye_640/6m/In2.avi'
	#videoPath='/mnt/hgfs/Virtural Share doc/rc_data_5.24/double_eye_320/leftIn2.avi'
	videoPath='/mnt/hgfs/Virtural Share doc/rc_data_5.24/single_eye_1280/6mFirst/NotIn1.avi'
	camera = cv2.VideoCapture(videoPath)
	res,image=camera.read()
	res,image=camera.read()
	

	camera.release()
	#Find circle，霍夫变换获取圆环位置
	if res:
		print("Image captured!")
		(x,y,r)=detectCircle(image,disHor)
		print('(',x,y,r,')')
	else:
		print("Image not Captured!")