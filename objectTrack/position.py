import cv2
import numpy as np
import houghCircle
import cutImage
import ballDetect
import angle
import math
import line
import leastsq
import cluster
import time

def lengthRecal(rate,disHor,xPixel):
	'''
	Argument:
	rate	---actual/pixel
	disHor	--水平距离
	xPixel  --环中心与图片中轴线之差

	Return:
	Actual horizontal distance
	'''
	xd=rate*xPixel
	return (xd**2+disHor**2)**0.5


#计算摄像机与环中心距离
def calDistance(height,length):
	return (height**2+length**2)**0.5
#计算焦距
def fCalculate(distance,radius,pixRadius):
	return distance*pixRadius/radius
#利用焦距、球实际半径、球像素半径，计算球与摄像机实际距离
def calZ(f,radius,pixRadius):
	return f*radius/pixRadius

def imageToPoints(image,disHor,videoPath,showIt):
	#Find circle，霍夫变换获取圆环位置
	(x,y,r)=houghCircle.detectCircle(image,disHor,showIt)

	#Crop ball,x,y,w,h，利用前景提取获得球的位置与范围（在照片中）
	list,isDetect=ballDetect.detect_video(videoPath,(x,y,r),showIt)
	points=np.array(list)

	return x,y,r,points,isDetect
#计算三维坐标系
def obtainCoordinate(image,disHor,disVer,ringActual,cameraHight,ballR,points,x,y,r):


	#coordinate in image，创建记录球实际坐标的数组
	pointPos=np.array(points[:,0:3],dtype='float64',copy=True)

	#Fetch width and height，截取球的范围数据
	points=points[:,2:4]


	#calculate ring distance，计算环的实际距离
	length=lengthRecal(ringActual/r,disHor,x-image.shape[1]/2)
	distance=calDistance(disVer-cameraHight,length)
	#print("Distance",distance)


	#calculate f，计算焦距
	f=fCalculate(distance,ringActual,r)
	for (i,j) in zip(points,pointPos):

		#calculate distance，计算球半径（像素）
		pixRadius=abs(i[0])/2
		#print(i)
		#print("pixRadius:",pixRadius)
		#calculate distance，计算球距离（实际）
		z=calZ(f,ballR,pixRadius)
		#print("Ball distance:",z/100,"m")

		#position ---float (x,y,Z),Z-->(cm)
		#store distance，记录球的坐标（像素）与距离（实际）
		j[2]=z
		j[0]+=pixRadius
		j[1]+=(i[1]-pixRadius)

	#store rectangel coordinate，创建数组记录球的三维直角坐标（真实）
	coordinate=[]
	#get resolution,获取图片分辨率
	resolution=np.array([image.shape[1],image.shape[0]])#640,480

	rate=r/ringActual

	cameraAngle=angle.calCamerAngle((x,y),resolution,rate,distance,disVer,cameraHight)

	xAngle,yAngle = angle.calAngle(cameraAngle,(x,y),resolution,rate,distance)
	ringXYZ = angle.calRectCoordin(xAngle,yAngle,distance,cameraHight)
	#print("Ring X,Y,Z",ringXYZ,"camera angle",cameraAngle)

	for p in pointPos:
		#Calculate angels
		xAngle,yAngle = angle.calAngle(cameraAngle,p[:2],resolution,rate,p[2])
		#Calcualte coordinate
		point=angle.calRectCoordin(xAngle,yAngle,p[2],cameraHight)
		coordinate.append(point)

	#line.drawGraph(coordinate)
	#print(np.array(coordinate))
	coordinate=np.round(np.array(coordinate),decimals=2)
	print('\n',coordinate.tolist())
	return coordinate,ringXYZ

def main(videoPath,expect,showIt):
	start = time.time()
	'''
	Argument:
	disHor			--圆环中心距离机器人水平距离
	disVer			--圆环中心距离机器人垂直距离
	ringActual		--圆环实际半径大小
	cameraHight		--摄像机高度
	ballR			--球的实际半径
	'''
	disHor=600
	disVer=200
	robotR=20
	ringActual=40
	cameraHight=20
	ballR=17


	disHor-=robotR
	disVer+=ringActual

	#pathL,pathR=videoPath

	camera = cv2.VideoCapture(videoPath)
	res,image=camera.read()
	res,image=camera.read()
	if not res:
		print("Image not captured!")
		return

	camera.release()

	x,y,r,points,isDetect=imageToPoints(image,disHor,videoPath,showIt)

	if(not isDetect):
		return decide(0,expect)
	if(len(points)>7):
		points=cluster.clustering(points,showIt)

	#如果检测出来的球个数少于7个，则无法进行曲线拟合，跳出循环
	print('points number:',len(points))
	if(len(points)<4):
		print("Detected Ball not enough, Exit System")
		return decide(0,expect)

	coordinate,ringXYZ=obtainCoordinate(image,disHor,disVer,ringActual,cameraHight,ballR,points,x,y,r)



	if(max(coordinate[1])<disHor/3):
		return decide(0,expect)


	line.drawGraph(coordinate.tolist(),showIt)
	bp=leastsq.draw3DLine(coordinate,showIt)
	bx,bz=leastsq.predictBallPos(disHor,bp)
	print("Ball position around ring\n (x,y,z)=({:.2f},{:.2f},{:.2f})".format(bx,disHor,bz))
	print("Ring position:\n (x,y,z)=({:.2f},{:.2f},{:.2f})".format(ringXYZ[0],ringXYZ[1],ringXYZ[2]))

	if(disVer-ringActual-10<bz<disVer+ringActual+10):
		result=1
	else:
		result=0
	print("Use {:.2f} seconds".format(time.time() - start))
	return decide(result,expect),(bx,disHor,bz),ringXYZ

def decide(result,expect):
	if(expect==result):
		return 1
	else:
		return 0

if __name__ == '__main__':
    showIt=True
    videoPath='leftNotIn5.avi'
    result,ballPos,ringPos=main(videoPath,1,showIt)
    print(result)

'''
	showIt=False
	success=0
	successIn=0
	fail=0
	InError=[]
	outError=[]
	for i in range(1,6):
		videoPath='/mnt/hgfs/Virtural Share doc/rc_data_5.24/double_eye_320/leftIn'+str(i)+'.avi'
		#success+=main(videoPath,1)
		#videoPath='/mnt/hgfs/Virtural Share doc/rc_data_5.24/double_eye_320/RightIn'+str(i)+'.avi'
		result=main(videoPath,1,showIt)
		success+=result
		if(result==0):
			InError.append(i)
	successIn=success
	fail=success
	for i in range(1,13):
		videoPath='/mnt/hgfs/Virtural Share doc/rc_data_5.24/double_eye_320/leftNotIn'+str(i)+'.avi'
		#success+=main(videoPath,0)
		#videoPath='/mnt/hgfs/Virtural Share doc/rc_data_5.24/double_eye_320/RightNotIn'+str(i)+'.avi'
		result=main(videoPath,0,showIt)
		success+=result
		if(result==0):
			outError.append(i)
	fail=success-fail
	print('Total Accuracy:{:.2f}'.format(100*success/(5.0+12.0)))
	print('Detect In Accuracy:{:.2f}'.format(100*successIn/(5.0)))
	print('Detect out Accuracy:{:.2f}'.format(100*fail/(12.0)))
	print('In Error video',InError,'Out Error video',outError)
'''
