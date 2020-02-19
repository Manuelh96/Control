from control import *

class IControl(control):

    def __init__(self, kp):
        self.kp = kp
        self.temp_xe = 0

    def get_xa(self, xe):
        self.temp_xe = self.temp_xe + xe
        xa = self.kp * self.temp_xe * 0.01
        return xa
