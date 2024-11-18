from math import sin, cos
from lx16a import *
import time
import numpy as np

#Identify USB comm port (use USB 3.0 (blue one) towards the bottom of the pi)
LX16A.initialize("/dev/ttyUSB0")

#Boot Test Routine - Servo Connection
try:
    #Left Side Servos
    servoL1 = LX16A(1)
    servoL1.set_angle_limits(0, 240)
    servoL2 = LX16A(2)
    servoL2.set_angle_limits(0, 240)
    servoL3 = LX16A(3)
    servoL3.set_angle_limits(0, 240)
    servoL4 = LX16A(4)
    servoL4.set_angle_limits(0, 240)
    
    #Right Side Servos
    servoR101 = LX16A(101)
    servoR101.set_angle_limits(0, 240)
    servoR102 = LX16A(102)
    servoR102.set_angle_limits(0, 240)
    servoR103 = LX16A(103)
    servoR103.set_angle_limits(0, 240)
    servoR104 = LX16A(104)
    servoR104.set_angle_limits(0, 240)

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

#Homing Code
#Home ALL servos
#L1_home = 145 #Degrees
#L2_home = 128.5 #Degrees
#L3_home = 145 #Degrees
#L4_home = 128.5 #Degrees

#R101_home = 145 #Degrees
#R102_home = 128.5 #Degrees
#R103_home = 145 #Degrees
#R104_home = 128.5 #Degrees

#servoL1.move(L1_home)
#servoL2.move(L2_home)
#servoL3.move(L3_home)
#servoL4.move(L4_home)

#time.sleep(1)

#servoR101.move(R101_home)
#servoR102.move(R102_home)
#servoR103.move(R103_home)
#servoR104.move(R104_home)

#time.sleep(1)
punisher_mode = int(input("Type in desired robot mode: (1) - Pushups, (2) - Simple, (3) - Keyframe, (4) - Simulated, (5) - Optimized simulated"))

t = 0

#Option 3 - Keyframe Mode
if punisher_mode == 3: #keyframe mode
    while True:
        #Front left side leg
        servoL1.move(160.608 + (-9.747) * cos(2*np.pi * 1 * t / 3) + (-12.668) * sin(2*np.pi * 1 * t / 3) + (8.499) * cos(2*np.pi * 2 * t / 3) + (5.798) * sin(2*np.pi * 2 * t / 3))
        servoL2.move(134.880 + (-9.385) * cos(2*np.pi * 1 * t / 3) + (-17.220) * sin(2*np.pi * 1 * t / 3) + (11.545) * cos(2*np.pi * 2 * t / 3) + (3.363) * sin(2*np.pi * 2 * t / 3))
    
        #Back left side leg
        servoL3.move(173.712 + (-5.065) * cos(2*np.pi * 1 * t / 3) + (-8.396) * sin(2*np.pi * 1 * t / 3) + (6.313) * cos(2*np.pi * 2 * t / 3) + (0.110) * sin(2*np.pi * 2 * t / 3))
        servoL4.move(135.168 + (-5.968) * cos(2*np.pi * 1 * t / 3) + (-15.865) * sin(2*np.pi * 1 * t / 3) + (10.240) * cos(2*np.pi * 2 * t / 3) + (1.172) * sin(2*np.pi * 2 * t / 3))

        #Front right Side Leg
        servoR101.move(143.232 + (8.409) * cos(2*np.pi * 1 * t / 3) + (9.013) * sin(2*np.pi * 1 * t / 3) + (-8.121) * cos(2*np.pi * 2 * t / 3) + (0.524) * sin(2*np.pi * 2 * t / 3))
        servoR102.move(134.304 + (8.877) * cos(2*np.pi * 1 * t / 3) + (17.702) * sin(2*np.pi * 1 * t / 3) + (-13.341) * cos(2*np.pi * 2 * t / 3) + (1.982) * sin(2*np.pi * 2 * t / 3))

        #Back Right Side leg
        servoR103.move(106.944 + (6.412) * cos(2*np.pi * 1 * t / 3) + (12.383) * sin(2*np.pi * 1 * t / 3) + (-7.756) * cos(2*np.pi * 2 * t / 3) + (-3.703) * sin(2*np.pi * 2 * t / 3))
        servoR104.move(110.016 + (2.062) * cos(2*np.pi * 1 * t / 3) + (20.960) * sin(2*np.pi * 1 * t / 3) + (-11.998) * cos(2*np.pi * 2 * t / 3) + (0.589) * sin(2*np.pi * 2 * t / 3))
    
        time.sleep(0.05)
        t += 0.1
else:
    exit
