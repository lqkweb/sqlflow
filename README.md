##### 项目git：https://github.com/lqkweb/sqlflow

# SQLflow (python3.5)
SQLflow based on python development, support to Spark, Flink, etc as the underlying distributed computing engine, through a set of unified configuration file to complete the batch, flow calculation, the Rest service development.
##### 2019-01-22 更新界面,近期会规范一下代码,写一些注释并加入读写功能
主页：
<div align="center">
<a href="https://buglib.tech/" target="_blank">
<img src="https://upload-images.jianshu.io/upload_images/11023671-f9f8887c69961f55.png" alt="SQLflow Logo" width="500px"></img>
</a>
</div>
结果页：
<div align="center">
<a href="https://buglib.tech/" target="_blank">
<img src="https://upload-images.jianshu.io/upload_images/11023671-c87720c918357b4d.png" alt="SQLflow Logo" width="500px"></img>
</a>
</div>
# 目标
SQLflow 基于python开发, 支持通过写sql的方式操作分布式集群, 运行spark, 机器学习, 深度学习, 分布式爬虫, 数据可视化。

# 安装python3.5环境并测试

git clone https://github.com/lqkweb/sqlflow.git

pip install -r requirements.txt

python manage.py

打开http://127.0.0.1:5000 就可以测试了。

【注意：sqlflow/sqlflow/execute/main.py 中的data.csv测试时需要修改成你电脑中的绝对路径,数据文件在sqlflow/data/中】

# Demo

在http://127.0.0.1:5000输入框输入:

测试1:

select * from A limit 3;

测试2:

select * from A limit 3 as B;

新开一个 http://127.0.0.1:5000 网页, 直接就可以查询数据表B了:

select * from B limit 2;

as B 相当于创建了一个 B 临时表。

一个简单的sql操作spark集群的demo,是不是很简单。

### [还有更多sql版黑科技，sql版scikitlearn, sqlspider, sqlcharts, sqlkeras深度学习平台正在内测中！]

### * 正在新增sql版机器学习算法功能, 谢谢支持。 *
### * 正在新增sql版爬虫功能, 谢谢支持。 *
### * 正在新增sql版数据可视化功能, 谢谢支持。 *
### * 正在新增sql版keras深度学习功能, 谢谢支持。 *


# 记得给个start鼓励一下！Thanks♪(･ω･)ﾉ

赏给作者一杯咖啡, 提提神(To the author for a cup of coffee.)：
<div>
<a href="https://buglib.tech/" target="_blank">
<img src="http://www.kszixue.com/zb_users/upload/2018/08/201808151534340304580089.png" alt="SQLflow Logo" width="300px"></img>
</a>
</div>