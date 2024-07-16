import serial.tools.list_ports
from pyfirmata import Arduino, util
import time



def serial_read(port):
    with serial.Serial(port, 9600) as omni_mod:
        response = omni_mod.readline().decode().strip()
        return response


def serial_post(port, message):
    with serial.Serial(port, 9600) as omni_mod:
        omni_mod.write(message)
        omni_mod.flush()
        time.sleep(0.05)
        return serial_read(port)

def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = [port.device for port in ports]
    return available_ports

def identify_omni_modules():
    ports = list_serial_ports()
    arduino_boards:list = []
    omni_boards:list = []
    for port in ports:
        try:
            if serial_post(port, "omni?") == "yes":
                omni_boards.append(port)
        except:
            pass
    return omni_boards


