# Loops in Python

**Status:** In Progress

### Overview
Loops are used in programming to repeat a specific block of code.  
Loops utilize the DRY principle - **Dont Repeat Yourself**. Even repeating 2 times is not good in programming.

Following steps are used when repeating a task.  
- Step1: Initialization  
- Step2: Condition  
- Step3: Action  
- Step4: Updation  

### 1. While Loops
The while loop is used to iterate over a block of code as long as the condition is true.

```python
# Syntax
variable initialization  # Step1
while condition:         # Step2
      action             # Step3
      updation           # Step4
```
```python
# Printing 5 numners
i = 1
while i <= 5:
    print(i)
    i += 1
#Output: 1, 2, 3 ,4 ,5
```
Infinite Loop: Always ensure, we have all the four steps defined. Missing step4 to update the variable may result in condition being in true state for ever and results in infinite loop.


#### **Break**  
Whenever we execute the break statement inside a loop, it terminates the loop.

```python
# Example
count = 1
while count <= 10:
    if count == 3:
        break
    print(count)
    count += 1

#Output: 1, 2
```

#### **Continue**  
It skips the current execution of the loop & control of loop moves to next iteration of loop. 

```python
#Example
count = 1
while count <= 10:
    count += 1
    if count == 3:
        continue
    print(count)

#Output: 2, 4, 5, 6, 7, 8, 9, 10, 11
```

### 2. Range Function
We can generate a sequence of numbers using the `range()` function.

We can define the *start*, *end*, *step size*  while defiing the range function.
`range(start,end,step-size)`

Step size defaults to 1 if not defined. Steps towards right by default.


#### **range(end)**
It generates no's from [0 to end). Note the end will not be included, it will be end - 1.

```python
# Example
range(4)
#Output: 0, 1, 2, 3
```

#### **range(start,end)**
It generates no's from start to end - 1. Default step size is 1 towards right.

```python
# Example
range(2,6)
#Output: 2, 3, 4, 5

range(-1,-5)
#Output: None  # Default step is towards right from start postion.

range(-5,-1)
#Output: -5, -4, -3, -2
```

#### **range(start,end,step-size)**
It generates from start to end - 1 with a step size and direction as defined.

```python
# Example
range(2,8,2)
#Output: 2, 4, 6

range(-1,-5,-1)
#Output: -1, -2, -3, -4

range(-5,-1,-1)
#Output: None  # Step is towards left from start postion.
```



### 3. For Loop
For loop iterate over a given sequence.

#### **Iterable**
Group of objects on which iterations are possible. Ex: `range()` is an iterable.

#### **Iterator**
Object used to extract iterables one by one. Ex: for loop is an iterator.

```python
# Syntax
for val in sequence:
    Body of for
```
- Here `val` is the variable that takes the value of the item inside the sequence on each iteration.  
- Loop continues until we reach the last item in the sequence.  
- The body of the loop is seperated from the rest of the code using indentation.  
- With loop we can skip initialization, condition and updation.  

```python
# Example
for i in range(10):
    print(i)

#Output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

```python
# Example
for i in range(0,1):
    print("Hello")

#Output: Hello
```
```python
# Printing odd numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i,end=" ")

#Output: 1, 3, 5, 7, 9
```

#### **Using _ (underscore) as variable**  
Many programmers use _ (underscore) as a variable name when they don't want to use variable in loop.

```python
# Example
for _ in range(0,1):
    print("Hello")
```

If we use _, it won't give a warning in case we are not using it. With any other variable name, it gives warning.

#### **Pass Statement**  
The pass does nothing. It signifies that the programmer will later add some code to it. Right now it ignores this block. It does not skip iteration like continue.

```python
# Example
for i in range(6):
    if i % 2 == 0:
        pass
    print("i")
```


## Related
- For loop is used in simpler senarios, because we have less control.
- While loop is mostly used in complex scenarios as we have full control with initialization, condition, action and updation.
