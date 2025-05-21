# Simple Calculator Program
# This program takes two numbers as input and performs basic arithmetic operations.

# Get user input for two numbers
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

# Perform addition
add = n1 + n2

# Perform subtraction (always positive result)
if n1 > n2:
    sub = n1 - n2
else:
    sub = n2 - n1

# Perform multiplication
mul = n1 * n2

# Perform division (handle division by zero)
if n2 != 0:
    div = n1 / n2
else:
    div = "Undefined (division by zero)"

# Display the results
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
# End of program