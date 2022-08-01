#### 开发交流QQ群: 941879291
# SQLflow (python3.6)

[![image](https://camo.githubusercontent.com/6ff64ec221e68a362bab8af56f39c1ab2cd46ce1/68747470733a2f2f696d672e736869656c64732e696f2f707970692f6c2f72657175657374732e737667)](https://github.com/kennethreitz/requests/blob/master/LICENSE)[![HitCount](https://camo.githubusercontent.com/46429a8e0eb6868a9c97e09a0e8e766d7c92e595/687474703a2f2f686974732e6477796c2e696f2f6c716b7765622f73716c666c6f772e737667)](http://hits.dwyl.io/lqkweb/sqlflow)

SQLflow based on python development, support to Spark, as the underlying distributed computing engine, through a set of unified configuration file to complete the batch, flow calculation, the Rest service development.

##### 2019-03-26 更新后台路由,前端抽取base模板并更新使用ajax方式执行sql语句

主页：

[![SQLflow Logo](https://camo.githubusercontent.com/82e4243ba08dfd91d81574a652e675d64f3f1bff/68747470733a2f2f75706c6f61642d696d616765732e6a69616e7368752e696f2f75706c6f61645f696d616765732f31313032333637312d663966383838376336393936316635352e706e67)](https://buglib.tech/)

结果页：

[![SQLflow Logo](https://camo.githubusercontent.com/913bbed059366bad0f9f3c72036498aa0f325751/68747470733a2f2f75706c6f61642d696d616765732e6a69616e7368752e696f2f75706c6f61645f696d616765732f31313032333637312d623464383930356664613265626536372e706e67)](https://buglib.tech/)

# SQLflow

SQLflow 基于python开发, 支持通过写sql的方式操作分布式集群, 数据处理, 机器学习、深度学习模型训练, 模型部署, 分布式爬虫, 数据可视化等。

# Build

python3.6

git clone https://github.com/lqkweb/sqlflow.git

pip install -r requirements.txt

python manage.py

主页：[http://127.0.0.1:5000](http://127.0.0.1:5000/) 脚本页面：http://127.0.0.1:5000/script 单sql页面：http://127.0.0.1:5000/sql

【注意：1、下载apache spark文件配置manage.py中的SPARK_HOME路径。2、data.csv是放到sqlflow/data目录中】

# Usage

在脚本执行页面：http://127.0.0.1:5000/script 输入 select * from A limit 3; 或者 select * from A limit 3 as B; 生成临时表A或者B

生成临时表A数据:

```
select * from A limit 3;
```

生成临时表B数据:

```
select * from A limit 3 as B;
```

打开单sql执行页面：http://127.0.0.1:5000/sql, 直接就可以用spark sql任意语法操作数据表A和数据表B了:

```
desc A
select * from A limit 2
select * from B limit 2
```

[注] "as B" 相当于创建了一个 B 临时表。

一个简单的sql操作spark集群的Demo,是不是很简单。

[附] sparksql doc: https://spark.apache.org/docs/latest/api/sql/index.html

### 还有更多sql版黑科技，sql版scikitlearn, sqlspider, sqlcharts, sqlkeras深度学习平台正在内测中！

### * 正在新增sql版机器学习算法功能, 谢谢支持。 *

### * 正在新增sql版爬虫功能, 谢谢支持。 *

### * 正在新增sql版数据可视化功能, 谢谢支持。 *

### * 正在新增sql版keras深度学习功能, 谢谢支持。 *

# 记得给个star鼓励一下！Thanks♪(･ω･)ﾉ



