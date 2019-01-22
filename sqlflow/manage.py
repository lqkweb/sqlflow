# coding:utf-8
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
from urllib.parse import unquote
from dsl.lexer import lexer
from dsl.parser import parser
from session.abstract_class import PysparkPro
from execute.main import execute_main

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['JSON_AS_ASCII'] = False
socketio = SocketIO(app)
spark = PysparkPro().pysparkpro


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/demo')
def demo():
    return render_template('demo.html')


@socketio.on('client_event', namespace='/test')
def client_msg(msg):
    cur = unquote(msg["data"])
    result = parser.parse(cur, lexer=lexer)
    datat_response = execute_main(result, lexer, spark)
    emit('server_response', {'data': datat_response})


@socketio.on('connect_event')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1')
