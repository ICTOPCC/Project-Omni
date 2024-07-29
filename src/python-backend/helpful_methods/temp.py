import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200)

ser.write('omni?\n'.encode('utf-8'))
ser.flush()
time.sleep(0.1)
response = ser.readline().decode('utf-8').strip()
print(response)