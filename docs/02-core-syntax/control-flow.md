# Control Flow

**Status:** In Progress

## Overview
Decision making is required when we want to execute a code only if a certain condition is satisfied.

- In Python, the body of if statement is indicated by the indentation.
- Body starts with an indentation and the first unindented line marks the end.

## 1. If Statement
Executes block if condition is True.

```python
# Syntax
if expression:
    Body of if
```
```python
# Example
number = 3
if number > 0:
    print("Its a Positive number")

print("This is always printed)
```
## 2. If Else Statement
- The if-else statement evaluates the expression and will execute the body of if only when result is True.
- If the condition is False, body of else is executed.
- Indentation is used to seperate the blocks.

```python
# Syntax
if expression:
    Body of if
else:
    Body of else
```
```python
# Example
number = 3
if number >= 0:
    print("Its a Positive number or Zero")
else:
    print("Its a Negative number")
```
## 3. If Elif & Else
- the elif is short for else-if. It allows us to check multiple conditions.
- If the condition for if is False, it checks the condition of the next **elif** block and so on.
- If all the condition are False, body if else is executed.
- Only one block among all the several if..elif..else blocks is executed according to the condition.
- The if can have only one else block. But it can have multiple elif blocks.

```python
# Syntax
if expression:
    Body of if
elif:
    Body of elif
elif:
    Body of elif
else:
    Body of else
```
```python
# Example
number = 3
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

## 4. Nested If Else
Conditional statements within other conditional statements.

```python
# Syntax
if expression:
    Body of 1st if
    if expression:
        Body of 2nd if
else:
    Body of else
```
```python
# Example
number = 3
if number > 0:
    print("Positive")
    if number < 0:
        print("Negative")
    else:
        print("Zero")
else:
    print("Invalid")
```

## Common mistakes / gotchas
- 

## Practice
- [ ] 

## Related
- 
