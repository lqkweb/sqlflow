# coding:utf-8
from flask import Flask, render_template, request, jsonify
from urllib.parse import unquote
from dsl.lexer import lexer
from dsl.parser import parser
from session.baseclass import PysparkPro
from execute.main import execute_main
import os

app = Flask(__name__)
app.secret_key = 'secret_key'
# 下载apache spark, 指定解压目录，下载地址：http://spark.apache.org/downloads.html
os.environ['SPARK_HOME'] = '/Users/leiqiankun/spark-2.4.0'

spark = PysparkPro().sc
datadir = os.path.abspath(os.path.join(os.getcwd(), "..")) + "/data/"


@app.route('/')
def index():
    '''
    :return:
    '''
    return render_template('index.html')


@app.route('/sql')
def sql():
    '''
    运行单条sql
    :return:
    '''
    return render_template('sql.html')


@app.route('/script')
def script():
    '''
    运行脚本
    :return:
    '''
    return render_template('script.html')


@app.route('/udf')
def udf():
    '''
    注册udf函数
    :return:
    '''
    return render_template('udf.html')


@app.route('/runsql', methods=["POST", "GET"])
def runsql():
    sql = request.args.get("data", "")
    if sql:
        try:
            datatem = spark.sql(sql.replace(";", ""))
            data = datatem.toJSON().collect()
        except Exception as e:
            print(str(e))
            x = jsonify(list(str({"data": str(e)})))
            return x
        return jsonify(list(str({"data": data})))
    else:
        return jsonify(list(str({"data": "Invalid Input"})))


@app.route('/runscript', methods=["POST", "GET"])
def runscript():
    script = request.args.get("data", "")
    if script:
        cur = unquote(script)
        result = parser.parse(cur, lexer=lexer)
        data = execute_main(result, lexer, spark, datadir)
        print(data)
        return jsonify(data)
    else:
        return jsonify(list(str({"data": "Invalid Input"})))


if __name__ == '__main__':
    app.run()
