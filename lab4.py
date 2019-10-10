# Lab4
# Author: Asif Uddin
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Date:26 September 2019

from cs115 import map

def second(L):
    '''assume L has length two and return value at second index'''
    if L == []: return 0
    else:
        assert(len(L) == 2)
        return L[1]

def items(capacity,itemList):
    '''helper function gets lists of weights and values'''
    if (capacity  <= 0 or itemList == [] ): return []
    else:
        if capacity < itemList[0][0]: return items(capacity,itemList[1:])
        else:
            use_it = [itemList[0]]+items(capacity-itemList[0][0],itemList[1:])
            lose_it = items(capacity,itemList[1:])
            if sum(map(second,use_it)) > sum(map(second,lose_it)): return use_it
            else: return lose_it

def knapsack(capacity, itemList):
    '''main function that formats the list'''
    return [sum(map(second,items(capacity,itemList))),items(capacity,itemList)]






    
