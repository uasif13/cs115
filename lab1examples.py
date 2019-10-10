from cs115 import *

#This is a comment! Use these at the top of your file for the name and pledge
#I pledge my honor that I have abided by the Stevens Honor System

def myDoubleFunction(arg1, arg2):
    """This is a docstring! They are enclosed in triple " or '. They can be one
    line or multiple lines. They are used to describe what the function does in
    English so humans can quickly understand your code. For example: This function
    doubles the value of each argument and adds the results together"""
    return 2 * (arg1 + arg2) #comments can also be used at the end of a line of code to explain

def span(lst):
    """returns the difference between the min and max elements in a list"""
    return reduce(max, lst) - reduce(min, lst)

def span1(lst):
    """returns the difference between the min and max elements in a list"""
    return max(lst) - min(lst)

def gauss(N):
    """takes a positive int N and returns the sum 1+2+...+N"""
    def add(a, b):
        return a + b
    return reduce(add, range(N+1))

def gauss1(N):
    """takes a positive int N and returns the sum 1+2+...+N"""
    return sum(range(N+1))

def sumOfSquares(N):
    """takes a positive int N and returns the sum 1^2+2^2+...+N^2"""
    def add(a, b):
        return a + b
    def square(n):
        return n**2
    squares = map(square, range(N+1))
    return reduce(add, squares)
    
def sumOfSquares1(N):
    """takes a positive int N and returns the sum 1^2+2^2+...+N^2"""
    def square(n):
        return n**2
    squares = map(square, range(N+1))
    return sum(squares)

