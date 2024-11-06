from math import sin, cos
from pylx16a.lx16a import *
import time

#Identify USB comm port (use USB 3.0 (blue one) towards the bottom of the pi)
LX16A.initialize("/dev/ttyUSB0")

#Boot Test Routine - Servo Connection
try:
    #Left Side Servos
    servoL1 = LX16A(1)
    servoL1.set_angle_limits(129, 161)
    servoL2 = LX16A(2)
    servoL2.set_angle_limits(120, 137)
    servoL3 = LX16A(3)
    servoL3.set_angle_limits(129, 161)
    servoL4 = LX16A(4)
    servoL3.set_angle_limits(120, 137)
    
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
L1_home = 135 #Degrees
L2_home = 127.5 #Degrees
L3_home = 135 #Degrees
L4_home = 127.5 #Degrees

#L101_home = 
#L102_home =
#L103_home =
#L104_home =

servoL1.move(L1_home)
servoL2.move(L2_home)
servoL3.move(L3_home)
servoL4.move(L4_home)

t = 0
while True:
    #Front left side leg
    servoL1.move(sin(t) * 15 + 145)
    servoL2.move(sin(t) * 8.5 + 128.5)
    
    #Back left side leg
    servoL3.move(sin(t) * 15 + 145)
    servoL4.move(sin(t) * 8.5 + 128.5)

    time.sleep(0.05)
    t += 0.1
