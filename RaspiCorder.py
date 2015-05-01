#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

#Initialization of the plate
lcd = Adafruit_CharLCDPlate.Adafruit_CharLCDPlate()
lcd.begin(16,2)
lcd.clear()
lcd.message("  Introducing\n   RaspiCalc")
sleep(2)
lcd.clear()