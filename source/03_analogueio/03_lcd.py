# Copyright 2016 Nikhil Metrani
# Institute of Systems Science, National University of Singapore
#
# Displaying text on 4x20 LCD display
# Connections:
#    VCC:        2
#    Ground:     6
#    SDA:        3 (GPIO 2)
#    SCL:        5 (GPIO 3)
#
# Usage:
#     Parameter 1: Text to display on line 1
#     Parameter 2: Text to display on line 2
#     Parameter 3: Text to display on line 3
#     Parameter 4: Text to display on line 4
#

import sys
from Lcd import *

def main():
    lcd = Lcd()
    lcd.clear()
    for i in range(1,len(sys.argv)):
        lcd.display_string(sys.argv[i], i)

if __name__ == "__main__":
    main()