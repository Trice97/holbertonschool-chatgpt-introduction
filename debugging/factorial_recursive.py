#!/usr/bin/python3
import sys

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer n.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Check if the user has provided exactly one command-line argument
if len(sys.argv) != 2:
    print("Usage: ./factorial_recursive.py <non-negative_integer>")
    sys.exit(1)

# Convert the argument to an integer and validate it
try:
    number = int(sys.argv[1])
    if number < 0:
        raise ValueError("The number must be a non-negative integer.")
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)

# Call the factorial function and print the result
f = factorial(number)
print(f)

