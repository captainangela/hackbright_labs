"""A number-guessing game."""

# Put your code here

import random  

num = random.randint(1,101)
name = raw_input("Howdy, what's your name? ")
guesses = 0

print name + ", I'm thinking of a number between 1 and 100"
print "Try to guess my number."
print num

guess = 0

while guess != num:
	guess = int(raw_input("Your guess? "))
	guesses += 1 
	if guess > num:
		print "That's too high."
	elif guess < num:
		print "That's too low."
	else:
		print "You got it in", guesses, "guesses"
		



