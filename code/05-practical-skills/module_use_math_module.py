"""
This program demonstrates the use of a custom math module.
It imports the module_math_operation module and uses its functions to perform basic mathematical operations.
The program performs addition, subtraction, multiplication, and division using the functions defined in the module.
It also prints the value of PI defined in the module.
The module_math_operation module contains functions for addition, subtraction, multiplication, and division, as well"""

import module_math_operation

result_add = module_math_operation.add(5, 3)
result_subtract = module_math_operation.subtract(10, 4)
result_multiply = module_math_operation.multiply(2, 6)
result_divide = module_math_operation.divide(15, 3)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")
print(f"Value of PI: {module_math_operation.PI}")