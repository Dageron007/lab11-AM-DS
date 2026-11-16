"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
# https://github.com/Dageron007/lab11-AM-DS
# Partner 1: Danila Sterlev
# Partner 2: Anthony Mitromaras

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid arguments for logarithm.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b
