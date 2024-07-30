from flask import Flask, request, jsonify
from .helpful_methods import *
import flask
import cv2
import numpy as np

app = Flask(__name__)




app = Flask(__name__)
omni_modules = []
@app.route('/')
def world():
    return jsonify("hello world")

@app.route('/video')
def vid():
    with open('/home/gryff1n/Documents/GitHub/Project-Omni/src/python-backend/cam/frame.png', 'rb') as f:
        img = f.read()
    buffer = cv2.imencode('.jpg', cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_UNCHANGED))[1].tobytes()
    return flask.Response(buffer, mimetype='image/jpeg')



@app.route('/omni_modules')
def get_omni_modules():
    L = []
    for port in omni_modules:
        L.append(omni_modules[port].name())
    return jsonify(L)


@app.route('/omni_modules/servo1/door1')
def toggle_door1():
    resp = omni_modules['servo_door'].Door1()
    return jsonify(resp)

@app.route('/omni_modules/servo1/door2')
def toggle_door2():

    resp = omni_modules['servo_door'].Door2()
    return jsonify(resp)

@app.route('/omni_modules/servo1/lock1')
def toggle_lock1():

    resp = omni_modules['servo_door'].Lock1()
    return jsonify(resp)

@app.route('/omni_modules/servo1/lock2')
def toggle_lock2():

    resp = omni_modules['servo_door'].Lock2()
    return jsonify(resp)


if __name__ == '__main__':
    ports = helpers.list_serial_ports()
    print("Available serial ports:", ports)
    
    print("Identifying omni modules...")
    print(omni_modules:=helpers.identify_omni_modules())
    app.run(host='0.0.0.0', port=1942)










