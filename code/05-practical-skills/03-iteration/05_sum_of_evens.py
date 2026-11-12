# Problem: Sum of evens
# Topic:   03 - Iteration: Loops & Iteration Analysis


def main():
    # Gather user input for N
    N = int(input("Enter a positive integer N: "))
    
    # Initialize total sum of even numbers
    total = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            total += i
    print(f"Sum of even numbers from 1 to {N} = {total}")
    
if __name__ == "__main__":
    main()
