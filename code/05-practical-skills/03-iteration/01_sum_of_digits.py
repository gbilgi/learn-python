# Problem: Sum of digits
# Topic:   03 - Iteration


def digit_sum(n: int) -> int:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def main():
    number = 4721
    print(f"Sum of digits of {number} = {digit_sum(number)}")


if __name__ == "__main__":
    main()