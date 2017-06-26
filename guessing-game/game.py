"""A number-guessing game."""

# Put your code here

import random  

def guessing_game():
	num = random.randint(1,101)
	name = raw_input("Howdy, what's your name? ")
	guesses = 0
	guess = 0

	print name + ", I'm thinking of a number between 1 and 100"
	print "Try to guess my number."

	while guess != num:
		guess = int(raw_input("Your guess? "))
		guesses += 1 
		if guess > num:
			print "That's too high."
		elif guess < num:
			print "That's too low."
		else:
			print "Good job! You got it in", guesses, "guesses!"
			play = raw_input("Would you like to play again? Y or N ")
			if play == "y".upper():
				guessing_game()
			else: 
				break

guessing_game()

