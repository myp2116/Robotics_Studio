#Key Framing Script
from math import sin, cos
from lx16a import *
import time

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
    #servoR101.set_angle_limits(129, 161)
    servoR102 = LX16A(102)
    #servoR102.set_angle_limits(120, 137)
    servoR103 = LX16A(103)
    #servoR103.set_angle_limits(129, 161)
    servoR104 = LX16A(104)
    #servoR104.set_angle_limits(120, 137)

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

#Key Frame Operations

#Key Frame Function
def keyframe(m1,m2,n):
    """Keyframe Function for motor characterization"""
    #m1 defines motor 1 
    #m2 defines motor 2
    #n defines total number of keyframe points
    #loc defines the location of the leg being tested (FL, BL, FR, BR)

    #Disable torque to enable keyframe
    m1.disable_torque()
    m2.disable_torque()
    #Indicate Motors are prepared for keyframing
    m1.led_power_on()
    m2.led_power_on()
    motor_A = []
    motor_B = []

    for i in range(n):

        input("Position the leg to the keyframe position, Press Enter to record its angles.")
        motor_A += [i,m1.get_physical_angle()]
        motor_B += [i,m1.get_physical_angle()]

    #reenable torque in the motors
    m1.enable_torque()
    m2.enable_torque()
    print([motor_A])
    print([motor_B])
    return motor_A, motor_B

#Servo 1 & 2 Key Framing (FRONT LEFT LEG)
keyframe(servoL1,servoL2,5)
