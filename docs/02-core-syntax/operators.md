# Operators in Python

**Status:** In Progress 

## Overview
An operator in a programming language is a symbol that performs specific mathematical, relational or logical operation and *produces a final result*.

An expression consists of **operators** and **operands**  
`operators` + `operands` = `expression`

## 1. Arithmetic Operators
Arithmetic operators are used to perform mathematical operations like 

1. Addition (+) : Performs addition
2. Subtraction (-) : Performs subtraction
3. Multiplication (*) : Performs multiplication
4. Division (/) : Performs division and the result is always retured as decimal number.
5. Modulo (%) : Performs the division and returns the reminder.
6. Floor Division (//) : Performs divisiom and the result is floored to nearest smaller integer.
7. Power (**) : Poerforms power of function

### BODMAS Rule
In Python, BODMAS rule is used to determine the order of operations for mathematical expressions.

- Brackets (): Have the highest precedence and are evaluated first.
- Division (/) and Multiplication (*): Have equal precedence and are evaluated from left to right.
- Addition (+) and Subtraction (-): Have equal precedence and are evaluated from left to right.

## 2. Comparison Operators
These operators are used to perform comparison and the result is always a boolean: **True** or **False**

|Operator|Name|Example|
|-----|-----|-----|
| == | Is Equal To | 3 == 5 gives us **False** |
| != | Not Equal To | 3 != 5 gives us **True** |
| > | Greater Than | 3 > 5 gives us **False** |
| < | Less Than | 3 < 5 gives us **True**|
| >= | Greater Than or Equal To | 3 >= 5 gives us **False** |
| <= | Lesser Than or Equal To | 3 <= 5 gives us **True**|

## 3. Assignment Operators
These operators are used to assign value to the variables.

|Operator|Name|Example|
|-----|-----|-----|
| = | Assignment Operator | a = 7 |
| += | Addition Assignment | a += 1 #a = a + 1 |
| -= | Subtraction Assignment| a -= 2 #a = a - 2 |
| *= | Multiplication Assignment | a *= 4 #a = a * 4 |
| /= | Division Assignment | a /= 5 #a = a / 5 |
| %= | Reminder Assignment | a %= 6 #a = a % 6 |
| **= | Exponent Assignment | a **= 7 #a = a ** 7 |

## 4. Logical Operators
These operations are used to check whether the expression is True or False. They are used to evaluate conditions in decision-making.

|Operator|Name|Example|
|-----|-----|-----|
| and | a **and** b | True only of both the operands are True |
| or | a **or** b | True if atleast one of operands is True |
| not | not **a** | True if the operant is False and vice-versa |

## 5. Special Operators
There are two special operators **"is"** and **"in"**

1. Identity Operator (**is**)
It tells you if both the objects are at the same memory location.

2. Membership Operator (**in**)
It tells you if an object is part of another object or not.

## Related