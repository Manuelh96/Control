from PControl import *
from IControl import *

print("P-Glied:")
pglied = PControl(2)
print(pglied.get_xa(4))

print(" ")
print("I-Glied:")
iglied = IControl(1)
print(iglied.get_xa(2))

print(" ")
print("D-Glied")