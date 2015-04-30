#!/usr/bin/python

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

int pos = 0

lcd = Adafruit_CharLCDPlate.Adafruit_CharLCDPlate()
lcd.begin(16,2)
lcd.clear()
lcd.message("  Introducing\n RaspiCorder")
sleep(2)
lcd.clear()

lcd.blink()
update()
