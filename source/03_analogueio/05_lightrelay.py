# Copyright 2016 Nikhil Metrani
# Institute of Systems Science, National University of Singapore
#
# Switch relay on or off based on environmental light.
# Connections:
#    VCC:        2
#    Ground:     6
#    SDA:        3 (GPIO 2)
#    SCL:        5 (GPIO 3)
#

from IOBoard import *
from Relay import *
from Lcd import *
import time

def main():
    board = Board()
    relay = Relay()
    lcd = Lcd()

    while (1):
        light = int(board.light())
        lcd.display_string("Control: %d" % (board.control()), 1)
        lcd.display_string("Light: %d" % (light), 2)
        lcd.display_string("Temprature: %d" % (board.temperature()), 3)
        lcd.display_string("Custom: %d" % (board.custom()), 4)
        if light >= 175:
            relay.on(0)
        if light >= 200:
            relay.on(1)
        if light <= 125:
            relay.off(1)
        if light <= 50:
            relay.off(0)
        time.sleep(1)

if __name__ == "__main__":
    main()

