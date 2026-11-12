# Problem: Print perfect squares
# Topic:   03 - Iteration: Loops & Iteration Analysis


def main():
    # Print perfect squares from 1 to N
    N = int(input("Enter a positive integer N: "))

    # Print perfect squares from 1 to N
    print(f"Perfect squares from 1 to {N}:")
    for i in range(1, N + 1):
        square = i * i
        if square > N:
            break
        print(square, end=" ")
    print()  # Print a newline after the loop

if __name__ == "__main__":
    main()
