from player import Player
from bot import Bot
class Character:
	def __init__(self, typeC, clazz):
		if typeC == "P":
			self.charT = Player(clazz)
		if typeC == "B":
			self.charT = Bot()
	def help(self):
		return self.charT.help()
	def quit(self):
		return self.charT.quit()
	def health(self):
		return self.charT.health()		
	def goN(self, pp):
		return self.charT.goN(pp)
	def goE(self, pp):
		return self.charT.goE(pp)
	def goW(self, pp):
		return self.charT.goW(pp)
	def goS(self, pp):
		return self.charT.goS(pp)
	def getStr(self):
		return self.charT.getStr()
	def getDef(self):
		return self.charT.getDef()
	def attack(self, charT, defense):
		return self.charT.attack(charT, defense)
	def botHit(self, dmg):
		self.charT.botHit(dmg)
	def hit(self, dmg):
		self.charT.hit(dmg)

		
