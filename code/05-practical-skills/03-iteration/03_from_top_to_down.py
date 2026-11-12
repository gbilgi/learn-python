# Problem: From top to down
# Topic:   03 - Iteration: Loops & Iteration Analysis


def main():
    # Get user input for N
    N = int(input("Enter a positive integer N: "))

    # Print numbers from N down to 1
    for i in range(N, 0, -1):
        print(i, end=' ')
    print()  # Print a newline after the loop

if __name__ == "__main__":
    main()
