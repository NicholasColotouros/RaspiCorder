#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

class Instrument:
  drums = 1
  guitar = 2
  bass = 3
  other = 4

  @staticmethod
  def instrumentName(num):
  	if num == 1:
  		return "drums"
  	elif num == 2:
  		return "guitar"
  	elif num == 3:
  		return "bass"
  	else:
  		return "other"


class InstrumentMenu:
	instrumentSelection = " Drums     Bass\n Guitar    Other"
	selected = 1
	delayTime = 0.5      # The time it takes to look for another button press

	def __init__(self):
		selected = Instrument.drums
		delayTime = 0.5

	def updateCursor(self, lcd):
		if self.selected == Instrument.drums:
			lcd.setCursor(0,0)
		elif self.selected == Instrument.guitar:
			lcd.setCursor(0,1)
		elif self.selected == Instrument.bass:
			lcd.setCursor(10,0)
		else:
			lcd.setCursor(10,1)

	def getInstrumentInput(self, lcd):
		lcd.clear()
		lcd.message(self.instrumentSelection)
		lcd.blink()

		while True:
			self.updateCursor(lcd)
			
			# Move left
			if lcd.buttonPressed(lcd.LEFT):
		    		if self.selected == Instrument.bass:
		    			self.selected = Instrument.drums
			    		sleep(self.delayTime)

			    	elif self.selected == Instrument.other:
			    		self.selected = Instrument.guitar
		    			sleep(self.delayTime)

		         
			# Move right
			elif lcd.buttonPressed(lcd.RIGHT):
		    		if self.selected == Instrument.drums:
		    			self.selected = Instrument.bass
			    		sleep(self.delayTime)

			    	elif self.selected == Instrument.guitar:
			    		self.selected = Instrument.other
		    			sleep(self.delayTime)
		    
			# Move up
			elif lcd.buttonPressed(lcd.UP):
				if self.selected == Instrument.guitar:
					self.selected = Instrument.drums
		        		sleep(self.delayTime)

		        	elif self.selected == Instrument.other:
		        		self.selected = Instrument.bass
			        	sleep(self.delayTime)

			# Move down
			elif lcd.buttonPressed(lcd.DOWN):
				if self.selected == Instrument.drums:
					self.selected = Instrument.guitar
			        	sleep(self.delayTime)

		        	elif self.selected == Instrument.bass:
		        		self.selected = Instrument.other
			        	sleep(self.delayTime)				

			# Select the current entry
			elif lcd.buttonPressed(lcd.SELECT):
		    		lcd.noBlink()
		    		return self.selected