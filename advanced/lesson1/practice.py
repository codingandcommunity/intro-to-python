'''
This file includes practice code that should refresh
your memory on basic Python concepts. If anything here
looks totally out of wack, ask an instructor for help!

Remove the triple quotes around each code block to run it
'''
# ~~ Variables and I/O ~~
'''
x = 9
x += 2 # x is now 11
print(x)

a = "strings can be"
b = " added "
c = "like this!"
print(a + b + c)

# Get input from the user, click into the terminal to respond
name = input("Hi there, what is your name? ")
print("Thanks for coming, " + name + "!")
'''

# ~~ If Statements and Logic ~~
'''
a = True
b = False

# Not 'flips' a boolean variable
print("a and b flipped are:")
print('a: ' + str(not a))
print('b: ' + str(not b))

# An if statement can have two branching paths
# Don't forget the colons!
if a:
    print("a is true")
else:
    print("a is false")

# Add more outcomes with elif
if a:
    print("a is still true")
elif b:
    print("a is false but b is true")
else:
    print("nothing is true")

# and, not, and or make if statements more complex
if a or b:
    print("One of a and b are true")
if a and b:
    print("Both a and b are true")
if not (a or b):
    print("Neither a nor b are true")
'''

# ~~ Loops ~~
'''
# There are two flavors of loops: for and while

# For loops execute a set number of times
print("Numbers from 1-10 (for loop)")
for i in range(11):
    print(i, end=" ")
print()
# While loops execute as long as a condition is true
i = 0
print("Numbers from 1-10 (while loop)")
while i <= 10:
    print(i, end=" ")
    i += 1 # What if this was multiplication by 2?
print()
# A more complex while loop
# 'break' tells Python to end the loop prematurely
print("Some more numbers")
i = 1
while i < 6:
  print(i, end=" ")
  if i == 3:
    break
  i += 1

print()
'''

# ~~ Functions ~~
'''
# Functions collect code with a common purpose in one block
def star_staircase(steps):
    """ 
    I'm a comment that says what the function does

    It makes a stair case of stars, like so:
    star_staircase(3) ->
      *
     **
    *** 
    """
    
    for i in range(steps):
        print(" " * (steps - i - 1), end="")
        print("*" * (i+1))

star_staircase(3)
star_staircase(6)

# star_staircase doesn't return a value, but this one does
def pig_latin(string):
    """
    Translates string to pig latin under the following rules:
    - If first letter is a vowel, simply add 'ay'
    - If first letter is consonant, put it at the end of the word and add
        'ay'
    """
    vowels = 'aeiou'
    ay = 'ay'
    if string[0].lower() not in vowels:
        string += string[0]
        string = string[1:]
    
    return string.lower().capitalize() + ay

print(pig_latin("Hello"))
print(pig_latin("Please"))
'''