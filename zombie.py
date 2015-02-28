# game.py
# Zombie Survival
# Author: Cameron Johnson
# Date: 2/26/15

import random as r

#Creating a character class. Characters have a name, hp, ammo, and damage
class Character():
	#Initializing the character. He has a name, hp, ammo, damage, and Scavenging level
	def __init__(self, name, hp, ammo, damage):
		self.name = name
		self.hp = hp
		self.ammo = ammo
		self.damage = damage

	#Basic get statements
	def getHP(self):
		return self.hp
	def getName(self):
		return self.name
	def getAmmo(self):
		return self.ammo
	def getDmg(self):
		return self.damage

	#To check if the player is dead
	def isDead(self):
		if self.hp <= 0:
			return True
		else:
			return False
#Creating the zombie class. They have hp and do damage
class Zombie():
	def __init__(self, hp, dmg):
		self.hp = hp
		self. dmg = dmg
	def getHP(self):
		return self.hp
	def getDmg(self):
		return self.dmg
	def isDead(self):
		if self.hp <= 0:
			return True
		else:
			return False

#Introduce all the characters in a set format
def cIntro(player):
	print(player.getName())
	print("		Hp: ", player.getHP())
	print("		Ammo: ", player.getAmmo())
	print("		Damage: ", player.getDmg())
#Print out all the commands in a set format
def printC():
	print("Commands:\n Commands: Bring this up again \n Attack: Shoot at the zombie \n Scavenge: Scavenge for ammo and HP \n Run: Attempt to distance yourself from the zombie. \n HP: Show your hp and the zombie's hp")
#Introduction to the game
def intro(names):
	print("Welcome to Zombie Survival, a turn by turn based zombie fighting game! Please Choose your character.")
	print("Commands:\n Commands: Bring this up again \n Attack: Shoot at the zombie \n Scavenge: Scavenge for ammo and HP \n Run: Attempt to distance yourself from the zombie. \n HP: Show your hp and the zombie's hp")
	for i in names:
		cIntro(i)
#Method for attacking. Fight method.
def attack(pred, prey):
	pDmg = r.randint(1, pred.damage)
	prDmg = r.randint(1, prey.dmg)
	if pDmg >= prDmg:
		print("You successfully attacked doing ", str(pDmg), " damage!")
		prey.hp -= pDmg
		pred.ammo -= 1
		print("Zombie Hp: ", str(prey.hp))
		print("Your Hp: ", str(pred.hp))
	elif pDmg < prDmg:
		print("You try to attack, but the zombie is stronger! He deals ",str(prDmg), " damage to you.")
		pred.hp -= prDmg
		print("Your HP: ", str(pred.hp))
#Method for scavenging. Player has a chance to gain hp.
def scavenge(player, enemy):
	success = False
	dice = r.randint(1,11)
	while True:
		try:
			chance = float(input("Please choose a number, 1 - 10: "))
			if chance not in range(1,11):
				print("Please insert a valid number.")
				continue
			else:
				break
		except ValueError:
			print("Please insert a valid number.")
			continue
	if chance > dice:
		success = True
	if success:
		print("You scavenge and find a health potion. You gain 10 Hp.")
		player.hp += 10
	elif not success:
		print("You tried to scavenge, but failed doing so. The zombie attacked and did ", str(enemy.dmg), " damage.")
		player.hp -= enemy.dmg
#Player can try to distance himself from the enemy
def run(player, enemy):
	runP = False
	while True:
		try:
			chance = float(input("Please choose a number, 1 - 10: "))
			if chance not in range(1,11):
				print("Please insert a valid number.")
				continue
			else:
				break
		except ValueError:
			print("Please insert a valid number.")
			continue
	if chance > 8:
		runP = True
	if runP:
		print("You run and the zombie chases after you. The zombie steps on a trap taking 5 damage.")
		enemy.hp -= 5
	elif not runP:
		print("You try to run, but trip and fall. You take 5 damage.")
		player.hp -= 5
#Main game method
def game(player, enemy, commands):
	#Game loop
	while True:
		#Creating a command line with error handling
		while True:
			try:
				cmdL =  input("Type a command>>> ")
				cmdL = cmdL.lower()
				if cmdL not in commands:
					print("ERROR: INVALID_COMMAND. Type in 'commands' if you need a list of the commands.")
					continue
				else:
					break
			except AttributeError:
				continue
		#Input handling for commands that the player gives
		if cmdL == 'commands':
			printC()
		elif cmdL == 'attack':
			attack(player, enemy)
		elif cmdL == 'scavenge':
			scavenge(player, enemy)
		elif cmdL == 'run':
			run(player, enemy)
		elif cmdL == 'hp':
			hp(player, enemy)
		elif cmdL == 'quit':
			break
		#If player or enemy dies, game is over.
		if player.isDead():
			break
		elif enemy.isDead():
			break
	if player.isDead():
		print("You were slain by the zombie! Better luck next time")
	elif enemy.isDead():
		print("You have slain the zombie! Great Job, you win!")
#Player can check current hp stats
def hp(player, enemy):
	print("Your HP: ", str(player.hp))
	print("Zombie HP: ", str(enemy.hp))
#Main Method
def main():
	#Initializing the possible characters the player can choose
	cam = Character("Cameron", 125, 50, 5)
	marisa = Character("Marisa", 90, 25, 40)
	ross = Character("Ross", 150, 75, 3)
	characters = [cam, marisa, ross]

	names = ["a", "b", "c"]
	cmds = ['commands', 'attack', 'run', 'scavenge', 'hp']
	zombie = Zombie(100, 50)
	intro(characters)
	#Player chooses their character
	while True:
		try:
			player = input("Who do you choose? A) Cameron B) Marisa C) Ross ")
			player = player.lower().strip(' ')
			if player not in names:
				continue
		except ValueError:
			print("Please input a valid response.")
			continue
		else:
			break
	#Handling the players choice
	if player == 'a':
		player = cam
	elif player == 'b':
		player = marisa
	else:
		player = ross
	#Run the game
	game(player, zombie, cmds)
	#Game over. Play again?
	print("Thanks for playing! Would you like to go again? [y/n]")
	while True:
		again = input(">>> ")
		if again == 'y':
			main()
		else:
			break
main()
