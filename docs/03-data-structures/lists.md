# Lists

**In Progress 

### Overview
A list is an ordered, mutable (changeable) collection that can hold items of any type — numbers, strings, even other lists.

`shopping = ["milk", "bread", 3, 4.5]`

Key Properties
- **Ordered:** Elements have a defined sequence with indices.
- **Mutable:** You can modify the list by adding, removing, or changing items.
- **Heterogeneous:** Can contain different data types, unlike arrays in some languages.

Lists are like arrays but are more flexible due to their dynamic size and mixed data capabilities.

### 1. List Creation

1. Literal creation:  
    `colors = ["red","green","blue"]`

2. Using the list:  
    `numbers = list(range(10))   # [0,1,2,....,9]`  
    `sequence = list((1,2,3))`  
    `name = list("Sam")`


### 2. Indexing
Python counts from 0. Negative indices count from the end (-1 = last).

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])    # "apple"   (first)
print(fruits[1])    # "banana"  (second)
print(fruits[-1])   # "date"    (last)
print(fruits[-2])   # "cherry"  (second last)   
```
### 3. Slicing
Slicing is a way to get a portion (a sub-sequence) of a list, without copying the entire thing. It creates a new list — the original is not modified.

Syntax: `sequence[start : stop : step]`

```python
# Examples:
nums = [10, 20, 30, 40, 50, 60]

nums[1:4]    # [20, 30, 40] from index 1 to 4 (end not included)
nums[:3]     # [10, 20, 30] from start to index 3 (not included)
nums[3:]     # [40, 50, 60] from index 3 to end (end is included)
nums[::2]    # [10, 30, 50] start to end, step of 2 (end included)
nums[::-1]   # [60, 50, 40, 30, 20, 10] reversed (end included)
nums[:100]   # [10, 20, 30, 40, 50, 60] - out of range - no error
```

### 4. Updating a List
Since lists are mutable, you can change their contents after creation. There are two ways:

1. Change a single item (by index)
```python
fruits = ["apple", "banana", "cherry"]

fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'cherry']   
```
You're simply assigning a new value to an existing index.

2. Replace a slice (multiple items at once)
```python
nums = [10, 20, 30, 40, 50]

nums[1:4] = [99, 88, 77]
print(nums)  # [10, 99, 88, 77, 50]   
```
You're replacing the slice nums[1:4] (which was [20, 30, 40]) with a new list.  
The replacement list doesn't have to be the same length:
```python
nums = [10, 20, 30, 40, 50]

nums[1:3] = [99, 88, 77, 66]   # replacing 2 items with 4
print(nums)  # [10, 99, 88, 77, 66, 40, 50]

nums[1:3] = []                  # replacing 2 items with nothing (deletes them)
print(nums)  # [10, 77, 66, 40, 50]   
```
**In short:** `list[i] = value` changes one item. `list[a:b] = [new values`] replaces a chunk — and can even grow or shrink the list.

### 5. Iteration over a List
Iteration means going through each element of a list one by one. Python makes this easy with the for loop.



## 6. 2-D Lists

Explain in your own words, then add a short example and its output.

## 7. Iteration in 2D List

Explain in your own words, then add a short example and its output.

## 8. List Comprehension

Explain in your own words, then add a short example and its output.

## Common mistakes / gotchas
- 

## Practice
- [ ] 

## Related
- 



