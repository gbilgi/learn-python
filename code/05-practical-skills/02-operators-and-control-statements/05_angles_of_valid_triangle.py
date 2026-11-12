# Problem: Angles of valid triangle
# Topic:   02 - Operators and Control Statements


def main():
    # Get the angles of the triangle from the user
    angle1 = int(input("Enter the first angle of the triangle: "))
    angle2 = int(input("Enter the second angle of the triangle: "))
    angle3 = int(input("Enter the third angle of the triangle: "))

    # Check if the angles form a valid triangle
    if angle1 + angle2 + angle3 == 180:
        print("The angles form a valid triangle.")
    else:
        print("The angles do not form a valid triangle.")

if __name__ == "__main__":
    main()
