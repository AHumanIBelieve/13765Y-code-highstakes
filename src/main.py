#----------------------------------------------------------------------------# 
#                                                                            # 
# Module:       main.py                                                      # 
# Description:  Code for team 13675Y MTS_CtrlAltDefeat                       # 
#                                                                            # 
#----------------------------------------------------------------------------# 

#  Library imports
from vex import *
import math

# misc stuff
brain=Brain()
controller = Controller()
# drivebase
right_drive_back = Motor(Ports.PORT10, True)
right_drive_front = Motor(Ports.PORT9)
left_drive_back = Motor(Ports.PORT1, True)
left_drive_front = Motor(Ports.PORT20)
left_drive_smart = MotorGroup(left_drive_back, left_drive_front)
right_drive_smart = MotorGroup(right_drive_back, right_drive_front)
# intake/lift
intake_motor = Motor(Ports.PORT18)
lift_motor = Motor(Ports.PORT5)

counter = 0

# DRIVE CODE
def drive():
    while(True):
        vals = getDriveInput() #  gets input as an array
        controller.screen.print(vals[0], " ", vals[1])
        left_drive_smart.spin(FORWARD,vals[0],PERCENT) #  spins left side of the drivebase
        right_drive_smart.spin(REVERSE, vals[1], PERCENT) #  spins right side of the drivebase
        sleep(10, MSEC)

# process input from sticks 
def getDriveInput():
    global counter
    brain.screen.set_cursor(0, 0)
    controller.screen.set_cursor(1,1)
    vals = [controller.axis3.value(), controller.axis2.value()] # axis3 gets left input, axis2 gets right input
    #brain.screen.print(counter, " controller vals: ", vals[0], ", ", vals[1])
    #controller.screen.print(counter, " vals: ", vals[0], ", ", vals[1])
    for i in vals: # goes through the vals array, checks if -10<value<10, and if it is, sets it to 0
        if i > -10 and i<10:
            i=0
        i = i/127*100
    counter = counter+1
    return vals

# INTAKE CODE
def intake():
    while(True):
        if(controller.buttonA.pressing()): #checks if button is pressed
            intake_motor.spin(FORWARD, 100, PERCENT) # sets it to full
        elif(controller.buttonX.pressing()):
            intake_motor.spin(FORWARD, -100, PERCENT) #
        else:
            intake_motor.set_velocity(0) # turns it off if button is not pressed
        sleep(10, MSEC)

# lift CODE
def lift():
    while(True):
        if(controller.buttonB.pressing()):
            lift_motor.spin(REVERSE,100, PERCENT)
        elif(controller.buttonY.pressing()):
            lift_motor.spin(FORWARD, 100, PERCENT)
        else:
            lift_motor.spin(FORWARD, 0, PERCENT)
        sleep(10, MSEC)

# initialisation function for driver control. while loops will be within the functions.
Thread(drive)
Thread(intake)
Thread(lift)