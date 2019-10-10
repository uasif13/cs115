from cs115 import *
import math

def inverse(n):
    return 1.0/n

def multiply(a,b):
    return a*b

def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(multiply, range(1,n+1))


def e(n):
    factorials = map(factorial, range(0,n+1))
    inverses = map(inverse, factorials)
    return sum(inverses)

def error(n):
    return math.e - e(n)
