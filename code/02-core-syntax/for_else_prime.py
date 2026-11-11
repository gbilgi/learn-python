"""
This program checks for prime numbers in a given range.
It uses a for-else loop to determine if a number is prime or not.
The outer loop iterates through numbers from 2 to 9.
The inner loop checks if the current number is divisible by any number from 2 to itself (exclusive).
If a divisor is found, it prints that the number is not prime and breaks out of the inner loop.
If no divisors are found, the else block of the inner loop executes, indicating that the number is prime.
"""

for num in range(2, 10):
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime")