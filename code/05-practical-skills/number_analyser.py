"""
This program analyzes a list of numbers entered by the user.
It prompts the user to enter numbers one by one until they type 'done'.
After the user is done entering numbers, it calculates and displays the total, average, maximum, and minimum of the entered numbers.
It also provides a distribution analysis, indicating whether each number is below, above, or equal to the average.
"""


def analyze_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    if not numbers:
        print("No numbers entered.")
        return

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    print(f"\nAnalysis of {len(numbers)} numbers:")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

    print("\nNumber distribution:")
    for num in numbers:
        if num < average:
            print(f"{num} is below average")
        elif num > average:
            print(f"{num} is above average")
        else:
            print(f"{num} is equal to average")

if __name__ == "__main__":
    analyze_numbers()