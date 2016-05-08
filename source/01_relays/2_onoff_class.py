# Copyright 2016 Nikhil Metrani

# Switch relay state using a reusable class - Relay
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

def main():
    if len(sys.argv) > 2:
        [cmd,lamp,state] = sys.argv
        lamp = int(lamp)   # which lamp?
        state = int(state) # off/on?
        relay = Relay()
        relay.switch(lamp, state)
    else:
        print "Usage: %s <relay> <0/1>" % sys.argv[0]
 
if __name__ == "__main__":
    main()
