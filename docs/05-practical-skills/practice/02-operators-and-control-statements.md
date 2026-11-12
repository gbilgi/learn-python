# 02 - Operators and Control Statements

Practice problems for **Operators and Control Statements**. Each problem has the statement, the expected output, and a working solution. The solution is included straight from `code/05-practical-skills/02-operators-and-control-statements/`, so the code shown here is the code that was run.


## Problem 01: Even and odd

**Difficulty:** Easy | **Tags:** 

### Problem statement
Write a program to input an integer from user and print if its Even or Odd.

### Sample input
```text
One line containing an integer N.
5
1000
```

### Expected output
```text
5 is odd.
1000 is even.
```

### Solution
```python title="01_even_and_odd.py"
--8<-- "code/05-practical-skills/02-operators-and-control-statements/01_even_and_odd.py"
```

### Approach and notes
- Idea: The program uses the modulo operator (%) to check if a user-entered number divides evenly by 2, printing whether it is even or odd.
- Time / space complexity:
- Gotchas:

## Problem 02: Max of two

**Difficulty:** Easy | **Tags:** 

### Problem statement
Write a program to input two numbers(A & B) from user and print the maximum element among A & B.

### Sample input
```text
First line is a single integer A. Second line is a single integer B.
50
6
```

### Expected output
```text
50 is greater than 6.
```

### Solution
```python title="02_max_of_two.py"
--8<-- "code/05-practical-skills/02-operators-and-control-statements/02_max_of_two.py"
```

### Approach and notes
- Idea: The program uses if-elif-else conditional statements and comparison operators (>, <) to compare two user-entered numbers and print which one is greater or if they are equal.
- Time / space complexity:
- Gotchas:

## Problem 03: Coding rating

**Difficulty:** Easy | **Tags:** 

### Problem statement
Write a program to input from user an integer(n) representing the rating of a person on a platform. You have to print the category of that person.

If the rating is greater than or equal to 2000 then that person is "grand master".  
If the rating is greater than or equal to 1700 then that person is "candidate master".  
If the rating is greater than or equal to 1500 then that person is "expert".  
If the rating is greater than or equal to 1300 then that person is "pupil".  
If the rating is smaller than 1000 then that person is "newbie".

NOTE: Print all the chars of the category of the person in lowercase if rating is odd otherwise print in UPPERCASE

### Sample input
```text
One line containing an integer N.
1651
2100
```

### Expected output
```text
expert
GRAND MASTER
```

### Solution
```python title="03_coding_rating.py"
--8<-- "code/05-practical-skills/02-operators-and-control-statements/03_coding_rating.py"
```

### Approach and notes
- Idea: The program uses nested if-elif-else statements to classify a user's coding rating into a skill tier, printing the title in ALL CAPS if the rating is even and in lowercase if it is odd.
- Time / space complexity:
- Gotchas:

## Problem 04: Max of three

**Difficulty:** Easy | **Tags:** 

### Problem statement
Write a program to input three numbers(A, B & C) from user and print the maximum element among A, B & C in each line.

### Sample input
```text
First line is a single integer A.
Second line is a single integer B.
Third line is a single integer C.
```

### Expected output
```text
One line answer.
```

### Solution
```python title="04_max_of_three.py"
--8<-- "code/05-practical-skills/02-operators-and-control-statements/04_max_of_three.py"
```

### Approach and notes
- Idea: The program sets the first number as a running maximum and sequentially updates it using if statements whenever a larger number is found among the remaining inputs.
- Time / space complexity:
- Gotchas:

## Problem 05: Angles of valid triangle

**Difficulty:** Easy | **Tags:** 

### Problem statement
You are given 3 integer angles(in degrees) A, B and C of a triangle. You have to tell whether the triangle is valid or not.
A triangle is valid if sum of its angles equals to 180.

### Sample input
```text
First line of the input contains an integer A.
Second line of the input contains an integer B.
Third line of the input contains an integer C.
```

### Expected output
```text
(paste the real output here)
```

### Solution
```python title="05_angles_of_valid_triangle.py"
--8<-- "code/05-practical-skills/02-operators-and-control-statements/05_angles_of_valid_triangle.py"
```

### Approach and notes
- Idea: The program sums three user-entered angles and uses an if-else statement to check if the total equals 180 degrees, determining whether they form a valid triangle.
- Time / space complexity:
- Gotchas:
