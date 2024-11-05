from math import sin, cos
from pylx16a.lx16a import *
import time

#Identify USB comm port (use USB 3.0 (blue one) towards the bottom of the pi)
LX16A.initialize("/dev/tty0")

#Boot Test Routine - Servo Connection
try:
    #Left Side Servos
    servoL1 = LX16A(1)
    servoL1.set_angle_limits(140, 160)
    servoL2 = LX16A(2)
    #servoL2.set_angle_limits(125, 130)
    #servoL3 = LX16A(3)
    #servoL4 = LX16A(4)
    
    #Right Side Servos
    #servoR1 = LX16A(101)
    #servoR2 = LX16A(102)
    #servoR3 = LX16A(103)
    #servoR4 = LX16A(104)

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

#Homing Code
#Home ALL servos

t = 0
while True:
    #Front left leg
    servoL1.move(sin(t) * 20 + 140)
    #servoL2.move(sin(t) * 60 + 60)

    time.sleep(0.05)
    t += 0.1
