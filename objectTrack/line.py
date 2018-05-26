from  matplotlib import pyplot as plt
import  numpy as np
from mpl_toolkits.mplot3d import Axes3D

def drawGraph(point):
    fig = plt.figure()
    ax = Axes3D(fig)

    #列出实验数据
    
    plt.xlabel("X")
    plt.ylabel("Y")
    #在图中显示各点的位置
    for i in range(0,len(point)):

        x1i=point[i][0]
        x2i=point[i][1]
        yi=point[i][2]
        ax.scatter(x1i, x2i, yi, color="red")
        #show_point = "No."+str(i)+" ["+ str(x1i) +","+ str(x2i)+","+str(yi) + "]"
        show_point = "No."+str(i)
        ax.text(x1i,x2i,yi,show_point)
    
    #plt.show()
