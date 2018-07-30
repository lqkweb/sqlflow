# SQLflow (python3+)
Sqlflow based on python development, support to Spark, Flink, etc as the underlying distributed computing engine, through a set of unified configuration file to complete the batch, flow calculation, the Rest service development.

# 项目目标
基于python开发, 支持通过写sql的方式,运行spark, 机器学习算法, 爬虫。

# 安装python3环境, 执行项目
git clone https://github.com/lqkweb/sqlflow.git
pip install -r requirements.txt
（sqlflow/sqlflow/execute/main.py 中的data.csv需要修改成你电脑中的绝对路径,数据文件在sqlflow/data/中）
python manage.py
打开http://127.0.0.1:5000 就可以测试了。

# 项目测试
在http://127.0.0.1:5000输入框输入:
测试1:
select * from A limit 3;
测试2:
select * from A limit 3 as B;
新开一个http://127.0.0.1:5000网页, 直接就可以查询数据表B了:
select * from B limit 2;
as B 相当于创建了一个B临时表。
是不是很简单。
后期加入sql操作机器学习算法, 谢谢支持。

##### 记得给个start鼓励一下！Thanks♪(･ω･)ﾉ