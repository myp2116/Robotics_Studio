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
    servoR102 = LX16A(102)
    servoR103 = LX16A(103)
    servoR104 = LX16A(104)

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

#Homing Code
#Home ALL servos
L1_home = 135 #Degrees
L2_home = 127.5 #Degrees
L3_home = 135 #Degrees
L4_home = 127.5 #Degrees

#R101_home = 
#R102_home =
#R103_home =
#R104_home =
print(servoR101.get_physical_angle())
print(servoR102.get_physical_angle())
print(servoR103.get_physical_angle())
print(servoR104.get_physical_angle())

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
