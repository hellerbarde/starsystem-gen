import GURPS_Dice as GD

StEvoTable = {
	'mass': [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55,
		     0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05,
		     1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.6,
		     1.7, 1.8, 1.9, 2.0],
	'type': ['M7', 'M6', 'M5', 'M4', 'M4', 'M3', 'M2', 'M1', 'M0',
			 'K8', 'K6', 'K5', 'K4', 'K2', 'K0',
			 'G8', 'G6', 'G4', 'G2', 'G1', 'G0',
			 'F9', 'F8', 'F7', 'F6', 'F5', 'F4', 'F3', 'F2', 'F0',
			 'A9', 'A7', 'A6', 'A5'],
	'temp': [3100, 3200, 3200, 3300, 3300, 3400, 3500, 3600, 3800,
			 4000, 4200, 4400, 4600, 4900, 5200, 5400, 5500, 5700,
			 5800, 5900, 6000, 6100, 6300, 6400, 6500, 6600, 6700,
			 6900, 7000, 7300, 7500, 7800, 8000, 8200]
	# To be continued...
	}

class Star:
	roller = GD.DiceRoller()

	def roll(self, dicenum, modifier):
		return self.roller.roll(dicenum, modifier)
	
	def __init__(self, age):
		roller = GD.DiceRoller()
		self.randommass()
		self.setAge(age)
		self.printinfo()
	
	def printinfo(self):
		print("  Star Info")
		print("  ---------")
		#print("        Age:\t{}".format(self.__age))
		print("       Mass:\t{}".format(self.__mass))
		print("       Type:\t{}".format(self.__type))
		print("  ---------\n")
	
	def getMass(self):
		return self.__mass
	
	def getAge(self):
		return self.__age
	
	def setAge(self, age):
		self.__age = age
	
	def randommass(self):
		# Roll randomly for the star mass and type 
		diceroll1 = self.roll(3, 0)
		diceroll2 = self.roll(3, 0)
		#print("Roll 1: {}\t Roll2: {}".format(diceroll1, diceroll2))
		if diceroll1 == 3:
			if diceroll2 > 11:
				self.__mass = 2.0
				self.__type = "A5"
			else:
				self.__mass = 1.9
				self.__type = "A6"
		if diceroll1 == 4:
			if diceroll2 < 9:
				self.__mass = 1.8
				self.__type = "A7"
			elif diceroll2 > 11:
				self.__mass = 1.6
				self.__type = "F0"
			else:
				self.__mass = 1.7
				self.__type = "A9"
		if diceroll1 == 5:
			if diceroll2 < 8:
				self.__mass = 1.5
				self.__type = "F2"
			elif diceroll2 > 12:
				self.__mass = 1.35
				self.__type = "F5"
			elif diceroll2 > 10:
				self.__mass = 1.4
				self.__type = "F4"
			else:
				self.__mass = 1.45
				self.__type = "F3"
		if diceroll1 == 6:
			if diceroll2 < 8:
				self.__mass = 1.3
				self.__type = "F6"
			elif diceroll2 < 10:
				self.__mass = 1.25
				self.__type = "F7"
			elif diceroll2 == 10:
				self.__mass = 1.2
				self.__type = "F8"
			elif diceroll2 < 13:
				self.__mass = 1.15
				self.__type = "F9"
			else:
				self.__mass = 1.1
				self.__type = "G0"
		if diceroll1 == 7:
			if diceroll2 < 8:
				self.__mass = 1.05
				self.__type = "G1"
			elif diceroll2 < 10:
				self.__mass = 1.0 
				self.__type = "G2"
			elif diceroll2 == 10:
				self.__mass = 0.95
				self.__type = "G4"
			elif diceroll2 < 13:
				self.__mass = 0.9 
				self.__type = "G6"
			else:
				self.__mass = 0.85
				self.__type = "G8"
		if diceroll1 == 8:
			if diceroll2 < 8:
				self.__mass = 0.8 
				self.__type = "K0"
			elif diceroll2 < 10:
				self.__mass = 0.75
				self.__type = "K2"
			elif diceroll2 == 10:
				self.__mass = 0.7 
				self.__type = "K4"
			elif diceroll2 < 13:
				self.__mass = 0.65
				self.__type = "K5"
			else:
				self.__mass = 0.6 
				self.__type = "K6"
		if diceroll1 == 9:
			if diceroll2 < 9:
				self.__mass = 0.55
				self.__type = "K8"
			elif diceroll2 < 12:
				self.__mass = 0.5
				self.__type = "M0"
			else:
				self.__mass = 0.45
				self.__type = "M1"
		if diceroll1 == 10:
			if diceroll2 < 9:
				self.__mass = 0.4 
				self.__type = "M2"
			elif diceroll2 < 12:
				self.__mass = 0.35
				self.__type = "M3"
			else:
				self.__mass = 0.3 
				self.__type = "M4"
		if diceroll1 == 11:
			self.__mass = 0.25
			self.__type = "M4"
		if diceroll1 == 12:
			self.__mass = 0.2
			self.__type = "M5"
		if diceroll1 == 13:
			self.__mass = 6.15
		if diceroll1 > 13:
			self.__mass = 0.1
			self.__type = "M7"
		
		#print("Random mass {} generated.".format(self.__mass))
