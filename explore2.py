##Import public library python-RPi.GPIO
import RPi.GPIO as gpio
##Import public library python-time
import time
##Import public library python-sys
import sys
##Import local library python-sensors: see sensors.py
import sensors
##Import local library python-driveme: see driveme.py
import driveme
##Import public library python-random
import random

#Goal:
##1. Drive vechicle autonomously in "explore" mode.
##2. Check the distance before performing each action and print the result.
## ---sensors.distance() --- Return the distance from the sensor to the nearest object
## ---driveme.init() --- Initialise GPIO pins to drive as output
## ---driveme.forward(tf) --- Drive Foward
## ---driveme.reverse(tf) --- Drive in Reverse
## ---driveme.turn_left_fwd(tf) --- Turn left while moving forward
## ---driveme.turn_right_fwd(tf) --- Turn right while moving forward
## ---driveme.turn_left_rev(tf) --- Turn left while moving backward
## ---driveme.turn_right_rev(tf) --- Turn right while moving backward
## ---driveme.pivot_right(tf) --- Pivot clockwise (defined as from a 'birds eye view' with 12o'clock at the front of the vehicle (Pivot right)
## ---driveme.pivot_left(tf) --- Pivot counter clockwise (Pivot left)

#Assumptions: see driveme.py

##Call the function front_distance from the local python script sensors.py
sensors.front_distance()

##Define the function check_front to check the distance from the front sensor to the nearest object and respond
def check_front():
##Define the variable f_dist as the distance from the front sensor to the nearest object
    f_dist = sensors.front_distance()

##Instruct action: if an object is closer than 15 cm away, print "Too close, and the distance", and continue
    if f_dist < 15:
        print('Too close,', f_dist)
##Otherwise, print 'Front okay' and continue
    else:
        print('Front okay,', f_dist)

##Define the function autonomy
def autonomy():
##Set the time to run (for actions other than forward)
    tf = 1
##Introduce a variable, x, that will take on a sudorandom value to drive the vechicle in explore mode. x will take on values from 1-7
    x = random.randrange(0, 8)
##Set actions for the vechicle based on the value of x

##Drive forward for 5 seconds if x = 0
    if x == 0:
        check_front()
##Initialise GPIO pins (based on instructions defined in driveme.py)
        driveme.init()
##Drive forward for 5 seconds
        driveme.forward(5)

##Pivot left for tf seconds if x = 1
    elif x == 1:
        check_front()
        driveme.init()
        driveme.pivot_left(tf)

##Pivot right for tf seconds if x = 2
    elif x == 2:
        check_front()
        driveme.init()
        driveme.pivot_right(tf)

##Drive forward and to the left for tf seconds if x = 3
    elif x == 3:
        check_front()
        driveme.init()
        driveme.turn_left_fwd(tf)

##Drive forward and to the right for tf seconds if x = 4
    elif x == 4:
        check_front()
        driveme.init()
        driveme.turn_right_fwd(tf)

##Drive left and reverse for tf seconds if x = 5
    elif x == 5:
        check_front()
        driveme.init()
        driveme.turn_left_rev(tf)

##Drive right and reverse for tf seconds if x = 6
    elif x == 6:
        check_front()
        driveme.init()
        driveme.turn_right_rev(tf)

##Reverse for tf seconds if x = 7
    elif x == 7:
        check_front()
        driveme.init()
        driveme.reverse(tf)

##Run the function autonomy 10 times (generate 10 random iterations of x which will produce 10 movements at random)
for z in range(10):
    autonomy()



'''def check_front():
    driveme.init()
    dist = sensors.distance()

    if dist < 15:
        print('Too close,',dist)
        driveme.init()
        driveme.reverse(2)
        dist = sensors.distance()
        if dist < 15:
            print('Too close,', dist)
            driveme.init()
            driveme.pivot_left(3)
            driveme.init()
            driveme.reverse(2)
            dist = sensors.distance()
            if dist < 15:
                print('Too close, giving up', dist)
                sys.exit()

def autonomy():
    tf = 2
    x = random.randrange(0, 4)

    if x == 0:
        for y in range(30):
            check_front()
            driveme.init()
            driveme.forward(tf)

    elif x == 1:
        for y in range (30):
            check_front()
            driveme.init()
            driveme.pivot_left(tf)

    elif x == 2:
        for y in range (30):
            check_front()
            driveme.init()
            driveme.turn_right_fwd(tf)

    elif x == 3:
        for y in range (30):
            check_front()
            driveme.init()
            driveme.turn_left_fwd(tf)

for z in range(10):
    autonomy()'''
