#!/usr/bin/env python3

import sys
import random

def rollDice(n):
	num = random.randint(1,n)
	return num

def startAgain(inp):
	if (inp == "no" or inp == "n"):
		sys.exit()
	elif (inp == "yes" or inp == "y"):
		numSides = int(input("How many sided dice? "))
		print(rollDice(numSides))
		again = input("Play again? ")
		again.lower()
		if (again == "no" or again == "n"):
			sys.exit()
		elif (again == "yes" or again == "y"):
			return startAgain(again)
		else:
			print("Unknown Response")
	else:
		print("Unknown Response")
	return

userIn = input("Do you want to gamble: ")
userIn.lower()
startAgain(userIn)


"""while (userIn == "yes" or userIn == "y"):
	sides = int(input("How many sided dice? "))
	print(rollDice(sides))"""

