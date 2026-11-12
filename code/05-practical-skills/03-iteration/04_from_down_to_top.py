# Problem: From down to top
# Topic:   03 - Iteration: Loops & Iteration Analysis


def main():
    # Get user input for N
    N = int(input("Enter a positive integer N: "))

    # Print numbers from 1 to N
    for i in range(1, N + 1):
        print(i, end=' ')
    print()  # Print a newline after the loop
    
if __name__ == "__main__":
    main()
