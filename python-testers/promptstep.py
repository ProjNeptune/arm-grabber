
from time import sleep
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

#define GPIO pins
#Prerequisites:
#ms1-22
#ms2-27
#ms3-17
#stp-21
#dir-20

GPIO_pins = (22, 27, 17) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 20       # Direction -> GPIO Pin
step = 21      # Step -> GPIO Pin

# Declare an named instance of class pass GPIO pins numbers
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")

while True:
    print("cc closes, c opens")
    prom = input("say something you nerd (c or cc or q): ")
    if prom == "c":
        print("Moving Clockwise")
        mymotortest.motor_go(True, "Full" , 60, .005, False, .04)
    if prom == "cc":
        print("Moving Anti-Clockwise")
        mymotortest.motor_go(False, "Full" , 60, .005, False, .04)
    if prom == "q":
        print("cleaning up")
        GPIO.cleanup()
        print("gpio's cleaned you little troll")
        break

