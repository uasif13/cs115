# Author: Asif Uddin
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Date: September 12, 2019

def dot(L,K):
    '''Returns the dot product of two lists'''
    if L != [] and K != []: return L[0]*K[0] + dot(L[1:],K[1:])
    else: return 0 

def explode(S):
    '''Returns a list of all the characters in the string'''
    if S == "": return []
    else: return [S[0]] + explode(S[1:])

def ind(e,L):
    '''returns the index value of an element in a list'''
    if L == [] or L == '': return 0
    if e == L[0]: return 0
    else: return 1 + ind(e,L[1:])

def removeAll(e,L):
    '''Removes all instances of an element from a list'''
    if L == []: return []
    if e == L[0]: return removeAll(e,L[1:])
    else: return [L[0]] + removeAll(e,L[1:])

def myFilter(function,L):
    '''Applies a function to a list and returns a list of the true values'''
    if L == []: return []
    if function(L[0]) == True: return [L[0]] + myFilter(function,L[1:])
    else: return myFilter(function,L[1:])
    
def deepReverse(L):
    '''Reverses all elements in a list including within lists of lists'''
    if L == []: return []
    if isinstance(L[0],list): return deepReverse(L[1:]) + [deepReverse(L[0])]
    else: return deepReverse(L[1:]) + [L[0]]
    
