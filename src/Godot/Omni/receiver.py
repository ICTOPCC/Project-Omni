import requests
import cv2

frame = None

cap = cv2.VideoCapture("http://192.168.1.3:8080/video")
while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)