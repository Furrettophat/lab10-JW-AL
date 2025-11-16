"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://docs.google.com/document/d/17mvLUx1jLvktsB2fbov1l4P5_C3fEM9ayaUcBbuAtLc/edit?tab=t.0
import math

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    math.log(b, a)

def exponent(a, b):
    return a ** b


