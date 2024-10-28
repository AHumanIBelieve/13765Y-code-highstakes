# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Description:  Code for team 13675Y MTS_CtrlAltDefeat                       #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import math

brain=Brain()

#drive code
def drive():
    while(True):
        brain.screen.print("brrr")
        brain.screen.next_row()


#initialisation function for driver control. while loops will be within the functions.
def init():
    Thread(drive)

init()