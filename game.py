"""A number-guessing game."""

# Put your code here
from random import randint


print("Howdy, what's your name?")
name = input("(type in your name) ")

print(f"{name}, I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")

correct_num = randint(1, 100)
count = 0

while True:
    guess = input("Your guess? ")
    count += 1
    if guess == correct_num:
        pass
    else:
        pass

"""
get user's guess
check if guess is correct
if guess is correct:
    break
else:
    tell them if it is too low or too high
"""


"""
$ python3 game.py
the loop part:

Your guess? 50
Your guess is too low, try again.
Your guess? 80
Your guess is too high, try again.
Your guess? 60
Your guess is too low, try again.
Your guess? 70
Your guess is too high, try again.
Your guess? 63
Your guess is too low, try again.
Your guess? 64
Your guess is too low, try again.
Your guess? 67
Your guess is too low, try again.
Your guess? 69
Your guess is too high, try again.
Your guess? 68
Well done, Jessica! You found my number in 9 tries!
"""