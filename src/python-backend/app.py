from flask import Flask, request, jsonify
from.helpful_methods import *
import flask
import requests
import cv2
import threading

app = Flask(__name__)
URL = "http://192.168.31.18"
cap = cv2.VideoCapture(URL + ":81/stream")

frame = None

frame_lock = threading.Lock()



def start_capture():
    requests.get(URL + "/control?var=framesize&val={}".format(8))
    global frame
    while True:
            if cap.isOpened():
                success, frame_buffer = cap.read()
                if success:
                    with frame_lock:
                        frame = frame_buffer
                        print("frame acquired")





app = Flask(__name__)
omni_modules = []
@app.route('/')
def world():
    return jsonify("hello world")

@app.route('/video')
def vid():
    buffer = cv2.imencode('.jpg', frame)[1].tobytes()
    print("Got")
    return flask.Response(buffer, mimetype='img/jpeg')



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
    thread1 = threading.Thread(target=start_capture, daemon=True)
    thread1.start()


    app.run(host='0.0.0.0', port=1942)










