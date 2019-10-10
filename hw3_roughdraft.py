# Author: Asif Uddin
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Date: September 19, 2019

def change(amount, coins):
##    print (amount)
##    print (coins)
    '''Returns the minimum number of coins from a given coin system to make a certain amount
       Returns infinity if not possible'''
    # base case of recursion
    if amount == 0:
##        print (coins)
        return [[]]
    # case where it is impossible to form the value with the given change
    if (amount < 0 or coins == []): return []
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
##        print (one_time)
##        print (multi_times)
##        print (no_times)
        return min([coins[0]]+min(one_time, multi_times),no_times)
