import scipy
import scipy.cluster.hierarchy as sch
from scipy.cluster.vq import vq,kmeans,whiten
import numpy as np
import matplotlib.pylab as plt
from  matplotlib import pyplot as plt2
from mpl_toolkits.mplot3d import Axes3D
import collections

def clustering(points,showIt):
	points2=points.copy()[:,:2]
	points2=whiten(points2)
	#1. 层次聚类
	#生成点与点之间的距离矩阵,这里用的欧氏距离:
	disMat = sch.distance.pdist(points2,'euclidean') 
	#进行层次聚类:
	Z=sch.linkage(disMat,method='single') 
	#将层级聚类结果以树状图表示出来并保存为plot_dendrogram.png
	P=sch.dendrogram(Z)
	#plt.savefig('./plot_dendrogram.png')
	#根据linkage matrix Z得到聚类结果:
	cluster= sch.fcluster(Z, t=2, criterion='distance') 

	print ("Original cluster by hierarchy clustering:\n",cluster)
	fig = plt2.figure()
	ax = Axes3D(fig)

	#列出实验数据

	plt2.xlabel("X")
	plt2.ylabel("Y")
	#在图中显示各点的位置
	for i in range(0,len(points)):

	    x1i=points[i][0]
	    x2i=points[i][1]
	    yi=points[i][2]
	    if(cluster[i]==1):
	    	col='red'
	    else:
	    	col='blue'
	    ax.scatter(x1i, x2i, yi, color=col)
	    #show_point = "No."+str(i)+" ["+ str(x1i) +","+ str(x2i)+","+str(yi) + "]"
	    show_point = "No."+str(i)
	    ax.text(x1i,x2i,yi,show_point)
	if(showIt):
		plt2.show()


	d = collections.Counter(cluster)
	maxD=0
	index=0
	# 瞬间出结果
	for k in d:
	    # k是lst中的每个元素
	    # d[k]是k在lst中出现的次数
	    if(d[k]>maxD):
	    	maxD=d[k]
	    	index=k
	print('index',index,'maxD',maxD)

	newPoint=[]
	for i in range(0,len(points)):
		if(cluster[i]==index):
			newPoint.append(points[i])

	return np.array(newPoint)