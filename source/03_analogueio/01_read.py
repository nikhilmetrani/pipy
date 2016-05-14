# Copyright 2016 Nikhil Metrani
# Institute of Systems Science, National University of Singapore
#
# Reading the values of Analogue IO device pins
# Connections:
#    VCC:        2
#    Ground:     6
#    SDA:        3 (GPIO 2)
#    SCL:        5 (GPIO 3)
#

from IOBoard import *

def main():
    board = Board()
    while (1):
        print "%s: control:%d light:%d temp:%d custom:%d" % (time.asctime(),
                               board.control(),
                               board.light(),
                               board.temperature(),
                               board.custom())
        time.sleep(1)

if __name__ == "__main__":
    main()
