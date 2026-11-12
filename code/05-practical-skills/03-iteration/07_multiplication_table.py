# Problem: Multiplication table
# Topic:   03 - Iteration: Loops & Iteration Analysis


def main():
    # Gather user input for N
    N = int(input("Enter a positive integer N: "))

    # Print multiplication table for N
    print(f"Multiplication table for {N}:")
    for i in range(1, 11):
        print(f"{N} x {i:2} = {N * i}")  #i:2 - Alignment for better readability

if __name__ == "__main__":
    main()
