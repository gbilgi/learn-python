""""
This program checks if a number is odd or even.
It takes an integer input from the user and prints the result.
"""
# Get user input (input is always a string)
number = int(input("Enter a number: "))

# Check if the number is odd or even using the modulus operator
if number % 2 == 1:
	print(f"{number} is odd.")
else:
	print(f"{number} is even.")
