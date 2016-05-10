# Copyright 2016 Nikhil Metrani

# Interaction with a motion sensor
# Instead of polling the state of GPIO every second,
# here we used edge detection.
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

    def waitForEdge(self, event):
        GPIO.wait_for_edge(self.pin, event)

def main():
    sensor = Sensor(17)
    while True:
        sensor.waitForEdge(GPIO.RISING);
        print "Sensor is %d" % (sensor.getState())
        sensor.waitForEdge(GPIO.FALLING);
        print "Sensor is %d" % (sensor.getState())

if __name__ == "__main__":
    main()
