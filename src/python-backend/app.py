from flask import Flask, request, jsonify
from.helpful_methods import *


app = Flask(__name__)
omni_modules = []
@app.route('/')
def main():
    return "Hello, world!"

@app.route('/omni_modules')
def get_omni_modules():
    L = []
    for port in omni_modules:
        L.append(omni_modules[port].name())
    return jsonify(L)




if __name__ == '__main__':
    ports = helpers.list_serial_ports()
    print("Available serial ports:", ports)
    
    print("Identifying omni modules...")
    print(omni_modules:=helpers.identify_omni_modules())


    app.run(host='0.0.0.0', port=1942)










