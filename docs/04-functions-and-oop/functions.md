# Functions

**Status:** In Progress

### Overview
A function is a **named**, resuable block of code that does one specific task.  
We define the function once and call it as many times as required.

### 1. Defining a Function

We create a function using the keyword `def`, followed by the function name and parameters.  
To call a function, we write the name of the function and pass the arguments.

```python
#Syntax
def function_name(parameters):  # Defining the function
    body of function            # Statements of a function
    return                      # Returing the value

function_name(arguments)        # Calling a function
```
```python
#Example
def square(n):
    '''This function calculates the square of a number'''
    result = n * n
    return result

num = int(input)
print(square(num))
```
### 2. Docstrings
Docstring is a string written at the top of the function to explain what it does.  
Unlike a reglar # comment, a docstring is stored in python and can be read back at any time using `help()`

```python
#Example
def add(a,b):
    """ This function returns the sum of two numbers."""
    return a + b

help(add)
Help on function add in module __main__:

add(a, b)
    This function is used to add numbers.
~
 Help on add line 1/4 (END) (press h for help or q to quit)
```

### 3. Parameter & Arguments
Parameters are the variable names listed in the functions definition.  
Arguments are the actual values passed to the function when we call the function.

```python
#Example
def greet(greeting, name):          # here greeting and name are parameters
    print(greeting + ", " + name)

greeting("Hello", "Alice")          # here values "Hello" and "Alice" are arguments.

#Output: Hello, Alice
```

#### Types of Arguments
1. **Positional Arguments:** These arguments are passed in the correct order so they are mapped to function parameters in the same order.
```python
#Example
def bio_data(name,age):
    print(f"Name: {name}, Age: {age}")

bio_data("Sam", 22)

# Values of name and age are passed in same order as defined in function

#Output: Name: Sam, Age: 22
```
If we change the position of the argument, syntatically it will work but the outcome is not desired.
```python
bio_data(22, "Sam")

#Output: Name: 22, Age: Sam
```

2. **Keyword Arguments:** Parameter names (variable names) are explictly written when passing the argument values when calling the function. With this approach, the order in which arguments are passed does not matter - Only the variable names must match.
```python
#Example
def bio_data(name,age):
    print(f"Name: {name}, Age: {age}")

bio_data(age=25,name='Thomas')

#Output: Name: Thomas, Age: 25
```

#### Default Arguments
- Function arguments can have default values in python.
- We can provide a default value to an argument by using the assignment operator (=)

```python
def calculate_total(amount, discount_percentage = 0):
    discount_amount = discount_percentage / 100 * amount
    return amount - discount_amount

amount = 500
total_bill_amount = calculate_total(amount, 10)
print(total_bill_amount)
#Output: 450.0

amount = 500
total_bill_amount = calculate_total(amount)
print(total_bill_amount)
#Output: 500.0
```

**Note:** non-default arguments should always be towards left and default arguments should be towards right.  
**Note:** positional arguments should be always towards left and keyword arguments should be towards right.


### 4. Return
- A function can send back a result using the `return` statement.  
- If the `retuen` is not defined, the function returns `None` value. It is also not mandatory to add `return` in the function.
- Return also **immediately stops** the function - any code written after this is not executed. 
- We can also return multiple values from a function.

```python
# Example: Returning single value
def multiply(a,b):
    return a * b

print(multiply(100,5))

#Output: 500
```
```python
#Example : Returning two values
def add_div(a,b):
    add = a + b
    div = a / b
    return add, div

x1, x2 = add_div(10,5)
print(x1,x2)

#Output: 15 2.0
```

### 5. Scope of a Variable
A variable can be defined either inside or outside a function which determines its scope.

- **Local Scope:** Parameters and variables defined inside a function is not visible from outside. Hence they have a local scope. Once the function exits, they are erased from the memory.

```python
#Example: Local scope
def add(a,b):
    total = a + b
    print("Total inside = ", total)

add(4,9)
#Output: Total inside =  13

print("Total outside = ", total)
#Output: NameError: name 'total' is not defined
```

- **Global scope:** Variables defined outside the function are visible and accessible from inside as well as outside a function. Such variable values can be read from inside a function, but they cannot be updated. We need to add keyword `global` if we want to update the global variables.

```python
#Example: Global scope
total = 0
def add(a,b):
    total = a + b
    print("Total inside = ", total)

add(4,9)
#Output: Total inside = 13

print("Total outside = ", total)
#Output: Total outside = 0
```
We can define the variable as global with the `global` keyword. Now the variable can be updated from inside and outside the function.

```python
#Example: Global variable
total = 0
def add(a,b):
    total = a + b
    print("Total inside = ", total)

add(4,9)
#Output: Total inside = 13

print("Total outside = ", total)
#Output: Total outside = 13
```

### 6. Arbitary Arguments
"Arbitary" means we dont know how many arguments will be passed in advance. Python gives two special variants for this.

**1. \*args - any number of positional arguments**
```python
def greet(*args):
    for name in args:
        print("Hello, " + name)

greet("Alice", "Bob", "Charlie")

#Output: Hello, Alice
#Output: Hello, Bob
#Output: Hello, Charlie
```
The **\*** tells the python: Collect all positional arguments into a **`tuple`**

**2. \*\*kwargs - any number of keyword arguments**
```python
def profile(**kwargs):
    for key, value in kwargs.item():
        print(f"{key}:{value}")

profile(name="Alice", age=25, city="Mumbai")

#Output: name: Alice
#Output: age: 25
#Output: city: Mumbai
```
The **\*\*** tells the python : Collect all keyword arguments into a **`dictionary`**. Keys are the argument names and values are what we passed.

```python
# Using both together
def order(*items, **options):
    print("Items:", items)      # tuple
    print("Options:", options)  # dict

order("pizza", "soda", size="large", spicy=True)

#Output: Items: ("pizza","soda")
#Output: Options: {'size':'large','spicy': True}
```
Rule: **\*args** must come before **\*\*kwargs**


### 7. Lambda Function
A lambda is just a tiny, one-line function that doesn't needa a `def` or a name. You write it where you need it, use it once and its gone.
```python
# Syntax
lambda <inputs>: <one expression>
```

```python
# Normal function
def double(x):
    return x * 2

# Lambda function
double = lambda x: x * 2
```

**Key Rule**
- **One expression only** - no` if/else` blocks, no loops, no multiple lines.
- **No name** - You can assign one, but that defeats the point.
- **Short-lived** - best for quick throwaway logic, for anything complex, just write a normal `def`

```python
#Example 1: Add two numbers
add = lambda a,b: a + b
print(add(2,3))
#Output: 5

#Example 2: With a default
greet = lambda name = "World": "Hello ", + name
print(greet())
#Output: Hello World

print(greet("Alice"))
#Output: Hello Alice
``` 

### Related
