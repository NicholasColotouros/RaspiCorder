#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from RaspiCorder import *

# Initialization of the plate
lcd = Adafruit_CharLCDPlate.Adafruit_CharLCDPlate()
lcd.begin(16,2)
lcd.clear()
lcd.message("  Introducing\n  RaspiCorder")
sleep(2)
lcd.clear()

# Definition of utility functions
def instrumentConfirm():
	instmenu = InstrumentMenu.InstrumentMenu()
	instSelection = instmenu.InstrumentConfirm(lcd)
	lcd.clear()
	return instSelection

def RecConfirm(instName):
	recmenu = RecordingMenu.RecordingMenu(lcd, instName)
	recSelect = recmenu.getInput()
	lcd.clear()
	return recSelect

# Menu logic
while True:
	inst = instrumentInput()
	instName = Instrument.name(inst)

	beginRecording = RecConfirm(instName)

	if not beginRecording:
		continue

	# TODO: begin recording

