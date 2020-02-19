from control import *

class PControl(control):

    def __init__(self, kp):
        self.kp = kp

    def get_xa(self, xe):
        xa = xe * self.kp
        return xa
