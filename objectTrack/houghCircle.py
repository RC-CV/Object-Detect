import numpy as np
import cv2

def detectCircle(imagePath):
	image = cv2.imread(imagePath)
	output = image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	img = cv2.medianBlur(gray, 3)

	circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 100,
	                                   param1=50, param2=30, minRadius=40, maxRadius=60)
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
		#cv2.imshow("output", output)
		#cv2.waitKey(0)
	else:
		print("Circle not found!")

	return circles[0]