from pyspark.sql import SparkSession, HiveContext
from pyspark import SparkContext,SparkConf


class PysparkPro():
    pysparkpro = None

    # def __init__(self):
    #     super(PysparkPro, self).__init__()
    #     sparkConf = SparkConf().setAppName(value="testspark").setMaster("local[2]")
    #     sc = SparkContext(conf=sparkConf)
    #     self.pysparkpro = HiveContext(sparkContext=sc)

    def __init__(self):
        super(PysparkPro, self).__init__()
        self.pysparkpro = SparkSession \
            .builder \
            .appName("pysparkpro") \
            .config("spark.some.config.option", "some-value") \
            .getOrCreate()
