# Copyright 2016 Nikhil Metrani
# Institute of Systems Science, National University of Singapore
#
# Relay class - enables interaction with relay switches
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

class Relay:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.pinList = [22,23,24,25]

    def switch(self, lamp, state):
        pin = self.pinList[lamp]
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, (GPIO.HIGH if state == 0 else GPIO.LOW))
        print "Relay %s switched %s" % (lamp, ("off" if state == 0 else "on"))

    def on(self, lamp):
        pin = self.pinList[lamp]
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        print "Relay %s switched %s" % (lamp, "on")

    def off(self, lamp):
        pin = self.pinList[lamp]
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        print "Relay %s switched %s" % (lamp, "off")
