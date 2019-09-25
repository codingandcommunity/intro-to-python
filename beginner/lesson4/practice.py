import random

'''
Practice exercises for lesson 4 of beginner Python.
'''

# Level 1
# Ask the user if they want ice cream.
# If the user says no, keep asking!
# If the user says yes, print "yay!"

inp = input("Do you want ice cream? ")



# Level 2
# Goal: determine which numbers are even.
# Ask the user how many numbers we should check
# Use a loop to iterate through the numbers between 0 and the number of the user input
# Hint: use the modulus operator -> # % 2 == 1 means that the number is odd and # % 2 == 0 means the number is even

num = int(input("Input a positive number greater than 0. "))



# Level 3
# Goal: create a number guessing game.
# Pick a random number for the user to try to guess. Don't display it for the user!
# Ask the user to guess a number between 0 and 100.
# After the user guesses, tell them if the number is too high, too low, or correct.
# Repeat asking them until they guess the right number.

n = random.randint(1, 100)
