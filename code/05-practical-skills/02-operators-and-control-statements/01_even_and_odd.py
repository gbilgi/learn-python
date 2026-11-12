# Problem: Even and odd
# Topic:   02 - Operators and Control Statements


def main():
    # Gather input
    num = int(input("Enter a number: "))

    # Check divisibility by 2 and print result
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")


if __name__ == "__main__":
    main()
