# coding:utf-8
from flask import Flask, render_template, request, jsonify
from urllib.parse import unquote
from dsl.lexer import lexer
from dsl.parser import parser
from session.baseclass import PysparkPro
from execute.main import execute_main
import os

app = Flask(__name__)
spark = PysparkPro().pysparkpro
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


@app.route('/run', methods=["POST", "GET"])
def run():
    msg = request.args.get("data", "")
    cur = unquote(msg)
    result = parser.parse(cur, lexer=lexer)
    data = execute_main(result, lexer, spark, datadir)
    print(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=5002)
