# Copyright 2016 Nikhil Metrani
# Institute of Systems Science, National University of Singapore
# Interaction with motion sensor
# Event based GPIO.
# Sensor class
# Connections:
#    VCC:        2
#    Ground:     6
#    Out:        11 (GPIO 17)

import RPi.GPIO as GPIO
import time
import sys

class Sensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.IN)

    def getState(self):
        return GPIO.input(self.pin)

    def waitForEdge(self, event):
        GPIO.wair_for_edge(self.pin, event)

    def onStateChange(self, channel):
        sys.exit("onStateChange() should be overriden")

    def setEvent(self, event):
        GPIO.add_event_detect(self.pin, event, callback=self.onStateChange)
