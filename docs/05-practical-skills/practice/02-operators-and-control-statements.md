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
