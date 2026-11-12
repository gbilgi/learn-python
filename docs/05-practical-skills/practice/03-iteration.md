# 03 - Iteration: Loops & Iteration Analysis

Practice problems for **Iteration: Loops & Iteration Analysis**. Each problem has the statement, the expected output, and a working solution. The solution is included straight from `code/05-practical-skills/03-iteration/`, so the code shown here is the code that was run.


## Problem 01: Sum of digits

**Difficulty:** Easy | **Tags:** 

### Problem statement
Describe the task in your own words, with any constraints.

### Sample input
```text
(none)
```

### Expected output
```text
(paste the real output here)
```

### Solution
```python title="01_sum_of_digits.py"
--8<-- "code/05-practical-skills/03-iteration/01_sum_of_digits.py"
```

### Approach and notes
- Idea:
- Time / space complexity:
- Gotchas:

## Problem 02: Sum of odds

**Difficulty:** Easy | **Tags:** 

### Problem statement
Take an integer N as input. You have to print the sum of all odd numbers in the range [1, N].

### Sample input
```text
A single positive integer N.
```

### Expected output
```text
Print the required sum in a single line.
```

### Solution
```python title="02_sum_of_odds.py"
--8<-- "code/05-practical-skills/03-iteration/02_sum_of_odds.py"
```

### Approach and notes
- Idea: The program uses a for loop with a step of 2 (range(1, N + 1, 2)) to iterate directly over all odd numbers from 1 to N and accumulate their sum.
- Time / space complexity:
- Gotchas:

## Problem 03: From top to down

**Difficulty:** Easy | **Tags:** 

### Problem statement
Write a program that takes a positive integer N as input from the user and prints all natural numbers from N to 1, with each number followed by a space (including the last number).

### Sample input
```text
A single line representing N
```

### Expected output
```text
Space separated integers from N to 1, with each number followed by a space, including the last number.
```

### Solution
```python title="03_from_top_to_down.py"
--8<-- "code/05-practical-skills/03-iteration/03_from_top_to_down.py"
```

### Approach and notes
- Idea: The program uses a for loop with a negative step (range(N, 0, -1)) to count backward from N down to 1 and print each number.
- Time / space complexity:
- Gotchas:

## Problem 04: From down to top

**Difficulty:** Easy | **Tags:** 

### Problem statement
Write a program to print all Natural numbers from 1 to N where you have to take N as input from user

### Sample input
```text
A single line representing N
```

### Expected output
```text
Space separated integers from 1 to N.
```

### Solution
```python title="04_from_down_to_top.py"
--8<-- "code/05-practical-skills/03-iteration/04_from_down_to_top.py"
```

### Approach and notes
- Idea: The program uses a for loop with range(1, N + 1) and end=' ' in print() to display all integers from 1 to N on a single space-separated line.
- Time / space complexity:
- Gotchas:

## Problem 05: Sum of evens

**Difficulty:** Easy | **Tags:** 

### Problem statement
You are given a positive integer A. You have to print the sum of all even numbers in the range [1, A].

### Sample input
```text
First and only line contains a single positive integer A.
```

### Expected output
```text
Print the required sum in a single line.
```

### Solution
```python title="05_sum_of_evens.py"
--8<-- "code/05-practical-skills/03-iteration/05_sum_of_evens.py"
```

### Approach and notes
- Idea: The program iterates from 1 to N using a for loop and checks each number with the modulo operator (%) to accumulate the sum of all even numbers.
- Time / space complexity:
- Gotchas:

## Problem 06: Multiples of 4

**Difficulty:** Easy | **Tags:** 

### Problem statement
Given an integer input N, print all multiples of 4 less than or equal to N.

### Sample input
```text
Single line containing an integer N.
```

### Expected output
```text
Space separated integers representing multiples of 4 less than or equal to N.
```

### Solution
```python title="06_multiples_of_4.py"
--8<-- "code/05-practical-skills/03-iteration/06_multiples_of_4.py"
```

### Approach and notes
- Idea: The program loops from 1 to N using a for loop and checks each number with the modulo operator (% 4 == 0) to print all multiples of 4 on a single line.
- Time / space complexity:
- Gotchas:

## Problem 07: Multiplication table

**Difficulty:** Easy | **Tags:** 

### Problem statement
Take a number N as input, print its multiplication table having the first 10 multiples.

### Sample input
```text
First line contains a single integer N.
```

### Expected output
```text
Print 10 lines containing the multiples.
```

### Solution
```python title="07_multiplication_table.py"
--8<-- "code/05-practical-skills/03-iteration/07_multiplication_table.py"
```

### Approach and notes
- Idea: The program uses a for loop with range(1, 11) and width-aligned f-strings ({i:2}) to print a neatly formatted multiplication table.
- Time / space complexity:
- Gotchas:

## Problem 08: Print perfect squares

**Difficulty:** Easy | **Tags:** 

### Problem statement
Take an input of a number N from the user. Print all perfect squares less than or equal to N.

### Sample input
```text
A single line consisting of a integer N.
```

### Expected output
```text
Print perfect squares less than or equal to N in a single line in a space-separated manner.
```

### Solution
```python title="08_print_perfect_squares.py"
--8<-- "code/05-practical-skills/03-iteration/08_print_perfect_squares.py"
```

### Approach and notes
- Idea: The program uses a for loop to compute consecutive squares (i * i) and a break statement to stop early as soon as a square exceeds N, printing all perfect squares up to N.
- Time / space complexity:
- Gotchas:
