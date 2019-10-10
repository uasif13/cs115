'''
Created on 9/13/19
@author:   Asif Uddin
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
#from dict import *

# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)




# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
             'spam', 'spammy', 'zzyzva']


# Implement your functions here.
# What I need:
# function that takes checks a string in a rack

def letterScore(letter, scorelist):
    '''Returns the score of a letter from scrabbleScores'''
    if (scorelist[0][0] == letter): return scorelist[0][1]
    else: return letterScore(letter, scorelist[1:])

def wordScore(S,scorelist):
    '''Returns the score of a word'''
    if S == '': return 0
    else: return letterScore(S[0],scorelist) + wordScore(S[1:],scorelist)

def listScore(L,scorelist):
    '''Returns an array of the word and its scrabble score'''
    if L == []: return []
    else: return [[L[0],wordScore(L[0],scorelist)]] + listScore(L[1:],scorelist)

def removeletter(e,L):
    '''Removes the letter inside the rack'''
    if e == L[0]: return L[1:]
    else: return [L[0]]+removeletter(e,L[1:])

def insideRack(S,Rack):
    '''Checking whether a word can be made from the rack'''
    if S == '': return True
    elif S[0] in Rack: return insideRack(S[1:],removeletter(S[0],Rack))
    else: return False

def wordstocheck(L,Rack):
    '''Returns the words from the dictionary inside the rack'''
    if L == []: return []
    if insideRack(L[0],Rack): return [L[0]] + wordstocheck(L[1:],Rack)
    else: return wordstocheck(L[1:],Rack)

def scoreList(Rack):
    '''Returns the list of stuff inside the rack'''
    return listScore(wordstocheck(Dictionary,Rack),scrabbleScores)

def maxWord(L):
    '''Returns word with maximum score from list'''
    if len(L) == 0: return ['',0]
    if len(L) == 1: return L[0]
    if len(L) == 2:
        if L[0][1] > L[1][1]: return L[0]
        else: return L[1]
    else:
        if L[0][1] > L[1][1]: return maxWord([L[0]]+L[2:])
        else: return maxWord(L[1:])
    
def bestWord(Rack):
    '''Returns the word with the maximum score'''
    return maxWord(scoreList(Rack))







