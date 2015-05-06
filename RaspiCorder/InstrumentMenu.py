#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

class Instrument:
  drums = 1
  guitar = 2
  bass = 3
  other = 4

class InstrumentMenu():
	instrumentSelection = "Drums Bass\nGuitar Other"
	selected = 1
	delayTime = 0.5      # The time it takes to look for another button press

	def __init__(self):
		selected = 1
		delayTime = 0.5

	def getInstrumentInput(self, lcd):
		lcd.clear()
		lcd.message(instrumentSelection)
		lcd.blink()

	"""	while True:
		    # Move left
		    if lcd.buttonPressed(lcd.LEFT):
		    	if self.selected = Instrument.bass:
		    		self.selected = Instrument.drums
		    		sleep(delayTime)

		    	elif self.selected = Instrument.other:
		    		self.selected = Instrument.guitar
		    		sleep(delayTime)

		         
		    # Move right
		    elif lcd.buttonPressed(lcd.RIGHT):
		    	if self.selected = Instrument.drums:
		    		self.selected = Instrument.guitar
		    		sleep(delayTime)

		    	elif self.selected = selected.guitar:
		    		self.selected = Instrument.other
		    		sleep(delayTime)
		    
		    # Move up
		    elif lcd.buttonPressed(lcd.UP):
		        sleep(delayTime)

		    # Move down
		    elif lcd.buttonPressed(lcd.DOWN):
		    	sleep(delayTime)

		    # Select the current entry
		    elif lcd.buttonPressed(lcd.SELECT):
		    	lcd.blink()
		    	return selected"""