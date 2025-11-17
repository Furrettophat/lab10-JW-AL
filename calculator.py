#https://github.com/Furrettophat/lab10-JW-AL
#Partner 1: John Weed
#Partner 2: Ashton Lakey

import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
    
def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except ValueError:
        return

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def subtract(a, b): 
    return a - b

def exp(a, b):
    return a**b

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    math.log(b, a)



