import serial.tools.list_ports
import time
from .omni_module import *

def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = [port.device for port in ports]
    return available_ports

def identify_omni_modules():
    ports = list_serial_ports()
    arduino_boards:list = []
    omni_boards:list = {}
    for port in ports:
        try:
            if 'ACM' in port:
                omni_mod = serial.Serial(port, 115200)
                omni_mod.write('omni?\n'.encode('utf-8'))
                omni_mod.flush()
                time.sleep(0.1)
                response = omni_mod.readline().decode('utf-8').strip()
                if response == 'YES':
                    omni_board = rasputin(omni_mod)
                    omni_boards[omni_board.name()] = omni_board
        except:
            print(port)
    return omni_boards


