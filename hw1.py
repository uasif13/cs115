# Author: Asif Uddin
# Pledge: I honor that I have abided by the Stevens Honor System.
# Date: 9/11/19

# Import map and reduce functions from cs115.py
from cs115 import reduce,map

def multi(x,y):
    return x * y

def add(x,y):
    return x+y

'''factorial function'''

def factorial(n):
    '''Returns n!'''
    if n > 0:
        return reduce(multi,range(1,n+1))
    else:
        print ("Please input a positive number")

'''mean function'''

def mean(L):
    '''Returns the mean of a list of a numbers'''
    return reduce(add,L)/len(L)


def divides(n):
    def div(k):
        return n % k == 0
    return div

'''prime function'''

def prime(n):
    '''Returns true if n is a prime number and false if n is not a prime number
        Checks values from 2 to the square root of the number plus one
    '''
    return sum((map(divides(n),(range(2,int(n**0.5+1)))))) == 0 and n > 1
