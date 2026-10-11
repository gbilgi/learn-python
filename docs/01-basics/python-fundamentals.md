# Basic Fundamentals of Python

**Status:** In Progress

### 1. Print function

`print()` is a function to output the text to the console. When called it evaluates any expressions supplied to it and converts values into text to be displayed.

Statement for print:  
`print(*objects, sep=' ', end=' ')`

After every print operation of each object, by default Python adds a space for separation. Similarly, after each print operation is completed, the output gets to a new line (\n).

- objects (positional values): Accepts any number of comma separated values or expressions.
- sep (Separator): Defines what character or string is printed between multiple arguments. Default value is space.
- end (End-of-Line Character): Defines what character or string is printed at the very end after all values are printed. Default value is next line `\n`

```python
print('cats', 'dogs', 'mice')
#Output: cats dogs mice

#Comma-Separated
print('cats', 'dogs', 'mice', sep=',')
#Output: cats,dogs,mice

#Delimit with vertical bars
print('Mozilla', 'Firefox', 'Safar', sep='|')
#Output: Mozilla|Firefox|Safari

#Tab separated alignment
print('word', 'frequency', sep='\t')
#Output: word    frequency

#Controlling line ending
print('Hello', end=' ')
print('World')
#Output: Hello World

#printing values
print(1000, 500)
#Output: 1000 500

#printing expressions
print(500 + 200)
#Output: 700

#Mixed values
print("Ramesh is", 45, "years", "old")
#Output: Ramesh is 45 years old

#String Concatenation: Joining string together using + operator
print("Hello" + "World")
#Output: HelloWorld
```

### 2. Data Types

In Python, a data type is a category for values, and every value belongs to exactly one data type. Python is object-oriented: everything is an object including numbers, strings, data structures and functions.

Variables do not explicitly require type declarations. It uses **dynamic typing**, where variables automatically takes on the type of the object assigned to it.

#### Basic Types
1. Integers (`int`): Represents positive or negative numbers without a decimal. (-∞ to +∞) 
2. Floating-Point (`float`): Represents positive or negative numbers with floating point or decimal (-100.45, 567.76, 33.0).
3. Boolean (`bool`): A data type strictly representing `True` or `False`.
4. String (`str`): Sequence of text characters enclosed in quotes - single quote (' ') or double quotes (" ").
5. None: A special data type denoting no value, None Type.

#### Four Data Structure Types
1. List (`list`): Ordered, mutable collection (allows duplicates).
2. Tuple (`tuple`): Ordered, immutable collection.
3. Dictionary (`dict`): Ordered collection of key-value pairs (keys must be unique).
4. Sets (`set`):Unordered collection of unique items.

| Data Structure|Syntax | Ordered?| Mutable?| Duplicates?|
|:---|:--|:---|:---|:---|
| List |[item1], [item2] | Yes| Mutable| Yes|
| Tuple |(item1, item2) | Yes| Immutable| Yes|
| Dictionary |{key:value} | Unordered| Mutable| Keys:No, Values:Yes|
| Set |{item1}, {item2} | Unordered| Mutable| No|

_Mutable:_ Their contents can be modified, appended, or removed.  
_Immutable:_ Their contents cannot be altered once created. 

#### Inspecting Type with `type()`
To inspect the type of any value or variable at runtime, Python provides the built-in `type()` function.

```python
x = 42
y = 55.65
z = "Hello"

print(type(x))
print(type(y))
print(type(z))

#Output: <class 'int'>
#Output: <class 'float'>
#Output: <class 'str'>
```

### 3. Variables
A **variable** is a label that points to a memory location storing data. Python is dynamically typed, so we do not need to declare the variable type - the type is inferred from the assigned value, and it can be changed later.
The variable name is just a label/reference; the object carries the type.

#### Naming Rules
1. Must start with a letter or underscore ( a-z , A-Z , _ )
2. Cannot start with a digit
3. Can only contain alphanumeric (letters, numbers or underscore)
4. Names are case-sensitive
5. Cannot be an in-built keyword

Best practice: use snake_case for multi-word names. Eg: first_name, total_price

#### Assignment Patterns
```python
# Multiple variables, same value
x = y = z = 0

# Multiple variables, different values
a, b, c = 1, 2, 3
```

#### ID Function
The `id()` function returns a **unique integer** that identifies *where* the object lives in the memory for the lifetime of the object.
```python
a = 10
print(id(a)) #Output: Eg: 94300019145712
```

### 4. Python Comments
A comment is a text in the code that Python interpreter completely ignores. It starts with `#` and runs to the end of the line.

#### Single line comment

```python
# Calculate the area of triangle
area = math.pi * radius ** 2
```
Comments can also be used to disable a line of code
```python
#print("This line is disabled")
print("This line is enabled")
```
#### Multi-line comment
1. Approach 1
```python
# This is a block comment
# explaining a complex algorithm.
# Each line starts with #.
```
2. Approach 2
```python
"""
This is a multi-line block
using triple quotes.
It's ignored if not assigned to a variable.
"""
```

### 5. Input Function in Python
`input()` is a function to take user input. By default, the input is always stored as string.  
Key-point: The data entered by user (integer, float, sting) is always stored as string by default.

```python
name = input("Enter your Name: ")
print(name)
print(type(name))
# Output:
# Enter your Name: Sam
# Sam
# <class 'str'>
```
when we need to accept different data type, we need to convert it.
```python
age = int(input("What is your age: "))
print(age)
print(type(age))
# Output
# What is your age: 43
# 43
# <class 'int'>
```

### Related
**Python is case-sensitive:** Python treats _uppercase_ and _lowercase_ letters as different characters. So `Name`, `name`, and `NAME` are three completely different identifiers.

**Garbage Collector:** The Garbage Collector is Python's automatic memory management system — it frees memory occupied by objects that are no longer in use, so you never have to manually delete or manage memory.