"""Read an array and print its maximum and minimum elements."""

# Get user input (input is always a string)
n = int(input("Enter the size of the array: "))

# Get the array elements as a list of integers
arr = list(map(int, input("Enter the array elements: ").split()))

# Initialize min and max with the first element of the array
min = max = arr[0]

# Iterate through the array to find the minimum and maximum elements
for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
# Print the minimum and maximum elements
print(f"Maximum element is {max}, Minimum element is {min}")
