# Copyright 2016 Nikhil Metrani

# This code shows how to connect to a 4-channel relay board and switch relay state
# Connections:
#    VCC:        2
#    Ground:     6
#    Relay switches -
#        Switch 0:    15 (GPIO 22)
#        Switch 1:    16 (GPIO 23)
#        Switch 2:    18 (GPIO 24)
#        Switch 3:    22 (GPIO 25)

import RPi.GPIO as GPIO
import sys
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinList = [22,23,24,25] 
if len(sys.argv)>2:
    [cmd,lamp,state] = sys.argv
    lamp = int(lamp)   # which lamp?
    state = int(state) # off/on?
    GPIO.setup(pinList[lamp], GPIO.OUT)
    GPIO.output(pinList[lamp], (GPIO.HIGH if state == 0 else GPIO.LOW))
    print "Relay %s switched %s" % (lamp, ("off" if state == 0 else "on"))
else:
    print "Usage: %s <relay> <0/1>" % sys.argv[0]
