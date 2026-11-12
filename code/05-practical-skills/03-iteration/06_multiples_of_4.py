# Problem: Multiples of 4
# Topic:   03 - Iteration: Loops & Iteration Analysis


def main():
    # Get user input for N
    N = int(input("Enter a positive integer N: "))

    # Print multiples of 4 from 1 to N
    for i in range(1, N + 1):
        if i % 4 == 0:
            print(i, end=' ')
    print()  # Print a newline after the loop

if __name__ == "__main__":
    main()
