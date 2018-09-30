##### 项目git：https://github.com/lqkweb/sqlflow

# SQLflow (python3+)
SQLflow based on python development, support to Spark, Flink, etc as the underlying distributed computing engine, through a set of unified configuration file to complete the batch, flow calculation, the Rest service development.

# 项目目标
SQLflow 基于python开发, 支持通过写sql的方式操作分布式集群, 运行spark, 机器学习, 深度学习, 分布式爬虫, 数据可视化。

# 安装python3环境, 执行项目

git clone https://github.com/lqkweb/sqlflow.git

pip install -r requirements.txt

【注sqlflow/sqlflow/execute/main.py 中的data.csv测试时需要修改成你电脑中的绝对路径,数据文件在sqlflow/data/中】

python manage.py

打开http://127.0.0.1:5000 就可以测试了。

# 项目测试

在http://127.0.0.1:5000输入框输入:

测试1:

select * from A limit 3;

测试2:

select * from A limit 3 as B;

新开一个 http://127.0.0.1:5000 网页, 直接就可以查询数据表B了:

select * from B limit 2;

as B 相当于创建了一个 B 临时表。

一个简单的sql操作spark集群的demo,是不是很简单。

### [还有更多sql版黑科技，sql版scikit-learn, sql版分布式爬虫, sql版数据可视化, sql版keras深度学习平台正在内测中！]

### * 正在新增sql版机器学习算法功能, 谢谢支持。 *
### * 正在新增sql版爬虫功能, 谢谢支持。 *
### * 正在新增sql版数据可视化功能, 谢谢支持。 *
### * 正在新增sql版keras深度学习功能, 谢谢支持。 *


##### 记得给个start鼓励一下！Thanks♪(･ω･)ﾉ