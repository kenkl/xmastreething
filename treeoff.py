#!/usr/bin/env python3

from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
from subprocess import *
tree = LEDBoard(*range(2,28),pwm=True)

def treeoff():
    cmd = "kill `ps -ef |grep xmastree.py |grep python3|grep -v grep |awk {'print $2'}`"
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

def dothings():
    result = treeoff()
    # Just in case - lets sweep through all the leds and make sure they're off
    for led in tree:
        led.off()


if __name__ == '__main__':
    dothings()


