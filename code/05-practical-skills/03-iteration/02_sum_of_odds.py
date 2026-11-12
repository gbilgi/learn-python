# Problem: Sum of odds
# Topic:   03 - Iteration: Loops & Iteration Analysis


def main():
    # Calculate the sum of odd numbers from 1 to N
    N = int(input("Enter a positive integer N: "))

    # Calculate the sum of odd numbers from 1 to N
    total = 0
    for i in range(1, N + 1,2):
        total += i
    print(f"Sum of odd numbers from 1 to {N} = {total}")


if __name__ == "__main__":
    main()
