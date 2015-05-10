#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

from RaspiCorder import Menus

# Initialization of the plate
lcd = Adafruit_CharLCDPlate.Adafruit_CharLCDPlate()
lcd.begin(16,2)
lcd.clear()
lcd.message("  Introducing\n  RaspiCorder")
sleep(2)
lcd.clear()

# Definition of utility functions
def instrumentInput():
	instmenu = Menus.InstrumentMenu()
	instSelection = instmenu.getInstrumentInput(lcd)
	lcd.clear()
	return instSelection

def RecConfirm(instName):
	recmenu = Menus.ConfirmationMenu(lcd, instName)
	recSelect = recmenu.InstrumentConfirm()
	lcd.clear()
	return recSelect

# Menu logic
while True:
	inst = instrumentInput()
	instName = Menus.Instrument.instrumentName(inst)

	beginRecording = RecConfirm(instName)

	if not beginRecording:
		continue

	# TODO: begin recording

