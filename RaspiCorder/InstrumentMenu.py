from enum import Enum

class Instrument(Enum):
  drums = 1
  guitar = 2
  bass = 3
  other = 4

class InstrumentMenu(self):
	str instrumentSelection = "Drums Bass\nGuitar Other"
	Instrument selected = Instrument.drums
	#TODO
