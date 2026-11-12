# Problem: Max of two
# Topic:   02 - Operators and Control Statements


def main():
    # Gather input
    A = int(input("Enter first number: "))
    B = int(input("Enter second number: "))

    # Compare values and display result
    if A > B:
        print(f"{A} is greater than {B}.")
    elif A < B:
        print(f"{B} is greater than {A}.")
    else:
        print(f"{A} is equal to {B}.")


if __name__ == "__main__":
    main()
