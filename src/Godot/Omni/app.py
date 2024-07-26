from flask import Flask, request, jsonify
import flask
import requests
import cv2
import threading

app = Flask(__name__)
URL = "http://192.168.1.244"
cap = cv2.VideoCapture(URL + ":81/stream")
frame = None

frame_lock = threading.Lock()

@app.route('/')
def get_users():
    return jsonify({"users": ["John", "Jane", "Doe"]})

@app.route('/recognize', methods=['POST'])
def recognize():
    return f"{request.args}"

@app.route('/test')
def test():
    return jsonify({"test": "test"})



def start_capture():
    global frame
    while True:
        success, frame_buffer = cap.read()
        if success:
            with frame_lock:
                frame = frame_buffer



@app.route('/video')
def vid():
    print("accessed")
    buffer = cv2.imencode('.jpg', frame)[1].tobytes()
    return flask.Response(buffer, mimetype='img/jpeg')




if __name__ == "__main__":
    thread1 = threading.Thread(target=start_capture, daemon=True)
    thread1.start()
    app.run(host="0.0.0.0", port=2157)
