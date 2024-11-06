from math import sin, cos
from lx16a import *
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
    servoL4.set_angle_limits(120, 137)
    
    #Right Side Servos
    servoR101 = LX16A(101)
    servoR101.set_angle_limits(129, 161)
    servoR102 = LX16A(102)
    servoR102.set_angle_limits(120, 137)
    servoR103 = LX16A(103)
    servoR103.set_angle_limits(129, 161)
    servoR104 = LX16A(104)
    servoR104.set_angle_limits(120, 137)

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

#Homing Code
#Home ALL servos
L1_home = 145 #Degrees
L2_home = 128.5 #Degrees
L3_home = 145 #Degrees
L4_home = 128.5 #Degrees

R101_home = 145
R102_home = 128.5
R103_home = 145
R104_home = 128.5

servoL1.move(L1_home)
servoL2.move(L2_home)
servoL3.move(L3_home)
servoL4.move(L4_home)

servoR101.move(R101_home)
servoR102.move(R102_home)
servoR103.move(R103_home)
servoR104.move(R104_home)

t = 0
while True:
    #Front left side leg
    servoL1.move(sin(t) * 15 + 145)
    servoL2.move(sin(t) * 8.5 + 128.5)
    
    #Back left side leg
    servoL3.move(sin(t) * 15 + 145)
    servoL4.move(sin(t) * 8.5 + 128.5)

    #Front right Side Leg
    #servoR101.move(cos(t) * 15 + 145)
    #servoR102.move(cos(t) * 8.5 + 128.5)
    #Back Right Side leg
    #servoR103.move(cos(t) * 15 + 145)
    #servoR104.move(cos(t) * 8.5 + 128.5)
    time.sleep(0.05)
    t += 0.1
