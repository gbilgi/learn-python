"""This program takes three numbers as input from the user and determines the maximum number among them using if-elif-else statements."""

# Get user input (input is always a string)
first = input("Enter the first number: ")
second = input("Enter the second number: ")
third = input("Enter the third number: ")

# Convert the input strings to integers
first = int(first)
second = int(second)
third = int(third)

# Determine the maximum number using if-elif-else statements
if (first >= second) and (first >= third):
	maximum = first
elif (second >= first) and (second >= third):
	maximum = second
else:
	maximum = third

# Create an output message using an f-string
print(f"The maximum number is: {maximum}")