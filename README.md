# Robocon 物体跟踪与识别
**Robocon 视觉组的库**
<br>
本次比赛的任务内容在于使用计算机视觉的目标跟踪,目标是跟踪小球的坐标轨迹，判断球是否进环，如不进，算出偏差，传输参数以调整自动机器人角度方向。
* 识别的内容:**位置**以及**颜色**
* 识别的对象:**绣球**以及**圆环**

**本周任务：（在linux环境配置opencv和熟悉opencv,继续学习Python，查找相关跟踪算法）**
 * 1.配置opencv
   * [ubuntu16.04系统配置opencv](https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/) 
   
 * 2.学习opencv
   * [opencv官网教程](https://docs.opencv.org/master/d9/df8/tutorial_root.html) 
   
 * 3.查找相关跟踪算法
   * [类似demo学习](https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/)
   * [实战教程](https://www.pyimagesearch.com/)
   

**目录**
 * [_1.流程及要求_](#1流程及要求)
 * [_2.所需相关应用_](#2所需相关应用)
 * [_3.安装包_](#3安装包)
 * [_4.相关文献资料_](#4相关文献资料)
## 1.流程及要求 
#### 1.实现小球跟踪
 * 利用opencv+python,调用摄像头，参照其他代码完成本任务（检验标准：算法+效果）。
#### 2.编写参数输出代码
 * 需要和电控组合作沟通 
#### 3.部署至工控机
 * 这步容易完成，只需重走一遍自己电脑的配置流程。
#### 4.投放模型与调试
 * 把工控机投放机器人上，与电控组合作调试
 
 
 --------以下资料未改动------------- 
## 2.所需相关应用
 *  **关键软件**
	 * [**Anaconda**](https://www.anaconda.com/download/)  : 主要用于管理安装包
	 * [**Git**](https://git-scm.com/) : 配合github，管理项目
	 * Jupyter notebook: 用于即时代码运行显示、文档记录以及图表展示
 *  **辅助软件**
	 * [**Lantern**](https://getlantern.org/en_US/) : 翻墙软件
	 * Spyder : 可选的代码运行环境，和Jupyter notebook 类似，能够搜索各种数据分析包的参考文档
 	* [**Tensorflow**](http://www.tensorfly.cn/):google开源的深度学习框架
## 3.安装包
**使用Anaconda创建一个环境后安装以下安装包**
 * Python 3: 主要的编程语言
 * Jupyter notebook: 编程环境
 * Numpy: 数据处理的基础包
 * Tensorflow: 深度学习框架
 * Matplotlib: 数据图表库
 * Scipy: 基于Numpy的进一步拓展包
 * Scikit-learn: 机器学习库(基于Numpy、Scipy、matplotlib）
 * Keras: 基于tensorflow的深度学习框架
 * Pandas: python的数据分析库
## 4.相关文献资料

 * [Anaconda 下载地址](https://www.anaconda.com/download/) 
 * [Anaconda命令文档](https://conda.io/docs/using/index.html)
 * [深度学习-社区 (内涵丰富的学习资料)](https://www.commonlounge.com/community/9dcdd386cc28446695305db00d2de532)
 * [Tensorflow官网](https://www.tensorflow.org/)
 * [Numpy 文档](http://www.numpy.org/)
 * [Matplotlib 文档](http://matplotlib.org/users/pyplot_tutorial.html)
 * [Scikit-learn 文档](http://scikit-learn.org/stable/index.html)
 * [Pandas 文档](http://pandas.pydata.org/pandas-docs/stable/index.html)	
 * [Udacity 中国课程网址](https://cn.udacity.com/)
 * [斯坦福深度学习课程](http://study.163.com/course/introduction/1004697005.htm)
 * [深度学习的中文资源，教程推荐](http://mp.weixin.qq.com/s/op_bWAF5u2kGPJs8V1oR5g)
 * [从零开始用TensorFlow搭建卷积神经网络](http://mp.weixin.qq.com/s/VlvQmrS7Qi2qq6fTBXKTYw)
