# 物体跟踪与识别
**RoboCon 视觉组的库**
&emsp;本次比赛的任务内容在于实现对物体的**位置**以及**颜色**的识别，识别的对象为**绣球**以及**圆环**。

**目录**
 * [_1.流程及要求_](#1)
 * [_2.所需相关应用_](#2)
 * [_3.安装包_](#3)
 * [_4.相关文献资料_](#4)
<span id="1"></span>
## 1.流程及要求：
#### 1.搜集数据
 * 需要大量的**绣球**以及**圆环**的图片数据
#### 2.数据预处理
 * 利用**opencv**对数据进行预处理
 * 尽量**减少**深度学习模型学习**负担**
 * **保留**图片的拍摄**顺序**
#### 3.模型搭建
 * 避免过大**计算量**造成**内存**耗尽
 * 阅读最新**论文**文献，参考已有的**框架**
#### 4.测试模型效果
 * **快速计算**出结果
 * 检测的**精准度高**
<span id="2"></span>
## 2.所需相关应用
 *  **关键软件**
	 * [**Anaconda**](https://www.anaconda.com/download/)  : 主要用于管理安装包
	 * [**Git**](https://www.anaconda.com/download/) : 配合github，管理项目
	 * Jupyter notebook: 用于即时代码运行显示、文档记录以及图表展示
 *  **辅助软件**
	 * [**Lantern**](https://www.anaconda.com/download/) : 翻墙软件
	 * Spyder : 可选的代码运行环境，和Jupyter notebook 类似，能够搜索各种数据分析包的参考文档
<span id="3"></span>
## 3.安装包
**使用Anaconda创建一个环境后安装以下安装包**
 * Python 3: 主要的编程语言
 * Jupyter notebook: 编程环境
 * Numpy: 数据处理的基础包
 * Tensorflow: 深度学习框架
 * Matplotlib: 数据图表库
 * Scipy: 基于Numpy的进一步拓展包
 * Scikit-learn: 机器学习库(基于Numpy、Scipy、matplotlib
 * Keras: 基于tensorflow的深度学习框架

<span id="4"></span>
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
