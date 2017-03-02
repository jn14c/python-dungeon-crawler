from hacker import Hacker
from warrior import Warrior
import sys
import random
class Player:
	def __init__(self, charT):
		if charT == 'H':
			self.h = Hacker()
			self.charType = "Hacker"
		elif charT == 'W':
			self.h = Warrior()
			self.charType = "Warrior"
		self.maxHP = self.h.getHP()
		self.strength = self.h.getStr()
		self.defense = self.h.getDef()
	def health(self):
		return self.maxHP
	def quit(self):
		return "The overwhelming discomfort of Langley's sanctuary has forced you to run and ditch the thumb wand. Your heart sinks as you run towards the door and it closes and disapears. You bang where the door was and find it has turned into solid stone. Langley laughs and you hear his voice say, 'Grab them quickly, for we have a new test subject for my Linux android. HA HA HA!!.' All you can hear is the sound of mechanical keys clicking louder and louder as they aproach then...."

	def help(self):
		return("go [N, S, E, Q]\nquit\nattack\nhealth\nhelp")
	def goN(self, pp):
		if pp[0] == 0:
			
			return(0, 0)
		else:
			x = pp[0] - 1
			y = pp[1]
			return (x,y)
	def goW(self, pp):
		if pp[1] == 0:
			
			return(0, 0)
		else:
			x = pp[0]
			y = pp[1] - 1
			return (x,y)
	def goE(self, pp):
		if pp[1] == 4:
			
			return(0, 0)
		else:
			x = pp[0]
			y = pp[1] + 1
			return (x,y)
	def goS(self, pp):
		if pp[0] == 4:
			
			return(0, 0)
		else:
			x = pp[0] + 1
			y = pp[1]
			return (x,y)
	def attack(self, playar, defense):
		damage = random.randint(0, 6) + self.strength - defense
		if damage <= 0:
			return 0
		else:
			return damage
	def hit(self, dmg):
		self.maxHP = self.maxHP - dmg
	def getDef(self):
		return self.defense
