#!/usr/bin/python

from Adafruit_I2C import Adafruit_I2C
from time import sleep

class RecordingMenu():
	menuText
	selected
	lcd

	def __init__(self, plcd, instrument):
		self.menuText = " START REC  " + instrument + "\nReselect instr"
		self.lcd = plcd
		self.selected = 0

	def InstrumentConfirm(self):
		lcd = self.lcd
		lcd.clear()
		lcd.message(menuText)
		lcd.blink()

		while True:
			lcd.setCursor(0, self.selected)

			if lcd.buttonPressed(lcd.UP):
				self.selected = 0

			elif lcd.buttonPressed(lcd.DOWN):
				self.selected = 1

			elif lcd.buttonPressed(lcd.SELECT):
				lcd.noBlink()
				if self.selected == 1:
					return False
				else:
					return True