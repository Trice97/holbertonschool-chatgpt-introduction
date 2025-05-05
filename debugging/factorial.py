#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémentation de n à chaque tour
    return result

f = factorial(int(sys.argv[1]))
print(f)

