#### 项目git：https://github.com/lqkweb/sqlflow
#### Blog：http://www.leiqiankun.com
#### 简书博客: https://www.jianshu.com/u/3fe4aab60ac4

开发交流QQ群: 941879291

# SQLflow (python3.6)
SQLflow based on python development, support to Spark, as the underlying distributed computing engine, through a set of unified configuration file to complete the batch, flow calculation, the Rest service development.
##### 2019-03-26 更新后台路由,前端抽取base模板并更新使用ajax方式执行sql语句
主页：
<div align="center">
<a href="https://buglib.tech/" target="_blank">
<img src="https://upload-images.jianshu.io/upload_images/11023671-f9f8887c69961f55.png" alt="SQLflow Logo" width="500px"></img>
</a>
</div>
结果页：
<div align="center">
<a href="https://buglib.tech/" target="_blank">
<img src="https://upload-images.jianshu.io/upload_images/11023671-b4d8905fda2ebe67.png" alt="SQLflow Logo" width="500px"></img>
</a>
</div>

# 目标
SQLflow 基于python开发, 支持通过写sql的方式操作分布式集群, 运行spark, 机器学习, 深度学习, 分布式爬虫, 数据可视化。

# Build

python3.6

git clone https://github.com/lqkweb/sqlflow.git

pip install -r requirements.txt

python manage.py

主页：http://127.0.0.1:5000
脚本页面：http://127.0.0.1:5000/script
单sql页面：http://127.0.0.1:5000/sql 

【注意：1、下载apache spark文件配置manage.py中的SPARK_HOME路径。2、data.csv是放到sqlflow/data目录中】

# Usage [sparksql doc:https://spark.apache.org/docs/latest/api/sql/index.html]

在脚本执行页面：http://127.0.0.1:5000/script  输入 select * from A limit 3; 或者 select * from A limit 3 as B; 生成临时表A或者B

生成临时表A数据:

select * from A limit 3;

生成临时表B数据:

select * from A limit 3 as B;

打开单sql执行页面：http://127.0.0.1:5000/sql, 直接就可以用spark sql语法操作数据表A和数据表B了:

desc A

select * from A limit 2

select * from B limit 2

as B 相当于创建了一个 B 临时表。

一个简单的sql操作spark集群的demo,是不是很简单。

### [还有更多sql版黑科技，sql版scikitlearn, sqlspider, sqlcharts, sqlkeras深度学习平台正在内测中！]

### * 正在新增sql版机器学习算法功能, 谢谢支持。 *
### * 正在新增sql版爬虫功能, 谢谢支持。 *
### * 正在新增sql版数据可视化功能, 谢谢支持。 *
### * 正在新增sql版keras深度学习功能, 谢谢支持。 *


# 记得给个star鼓励一下！Thanks♪(･ω･)ﾉ

----------
[![HitCount](http://hits.dwyl.io/lqkweb/sqlflow.svg)](http://hits.dwyl.io/lqkweb/sqlflow)