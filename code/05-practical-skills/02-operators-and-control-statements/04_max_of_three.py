# Problem: Max of three
# Topic:   02 - Operators and Control Statements


def main():
    # Gather input
    A = int(input("Enter first number: "))
    B = int(input("Enter second number: "))
    C = int(input("Enter third number: "))

    # Step 2: Find the maximum of the three numbers
    max_num = A
    if B > max_num:
        max_num = B
    if C > max_num:
        max_num = C
    print(f"Maximum of {A}, {B}, and {C} is: {max_num}")


if __name__ == "__main__":
    main()
