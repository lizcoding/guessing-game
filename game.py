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
    if not guess.isdigit():
        print("Please enter digits only.")
        continue
    guess = int(guess)
    if guess > 100 or guess < 1:
        print("Please use a number between 1 and 100.")
        continue
    count += 1
    if guess == correct_num:
        print(f"Well done, {name}! You found my number in {count} tries!")
        break
    elif guess < correct_num:
        print("You guessed too low! Try again.")
    else:
        print("You guessed too high! Try again.")