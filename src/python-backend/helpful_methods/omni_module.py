import serial
import time

class omni_module():
    module = None

    def post(self, command:str):
        self.module.write(f"{command}\n".encode('utf-8'))
        self.module.flush()
        time.sleep(0.1)
        response = self.module.readline().decode('utf-8').strip()
        return response
    def __init__(self, module):
        self.module = module

    def name(self):
        return self.post("type?")

    

class rasputin(omni_module):
    def __init__(self, port):
        super().__init__(port)
    
    