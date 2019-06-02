
from flask import  Flask, request, jsonify
import sys, os, json
import logging, threading, time
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
from flask_cors import CORS
from core import Core


app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)
core = None

@app.route("/")
def monitor():
    return "Hello, World!"

@app.route('/register_new_platform', methods=['POST'])
def register_new_platform():
    global core
    data = request.args.get('platform_data')
    response = core.register_new_platform(data)
    return jsonify(response)

@app.route('/set_action_rules', methods=['POST'])
def set_action_rules():
    global core
    data = request.args.get('action_rules')
    response = core.set_action_rules(data)
    return jsonify(response)

@app.route('/register_new_user', methods=['POST'])
def register_new_user():
    global core
    data = request.args.get('user_name')
    response = core.register_new_user(data)
    return jsonify(response)

@app.route('/get_user_info_by_name', methods=['GET'])
def get_user_info_by_name():
    global core
    data = request.args.get('user_name')
    response = core.get_user_info_by_name(data)
    return jsonify(response)

@app.route('/get_platform_info', methods=['GET'])
def get_platform_info():
    global core
    data = request.args.get('platform_name')
    response = core.get_platform_info(data)
    return jsonify(response)

@app.route('/get_action_rules', methods=['GET'])
def get_action_rules():
    global core
    data = request.args.get('platform_name')
    response = core.get_action_rules(data)
    return jsonify(response)

@app.route('/new_action', methods=['POST'])
def new_action():
    global core
    data = request.args.get('action_data')
    response = core.new_action(data)
    return jsonify(response)

@app.route('/get_user_balance', methods=['GET'])
def get_user_balance():
    global core
    data = request.args.get('user_name')
    response = core.get_user_balance(data)
    return jsonify(response)

@app.route('/get_registered_actions', methods=['GET', 'HTTP', 'HTTPS'])
def get_registered_actions():
    global core
    response = core.get_registered_actions()
    return jsonify(response)



def start_server(host, port):
    app.run(host=host, port=port, threaded=True)

def main():
    global core
    core = Core()
    start_server("127.0.0.1", 3000)

if __name__ == '__main__':
    main()