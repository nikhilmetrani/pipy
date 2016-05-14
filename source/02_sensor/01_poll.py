# Copyright 2016 Nikhil Metrani
# Institute of Systems Science, National University of Singapore
# Interacting with a motion sensor
# Let's poll the sensor output every second.
# Connections:
#    VCC:        2
#    Ground:     6
#    Out:        11 (GPIO 17)

import RPi.GPIO as GPIO
import time

class Sensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.IN)
    def getState(self):
        return GPIO.input(self.pin)

def main():
    sensor = Sensor(17) #GPIO pin number 11
    state = sensor.getState()
    while True:
        time.sleep(1) #wait for a second
        r = sensor.getState()
        if (r != state):
            state = r
            print "%s: status is %d" %(time.asctime(), state)

if __name__ == "__main__":
    main()

