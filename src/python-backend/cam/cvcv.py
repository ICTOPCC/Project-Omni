import cv2
import numpy as np
import requests
import time
import queue
import threading
import matplotlib.pyplot as plt

 
 
 
 
URL = "http://192.168.31.165"
cap = cv2.VideoCapture(URL + ":81/stream")

if __name__ == '__main__':

    while True:
        if cap.isOpened():
            ret, frame = cap.read()
            
            # Encode the frame as PNG (lossless compression, better for quality)
            _, encoded_image = cv2.imencode('.png', frame)
            
            # Create and save the image file
            with open("~/Documents/GitHub/Project-Omni/src/python-backend/cam/frame.png", "wb") as f:
                f.write(encoded_image)

            im = frame

            key = cv2.waitKey(3)
            
            if key == 27:
                break


 
    cv2.destroyAllWindows()
    cap.release()