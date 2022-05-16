
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

print("welcome to the variable step direction tester, have fun!")

while True:
    prom = input("say something (c or cc or q): ")
    
    if (prom != "c") and (prom != "cc") and (prom != "q"):
        print("invalid input")
        continue
    
    if prom == "q":
        print("cleaning up")
        GPIO.cleanup()
        print("gpio's cleaned")
        break

    ang = input("no. of steps: ")
   
    try:
        int(ang)
    except:
        print("that's not a number")
        continue
    
    if prom == "cc":
        print("Moving CCW")
        mymotortest.motor_go(True, "Full" , int(ang), .005, False, .04)
    if prom == "c":
        print("Moving CW")
        mymotortest.motor_go(False, "Full" , int(ang), .005, False, .04)
    

