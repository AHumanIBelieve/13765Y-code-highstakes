# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Description:  Code for team 13675Y MTS_CtrlAltDefeat                       #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import math

#misc stuff
brain=Brain()
controller = Controller()
#drivebase
right_drive_back = Motor(Ports.PORT1, True)
right_drive_front = Motor(Ports.PORT11)
left_drive_back = Motor(Ports.PORT10, True)
left_drive_front = Motor(Ports.PORT20)
left_drive_smart = MotorGroup(left_drive_back, left_drive_front)
right_drive_smart = MotorGroup(right_drive_back, right_drive_front)

#drive code
def drive():
    while(True):
        vals = getInput() # gets input as an array
        left_drive_smart.spin(vals[0]) # spins left side of the drivebase
        right_drive_smart.spin(vals[1]) # spins right side of the drivebase
        sleep(10, MSEC)

#process input from left stick
def getInput():
    vals = [controller.axis3.value(), controller.axis2.value()] #axis3 gets left input, axis2 gets right input
    for i in vals: # goes through the vals array, checks if -10<value<10, and if it is, sets it to 0
        if i > -10 and i<10:
            i=0
    return vals

#initialisation function for driver control. while loops will be within the functions.
def init():
    Thread(drive)

init()