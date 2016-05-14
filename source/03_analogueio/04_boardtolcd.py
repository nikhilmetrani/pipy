# Copyright 2016 Nikhil Metrani
# Institute of Systems Science, National University of Singapore
#
# Displaying readout from analogur IO board on 4x20 LCD display
# Connections:
#    VCC:        2
#    Ground:     6
#    SDA:        3 (GPIO 2)
#    SCL:        5 (GPIO 3)
#

from IOBoard import *
from Lcd import *


def main():
    board = Board()
    lcd = Lcd()
    while (1):
        lcd.clear()
        lcd.display_string("Control: %d" % (board.control()), 1)
        lcd.display_string("Light: %d" % (board.light()), 2)
        lcd.display_string("Temprature: %d" % (board.temperature()), 3)
        lcd.display_string("Custom: %d" % (board.custom()), 4)
        time.sleep(1)
