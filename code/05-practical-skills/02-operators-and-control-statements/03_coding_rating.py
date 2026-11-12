# Problem: Coding rating
# Topic:   02 - Operators and Control Statements


def main():
    # Gather input
    N = int(input("Enter your coding rating: "))

    # Step 1: Determine the title once
    if N >= 2000:
        title = "grand master"
    elif N >= 1700:
        title = "candidate master"
    elif N >= 1500:
        title = "expert"
    elif N >= 1300:
        title = "pupil"
    else:
        title = "newbie"

    # Step 2: Convert to uppercase if the rating is even
    if N % 2 == 0:
        title = title.upper()

    print(f"You are a {title}.")

if __name__ == "__main__":
    main()
