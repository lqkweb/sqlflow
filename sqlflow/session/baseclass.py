from pyspark.sql import SparkSession, HiveContext
from pyspark import SparkContext,SparkConf
import os


class PysparkPro():
    sc = None

    def __init__(self):
        super(PysparkPro, self).__init__()
        self.sc = SparkSession \
            .builder \
            .appName("pysparkpro") \
            .config("spark.some.config.option", "some-value") \
            .getOrCreate()
