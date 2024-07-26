from flask import Flask, request, jsonify
from.helpful_methods import *


app = Flask(__name__)
omni_modules = []
@app.route('/')
def main():
    return jsonify("hello world")


@app.route('/omni_modules')
def get_omni_modules():
    L = []
    for port in omni_modules:
        L.append(omni_modules[port].name())
    return jsonify(L)


@app.route('/omni_modules/servo1/door1')
def toggle_door1():
    omni_modules['servo_door'].Door1()
    return "OK"

@app.route('/omni_modules/servo1/door2')
def toggle_door2():
    omni_modules['servo_door'].Door2()
    return "OK"

@app.route('/omni_modules/servo1/lock1')
def toggle_lock1():
    omni_modules['servo_door'].Lock1()
    return "OK"

@app.route('/omni_modules/servo1/lock2')
def toggle_lock2():
    omni_modules['servo_door'].Lock2()
    return "OK"


if __name__ == '__main__':
    ports = helpers.list_serial_ports()
    print("Available serial ports:", ports)
    
    print("Identifying omni modules...")
    print(omni_modules:=helpers.identify_omni_modules())


    app.run(host='0.0.0.0', port=1942)










