from pyspark.sql import SparkSession, HiveContext
from pyspark import SparkContext,SparkConf
import os


class PysparkPro():
    pysparkpro = None

    # def __init__(self):
    #     super(PysparkPro, self).__init__()
    #     sparkConf = SparkConf().setAppName(value="testspark").setMaster("local[2]")
    #     sc = SparkContext(conf=sparkConf)
    #     self.pysparkpro = HiveContext(sparkContext=sc)

    def __init__(self):
        os.environ['SPARK_HOME'] = '/Users/leiqiankun/spark-2.4.0'
        super(PysparkPro, self).__init__()
        self.pysparkpro = SparkSession \
            .builder \
            .appName("pysparkpro") \
            .config("spark.some.config.option", "some-value") \
            .getOrCreate()
