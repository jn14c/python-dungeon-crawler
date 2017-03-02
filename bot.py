class Bot:
	def __init__(self):
		self.type = "Linux robot"
		self.maxHP = 15
		self.strength = 9
		self.defense = 7
	def health(self):
		return self.maxHP
	def getStr(self):
		return self.strength
	def getDef(self):
		return self.defense
	def botHit(self, dmg):
		self.maxHP = self.maxHP - dmg
		
