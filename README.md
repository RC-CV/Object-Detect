# Robocon 物体跟踪与识别
**Robocon 视觉组的库**
<br>
本次比赛的任务内容在于使用计算机视觉的图像识别，目标跟踪。
* 识别的内容:**位置**以及**颜色**
* 识别的对象:**绣球**以及**圆环**

**本周任务：细读siamFC论文，看完udacity的git和github以及Linux命令**
 * 1.细读siamFC论文
   * [_主页_](http://www.robots.ox.ac.uk/~luca/siamese-fc.html) 
   * [_论文_](https://arxiv.org/pdf/1606.09549.pdf) 
   * [_源代码_](https://github.com/bertinetto/siamese-fc) 
   * [_介绍视频_](https://www.youtube.com/watch?v=jZoUalMMZ_0) 
 * 2.看完Linux/git/github学习（Udacity中有课程）
 * 3.补充资料（公开课，浙江大学王蒙蒙关于目标跟踪的介绍）
   * [_公开课视频_](http://cvmart.net/community/article/detail/40)
   * [_知乎专栏_](https://zhuanlan.zhihu.com/visual-tracking)
   * [_推荐的入门论文1_](https://pdfs.semanticscholar.org/59e5/b451055963f5e2b16e10958f806edf2b196f.pdf)
   * [_推荐的入门论文2_](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Nam_Learning_Multi-Domain_Convolutional_CVPR_2016_paper.pdf)



**目录**
 * [_1.流程及要求_](#1流程及要求)
 * [_2.所需相关应用_](#2所需相关应用)
 * [_3.安装包_](#3安装包)
 * [_4.相关文献资料_](#4相关文献资料)
## 1.流程及要求
#### 1.搜集数据
 * 需要大量的**绣球**以及**圆环**的图片数据
#### 2.数据预处理
 * 利用**opencv**对数据进行预处理
 * 尽量**减少**深度学习模型学习**负担**
 * **保留**图片的拍摄**顺序**
#### 3.模型搭建
 * 避免过大**计算量**造成**内存**耗尽
 * 阅读最新**论文**文献，参考已有的**框架**
#### 4.训练模型
 * 可能会用到云计算（阿里云/腾讯云/floyd/AWS...）
#### 5.测试与评估模型效果
 * **实时**出结果
 * 检测的**精准度高**
#### 6.投放模型与调试
 * 与电控组合作调试
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
