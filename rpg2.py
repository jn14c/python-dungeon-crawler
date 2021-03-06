'''client-server version of rpg game. 
uses the client.py module to connect 
and play the game

JOEL NEAL /// JN14C'''

import random
from character import Character
import SocketServer
import threading
import time
class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
		
	def handle(self):
		
#item postion instantiation
		e1p = (random.randint(0,4), random.randint(0,4))
		e2p = (random.randint(0,4), random.randint(0,4))
		while e2p == e1p:
			e2p = (random.randint(0,4), random.randint(0,4))
		e3p = (random.randint(0,4), random.randint(0,4))
		while e3p == e2p or e3p == e1p:
			e3p = (random.randint(0,4), random.randint(0,4))
		e4p = (random.randint(0,4), random.randint(0,4))
		while e4p == e3p or e4p == e2p or e4p == e1p:
			e4p = (random.randint(0,4), random.randint(0,4))
		bpp = (random.randint(0,4), random.randint(0,4))
		while bpp == e4p  or bpp == e3p or bpp == e2p or bpp == e1p:
			bpp = (random.randint(0,4), random.randint(0,4))
		pp = (random.randint(0,4), random.randint(0,4))
		while pp == bpp or pp == e4p  or pp == e3p or pp == e2p or pp == e1p:
			pp = (random.randint(0,4), random.randint(0,4))
		rt = (random.randint(0,4), random.randint(0,4))
		while rt == pp  or rt == bpp or rt == e4p  or rt == e3p or rt == e2p or rt == e1p:
			rt = (random.randint(0,4), random.randint(0,4))
#init game board 5x5 matrix
		gameboard = [[0]*5 for i in range(5)]
#put units on board
		gameboard[e1p[0]][e1p[1]] = 'E'
		gameboard[e2p[0]][e2p[1]] = 'E'
		gameboard[e3p[0]][e3p[1]] = 'E'
		gameboard[e4p[0]][e4p[1]] = 'E'
		gameboard[bpp[0]][bpp[1]] = 'B'
		gameboard[pp[0]][pp[1]] = 'P'
		gameboard[rt[0]][rt[1]] = 'R'
	
	#Enter your characters info
		self.request.send('Enter your characters name: ')
		cName = self.request.recv(100)
		while True:
			
			self.request.send("Are you a CodeWarrior or 1337H4x0r? Enter [c] or [h]: ")
			charType = self.request.recv(4)
			if charType[0] == "c" or charType[0] == "h":
					break
		if charType[0] == "c":
			player = Character("P", "W")
		elif charType[0] == "h":
			player = Character("P", "H")
#story
		print "Server is conncected and prepared to serve " + cName +"'s every need your highness..."
		self.request.send("A mystic storm has rolled through Tallahassee knocking out all the LOV building power. While you were studying in the majors lab, a hoard of COP3014 goblins start panicking cause the power is off... Unable to hold your composure after the 20 minutes of reading a book under the light of your smartphone and the goblins repetitively talking about the power outage, you say some obfuscated jibberish and start leaving startling the goblins. You check your pocket for your mythically imbued thumb wand (USB thumbdrive), but to your dismay it is gone. There is no way you could live without your 64GB wand, all those assignments, all those projects, all those torrents, NOOOOOOOO!!!! You start to get dizzy, feeling like you are going to pass out, well, you actually do pass out. You wake up with the room dim, illuminated only by a strange light. You follow the light and find out it is a sole COP3014 goblin appling snapchat filters to their selfie. You make awkward eye contact as you leave the majors lab. In the distance, you hear the faint sound of a wolf howling. 'Hmm, probably that one sorceress's wolf, Ben or whatever' you say. You have a unsettling feeling, a feeling like you are forgetting something. Oh yeah, your thumb wand, duh. You recall you were in the networking lab working on your Linux admin project. You run into a familiar face on your epic trek from the majors lab to the networking lab. Its the powerful sorceress Caitlin. She asks if you started working on your mid-term project yet. You nod and say 'mmhmm' (liar...). The young sorceress sees you walking down the path to the computer catacombs. Her eyes go wide as she exclaims 'wait...' you're going to the catacombs at this hour? she asks. You reply 'yeah... I forgot my thumb wand' you say. 'Legend has it professor Langley performed wicked black magic experiments on the remains of old Linux machines and they come to life during the blood moon' she says. In a stern voice she says, 'Heed my warning young bit-crafter.' You roll your eyes and say to yourself, 'Oh okay lady.' You travel down the catacomb hall, each step darker and darker. Finally, you reach the end of the hall past the mires of the forgotten tech. You see a sign illuminated by an orangish, flickering candle light. MECHANICAL RAT TRAPS ARE SET it reads. SNAP!! The haunting sound of an echoing rat trap snap from behind makes the hair on the back of your neck stand up. You step into the networking lab and your epic quest begins...")
#loop to handle user input and handle the board
		l = True
		while l ==True:
			#userInput = raw_input()
			userInput = self.request.recv(48)
			if userInput == "help":
				self.request.send(player.help())
			elif userInput == "health":
				self.request.send(cName + " has " + str(player.health()) + " HP.")
			elif userInput == "quit":
				self.request.send(player.quit() + " Press enter to exit.")
				l = False
			elif userInput == "go N":
				xy = player.goN(pp)
				if xy == (0,0):
					self.request.send("You have run into a wall. Try a different direction")
				else:
					self.request.send(" ")
					if gameboard[xy[0]][xy[1]] == "E":
						gameboard[pp[0]][pp[1]] = 0
						gameboard[xy[0]][xy[1]] = "P"
						pp = xy
						doe = self.fight(player)
						if doe == "quit":
							self.request.send(player.quit() + " Press enter to exit.")
							l = False
					elif gameboard[xy[0]][xy[1]] == "R":
						self.ratDeath()
						l = False
					elif gameboard[xy[0]][xy[1]] == "B":
						self.win()
						l = False
					else:
						gameboard[xy[0]][xy[1]] = "P"
						gameboard[pp[0]][pp[1]] = 0				
						pp = xy
				
			elif userInput == "go W":
				xy = player.goW(pp)
				if xy == (0,0):	
					self.request.send("You have run into a wall. Try a different direction")
				else:
					self.request.send(" ")
					if gameboard[xy[0]][xy[1]] == "E":
						gameboard[pp[0]][pp[1]] = 0
						gameboard[xy[0]][xy[1]] = "P"
						pp = xy
						doe = self.fight(player)
						if doe == "quit":
							self.request.send(player.quit() + " Press enter to exit.")
							l = False
					elif gameboard[xy[0]][xy[1]] == "R":
						self.ratDeath()
						l = False
					elif gameboard[xy[0]][xy[1]] == "B":
						self.win()
						l = False
					else:
						gameboard[pp[0]][pp[1]] = 0
						gameboard[xy[0]][xy[1]] = "P"
						pp = xy

			elif userInput == "go E":
				xy = player.goE(pp)
				if xy == (0,0):	
					self.request.send("You have run into a wall. Try a different direction")
				else:
					self.request.send(" ")
					if gameboard[xy[0]][xy[1]] == "E":
						gameboard[pp[0]][pp[1]] = 0
						gameboard[xy[0]][xy[1]] = "P"
						pp = xy
						doe = self.fight(player)
						if doe == "quit":
							self.request.send(player.quit() + " Press enter to exit.")
							l = False
					elif gameboard[xy[0]][xy[1]] == "R":
						self.ratDeath()
						l = False
					elif gameboard[xy[0]][xy[1]] == "B":
						self.win()
						l = False
					else:
						gameboard[pp[0]][pp[1]] = 0
						gameboard[xy[0]][xy[1]] = "P"
						pp = xy
				
			elif userInput == "go S":
				xy = player.goS(pp)
				if xy == (0,0):	
					self.request.send("You have run into a wall. Try a different direction")
				else:
					self.request.send(" ")
					if gameboard[xy[0]][xy[1]] == "E":
						gameboard[pp[0]][pp[1]] = 0
						gameboard[xy[0]][xy[1]] = "P"
						pp = xy
						doe = self.fight(player)
						if doe == "quit":
							self.request.send(player.quit() + " Press enter to exit.")
							l = False
					elif gameboard[xy[0]][xy[1]] == "R":
						self.ratDeath()
						l = False
					elif gameboard[xy[0]][xy[1]] == "B":
						self.win()
						l = False
					else:
						gameboard[pp[0]][pp[1]] = 0
						gameboard[xy[0]][xy[1]] = "P"
						pp = xy
		
			elif userInput == "attack":
				self.request.send( "There is nothing to attack.")
					
			else:
				self.request.send( cName + " has no clue what you are talking about.")
		self.request.close()

#functions-----------------------------------------------
	def ratDeath(self):
		self.request.send("You move forward slowly, cautiously, but the room's darkness masks its guise. 'Click' is the last thing you hear as the you trigger the rap trap you were warned about. Press enter to exit.")

	def nothing(self):
		self.request.send("You don't see anything that needs a whooping")

	def chicken(self):
		self.request.send("You can't run, chicken.")

	def fight(self,player):
		self.request.send("'BEEP!!! INTRUDER DETECTED.' You encounter one of the wicked Linux robots! Prepare to put your dukes up!")
		e1 = Character("B", "L")
		while True:
			userIn = self.request.recv(24)
			if userIn == "attack":
				damage = player.attack(player, e1.getDef())
				if damage <= 0:
					self.request.send("Swing and a miss. Bot evaided your attack\n")
				else:
					self.request.send(self.playerAttack() + "for " + str(damage) + " damage.\n")
				e1.botHit(damage)
				bDamage = self.botDMG(player, e1)
				player.hit(bDamage)
				if bDamage <= 0:
					self.request.send("You're quick on your feet. You dodged the bots attack\n")
				else:
					self.request.send(self.botAttack() + "for " + str(bDamage) + " damage.\n")
			else:
				if userIn == "help":
					self.request.send(player.help())
				elif userIn == "quit":
					return "quit"
				elif userIn == "health":
					self.request.send("You have " + str(player.health()) + " HP.")
				elif userIn == "go N":
					self.chicken()
				elif userIn == "go E":
					self.chicken()
				elif userIn == "go W":
					self.chicken()
				elif userIn == "go S":
					self.chicken()
				else:
					self.request.send("Type help to see a list of recognized commands.")
			if e1.health() <= 0:
				break
			if player.health() <= 0:
				break
		if e1.health() <= 0:
			finishers = []		
			finishers.append("The bot's scanner miscalculates its step leaving its power button vulernable. you jump in pressing and holding the power button which shuts the bot down. You continue on your way...\n\n")
			finishers.append("You feel frisky and try a kung fu move you saw in a Bruce Lee tribute video on YouTube. The roundhouse kick knocks off the bots head. You keep moving along...\n\n")
			self.request.send(finishers[random.randint(0,1)])
		elif player.health() <= 0:
			self.request.send("The bot freaks out, you gasp as the the final strike comes barreling towards you. You try to dodge the attack, but the bot fires a lasso which holds you in place. POW! The bot connects with a powersupply fist punch. K.O. You go down like a lead balloon, and when you wake up, you discover Langley has turned you into part of his android army, stowed away in a closet and lurking the lab only when the bloodmoon glistens. Press enter to quit.")
	

	def botAttack(self):
		attacks = []
		attacks.append("The bot socked you in the upper lip with its power supply fist ")
		attacks.append("Linux bot used a mouse as a flail and smacked you upside the head ")
		attacks.append("The evil bot shoots a mechanical key 'J' at your forehead leaving an imprinted 'L', HAHA! LOSER... heh ")
		attacks.append("Bot pull you close and head-butts you with a CRT monitor, OUCH ")
		attacks.append("The bot's upper torso starts spinning like a whirlwind and slaps you IN THE FACE with its num pad keyboard hand ")
		attacks.append("Wuh-PSHHH! The bot whipped you with a frayed power supply cable ")
		attacks.append("Linux bot clasps your wrist and repetively smacks you in the face and saying in its robotic synthesis voice, 'stop hitting your self' ")
		attacks.append("The bot starts blaring Nickelback right in your ear ")
		return attacks[random.randint(0,7)]

	def playerAttack(self):
		pattacks = []
		pattacks.append("You foot sweep the bot causing it to smack its CRT head on the ground ")
		pattacks.append("You whack the bot with your satchel ")
		pattacks.append("You pour your Starbucks on the bot ")
		pattacks.append("You kick the bot right in the hard drive, Whoa... c'mon, low blow ")
		pattacks.append("You say 'Come at me bro.' The bot lunges, missing you. You counter by kneeing it in the bot stomach. 'BOOM, RIGHT IN THE MOTHERBOARD!' you say.  ")
		pattacks.append("You shank the bot with your car key ")
		pattacks.append("You pull out the taser your mom bought you and zap the bot ")
		pattacks.append("You roll up an old ACM magazine and slap the bot ")
		return pattacks[random.randint(0,7)]

	def botDMG(self, play, bot):
		dmg = random.randint(0,6) + bot.getStr() - play.getDef()
		if dmg <=0:
			return 0
		else:
			return dmg 
	def win(self):
		self.request.send("You sneak past a bot almost silently. You make it to your PC. You scan the area looking for the thumb wand. There it is! 'AH HA' you say without thinking. Ominous beeps start blaring like crickets on a summer evening. Langley's voice is heard over the intercom, 'Who's there?!?.' Next, You hear that line you've heard so many times INTRUDER DETECTED. The bots surround you. 'This is it' you think to yourself. A bright colorful aura lights the room causing the bots to take their focus off you. You hear some sort of ancient scripture being recited in the background. The bots move just enough to see the commotion. The aura lights the mysterious figure. It's sorceress Caitlin! She says, 'GET DOWN!.' A portal opens up and a three headed python made of pure flames comes flying in. 'HISSSS' the bots are no match for sorceress Caitlin's hex. Levitating past the charred scraps of bots she yells out, 'LANGLEY! I told you not my bit-crafters!.' Langley responds, 'Aww, I know, but c'mon. Let me have have just one.' Sorceress Caitlin whistles and yells 'BEN!'. A panting wolf comes charging in. Not a second later the power is restored. She gets on the wolf's back, looks back and asks, 'Hop on. I'll give you a lift back to the majors' encampment.' You hop on the wolf, and the wolf begins racing forward at full speed. You ask, 'When are you going to teach me how to summon a fire python sorceress Caitlin?' She says, 'Heh, maybe once you master your twisted spells young bit-crafter.' Press enter to quit.")

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass

if __name__ == "__main__":
	HOST, PORT = "localhost", 9000
	server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
	server_thread = threading.Thread(target=server.serve_forever)
	server_thread.start()

