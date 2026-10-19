# Operators in Python

**Status:** In Progress 

### Overview
An operator in a programming language is a symbol that performs specific mathematical, relational or logical operation and *produces a final result*.

An expression consists of **operators** and **operands**  
`operators` + `operands` = `expression`

Example: 5 + 3 = 8  
Here 5 & 3 are Operands, '+' is the Operator

### 1. Arithmetic Operators
Arithmetic operators are used to perform mathematical operations like 

1. Addition (+) : Performs addition
2. Subtraction (-) : Performs subtraction
3. Multiplication (*) : Performs multiplication
4. Division (/) : Performs division and the result is always retured as decimal number.  
5. Modulus (%) : Performs the division and returns the reminder.
6. Floor Division (//) : Performs division and the result is floored to nearest smaller integer.  
7. Power (**) : Performs power of function

```python
print(10 + 3)       # both operands int, result stays int.
13

print(10 / 3)       # both operands int, result stays float. 
3.333333333

print(10 // 3)      # both operands int, result stays int.
3

print(-8 // 3)      # both operands int, result stays int.
-3

print(10 % 3)       # both operands int, result stays int.
1

print(2 ** 0.5)     # mixed int/float ⇒ result is float. 
1.414213

print("Hi "*3)      # Python's neat trick. Multiplies the string n times.
Hi Hi Hi 

print("abc"+"def")  # Python concatenates the strings. Result type stays string.
abcdef

print(2.5 + True)   # booleans are treated as integers in arithmetic.
3.5

print("1" + 1)      # Python does NOT auto-convert. You must explicitly cast
TypeError: can only concatenate str (not "int") to str

print(5 + None)     # None has no arithmetic operations defined.
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

print("Hi " * 2.5)  # string multiplication only works with INTEGER counts.
TypeError: cant multiply sequence by non-int

print(int(3.25 // 1))   # floors to 3
3

print(-4.25 // 1)   # floors to -5.0
-5.0

print(5 // 1)       # floors to same number 5
5
```

#### BODMAS Rule
In Python, BODMAS rule is used to determine the order of operations for mathematical expressions.

- Parenthsis ( )
- Power (**)
- Multiply (*), Divide (/), Floor division(//), Modulus (%)
- Addition (+), Subtraction (-)
- Not equal (!=), Equal (==)
- <. <=, >, >= : Comparision Operators
- not, and, or

### 2. Comparison Operators
These operators are used to perform comparison and the result is always a boolean: **True** or **False**

|Operator|Name|Example|
|-----|-----|-----|
| == | Is Equal To | 3 == 5 gives us **False** |
| != | Not Equal To | 3 != 5 gives us **True** |
| > | Greater Than | 3 > 5 gives us **False** |
| < | Less Than | 3 < 5 gives us **True**|
| >= | Greater Than or Equal To | 3 >= 5 gives us **False** |
| <= | Lesser Than or Equal To | 3 <= 5 gives us **True**|

```python
2 == 2.0        # int and float ARE compatible. Python auto-converts the int to float, then compares the values numerically.
True

2 == "2"        # Python does NOT auto-convert between numbers and strings.
False

2 == None       # None is equal only to itself. Any other comparison with None for equality is False.
False

False == 0      # booleans are treated as integers:True = 1, False = 0
True

True == 1       # booleans are treated as integers:True = 1, False = 0
True

"ABC" == "abc"  # straightforward same-type comparison.
False

"abc" != "abd"  # straightforward same-type comparison.
True

2 < "2"         # int and str cannot be ordered. Python won't auto-convert. 
TypeError: '<' not supported between instances of 'int' and 'str'

2 < 2.0001      # int and float ARE compatible.
True

100 >= 32       # straightforward same-type comparison.
True

2 == 2.00001    # int and float ARE compatible.
False
```

### 3. Assignment Operators
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

### 4. Logical Operators
These operations are used to check whether the expression is True or False. They are used to evaluate conditions in decision-making.

|Operator|Name|Example|
|-----|-----|-----|
| and | a **and** b | **True** only of both the operands are True |
| or | a **or** b | **True** if atleast one of operands is True |
| not | not **a** | **True** if the operant is False and vice-versa |

Truth Table - AND operation
| A | B | A and B |
|--|--|--|
| True | True | **True** |
| True | False | **False** |
| False | True | **False** |
| False | False | **False** |

Truth Table - OR operation
| A | B | A or B |
|--|--|--|
| True | True | **True** |
| True | False | **True** |
| False | True | **True** |
| False | False | **False** |

Usecase 1: `if user is not None and user.is_admin` - never errors even when user is None.  
Usecase 2: `if file_exists(path) and read(path)` - only reads if the file exists.

### 5. Special Operators
There are two special operators **"is"** and **"in"**

1. Identity Operator (**is**)
It tells you if both the objects are at the same memory location.

2. Membership Operator (**in**)
It tells you if an object is part of another object or not.

### Related