"""
This program generates a random number between 1 and 10 and prompts the user to guess the number.
It uses a while loop to repeatedly ask the user for their guess until they guess the correct number.
If the user's guess is too low or too high, it provides feedback accordingly.
Once the user guesses the correct number, it congratulates them and exits the loop."""


import random
number = random.randint(1, 10)
guess = 0

# Use a while loop to repeatedly ask the user for their guess until they guess the correct number
while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {number}!")