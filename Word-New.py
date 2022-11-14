#!/usr/bin/python
"""
WordClock.py
Author             :  Martin Coleman based on code from cyntech.co.uk & adafruit industries
Creation Date      :  09/11/2022

Free and open for all to use.  But put credit where credit is due.

OVERVIEW:-----------------------------------------------------------------------
Neopixel 8x8 panel required, display 'word' time with rainbow LEDs
"""

# Simple test for NeoPixels on Raspberry Pi
from time import sleep
from datetime import datetime
import board
import neopixel
import sys


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

# The number of NeoPixels
num_pixels = 64

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

#Define what combination of LEDs are required for each word

def mfive():
  pixels[16] = (colour)
  pixels[17] = (colour)
  pixels[18] = (colour)
  pixels[19] = (colour)

def mten():
  pixels[1] = (colour)
  pixels[3] = (colour)
  pixels[4] = (colour)

def quarter():
  pixels[8] = (colour)
  pixels[9] = (colour)
  pixels[10] = (colour)
  pixels[11] = (colour)
  pixels[12] = (colour)
  pixels[13] = (colour)
  pixels[14] = (colour)

def twenty():
  pixels[1] = (colour)
  pixels[2] = (colour)
  pixels[3] = (colour)
  pixels[4] = (colour)
  pixels[5] = (colour)
  pixels[6] = (colour)

def half():
  pixels[20] = (colour)
  pixels[21] = (colour)
  pixels[22] = (colour)
  pixels[23] = (colour)

def past():
  pixels[25] = (colour)
  pixels[26] = (colour)
  pixels[27] = (colour)
  pixels[28] = (colour)

def to():
  pixels[28] = (colour)
  pixels[29] = (colour)

def one():
  pixels[57] = (colour)
  pixels[60] = (colour)
  pixels[63] = (colour)

def two():
  pixels[48] = (colour)
  pixels[49] = (colour)
  pixels[57] = (colour)

def three():
  pixels[43] = (colour)
  pixels[44] = (colour)
  pixels[45] = (colour)
  pixels[46] = (colour)
  pixels[47] = (colour)

def four():
  pixels[56] = (colour)
  pixels[57] = (colour)
  pixels[58] = (colour)
  pixels[59] = (colour)

def five():
  pixels[32] = (colour)
  pixels[33] = (colour)
  pixels[34] = (colour)
  pixels[35] = (colour)

def six():
  pixels[40] = (colour)
  pixels[41] = (colour)
  pixels[42] = (colour)

def seven():
  pixels[40] = (colour)
  pixels[52] = (colour)
  pixels[53] = (colour)
  pixels[54] = (colour)
  pixels[55] = (colour)

def eight():
  pixels[35] = (colour)
  pixels[36] = (colour)
  pixels[37] = (colour)
  pixels[38] = (colour)
  pixels[39] = (colour)

def nine():
  pixels[60] = (colour)
  pixels[61] = (colour)
  pixels[62] = (colour)
  pixels[63] = (colour)

def ten():
  pixels[39] = (colour)
  pixels[47] = (colour)
  pixels[55] = (colour)

def eleven():
  pixels[50] = (colour)
  pixels[51] = (colour)
  pixels[52] = (colour)
  pixels[53] = (colour)
  pixels[54] = (colour)
  pixels[55] = (colour)

def twelve():
  pixels[48] = (colour)
  pixels[49] = (colour)
  pixels[50] = (colour)
  pixels[51] = (colour)
  pixels[53] = (colour)
  pixels[54] = (colour)

def update():
  pixels.show()

def clear():
  for i in range(0,num_pixels):
    pixels[i] = (0, 0, 0)

def wheel(pos):
    # Input a value 0 to 255 to get a colour value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

#Replacing looos
j = 0
#Keep track of the count direction
direction = 0

while True:
    try:
        time = datetime.now().time()
        hour,min,sec = str(time).split(":")
        hour = int(hour)
        min = int(min)

        #Clear the board for updates
        clear()

        colour = (wheel(j))

        #Logic replacing loops, cycle 255 and then back down to 0
        if j < 256 and direction == 0:
            j+=1
        if j >0 and direction == 1:
            j-=1
        if j == 255:
            direction = 1
        if j == 0:
            direction = 0

        # Work Out Minutes
        if 3 <= min <= 7:
            mfive()
            past()

        if 8 <= min <= 12:
            mten()
            past()

        if 13 <= min <= 17:
            quarter()
            past()

        if 18 <= min <= 22:
            twenty()
            past()

        if 23 <= min <= 27:
            twenty()
            mfive()
            past()

        if 28 <= min <= 32:
            half()
            past()

        if 33 <= min <= 37:
            twenty()
            mfive()
            to()

        if 38 <= min <= 42:
            twenty()
            to()

        if 43 <= min <= 47:
            quarter()
            to()

        if 48 <= min <= 52:
            mten()
            to()

        if 53 <= min <= 57:
            mfive()
            to()

        if min > 32:
            hour = hour + 1

        # Work Out Hours
        if hour == 1 or hour == 13:
            one()

        if hour == 2 or hour == 14:
            two()

        if hour == 3 or hour == 15:
            three()

        if hour == 4 or hour == 16:
            four()

        if hour == 5 or hour == 17:
            five()

        if hour == 6 or hour == 18:
            six()

        if hour == 7 or hour == 19:
            seven()

        if hour == 8 or hour == 20:
            eight()

        if hour == 9 or hour == 21:
            nine()

        if hour == 10 or hour == 22:
            ten()

        if hour == 11 or hour == 23:
            eleven()

        if hour == 12 or hour == 0 or hour == 24:
            twelve()

        update()
        sleep(0.1)

    except KeyboardInterrupt:
        clear()
        update()
        sys.exit()


