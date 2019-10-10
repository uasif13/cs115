'''
Created on 25 September 2019
@author:   Asif Uddin
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here

def giveChange(amount, coins):
    '''Returns minimum number of coins and list of those coins'''
    min_val = change(amount,coins)
    if min_val == float("inf"): return [float("inf"),[]]
    else:
        coin_set = getCoins(min_val,coins,amount)
        return [min_val,coin_set]

def change(amount, coins):
    '''Returns the minimum number of coins from a given coin system to make a certain amount
       Returns infinity if not possible'''
    # base case of recursion
    if amount == 0: return 0
    # case where it is impossible to form the value with the given change
    if (amount < 0 or coins == []): return float("inf")
    # case where the coin value is greater than the amount
    if coins[0] > amount: return change(amount,coins[1:])
    # case where the coin value is less than the amount
    else:
        #first line is the case when you only need one of the first coin values
        #second line is the case where you need more
        #third line is the case where it is less but you don't need it
        one_time = change(amount-coins[0],coins[1:])
        multi_times = change(amount-coins[0],coins)
        no_times = change(amount,coins[1:])        
        return min(1+min(one_time, multi_times),no_times)

def getCoins(min_val,coins,amount):
    '''Gets the list of points to return'''
    if (min_val == 0 and amount == 0): return []
    if (amount < 0 or coins == []): return [float("inf")]
    if coins[0] > amount: return getCoins(min_val,coins[1:],amount)
    else:
        one_time = getCoins(min_val-1,coins[1:],amount - coins[0]) + [coins[0]]
        multi_times = getCoins(min_val-1,coins,amount - coins[0]) + [coins[0]]
        no_times = getCoins(min_val,coins[1:],amount)
        return min(one_time,multi_times,no_times)
        
    

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []: return []
    else: return [[dct[0],wordScore(dct[0],scores)]] + wordsWithScore(dct[1:],scores)  # your code goes here

    # how do i do this with map?

def letterScore(letter, scorelist):
    '''Returns the score of a letter from scrabbleScores'''
    if (scorelist[0][0] == letter): return scorelist[0][1]
    else: return letterScore(letter, scorelist[1:])

def wordScore(S,scorelist):
    '''Returns the score of a word'''
    if S == '': return 0
    else: return letterScore(S[0],scorelist) + wordScore(S[1:],scorelist)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    assert n>=0 and n <= len(L)
    def taker(accumulator, n, L):
        if n == 0: return accumulator
        else: return taker(accumulator+[L[0]], n-1, L[1:])
    return taker([],n,L)  # your code goes here



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    assert n >= 0 and n <= len(L)
    def dropper(dissipator, n):
        if n == 0: return dissipator
        else: return dropper(dissipator[1:],n-1)
    return dropper(L,n)
    # your code goes here


