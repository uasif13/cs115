'''
Created on 6 October 2019
@author:   Asif Uddin
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

def sv_tree(trunk_length, levels):
    '''draws a tree'''
    if levels == 0:
        return
    if levels == 1:
        turtle.pencolor("green")
    else:
        turtle.pencolor("brown")
    turtle.width(levels)
    turtle.forward(trunk_length)
    turtle.right(30)
    sv_tree(trunk_length/2,levels-1)
    turtle.left(60)
    sv_tree(trunk_length/2,levels-1)
    turtle.right(30)
    turtle.backward(trunk_length)

def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    memo = {}
    def flucas(m,n):
        if n in memo:
            return memo[n]
        elif m == 0:
            memo[0] = 2
            return flucas(m+1,n)
        elif m == 1:
            memo[1] = 1
            return flucas(m+1,n)
        else:
            answer = memo[m-1]+memo[m-2]
            memo[m] = answer
            return flucas(m+1,n)
    return flucas(0,n)
    pass  # TODO

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if (amount, coins) in memo:
            return memo[(amount, coins)]
        if amount == 0:
            result = 0
        elif len(coins) == 0 or amount < 0:
            result = float("inf")
        else:
            use_it = 1 + fast_change_helper(amount - coins[0], coins, memo)
            lose_it = fast_change_helper(amount, coins[1:], memo)
            result = min(use_it, float("inf") if lose_it == 0 else lose_it)
        memo[(amount, coins)] = result
        return result
    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100])) #4
print(fast_change(292, [1, 5, 10, 20, 50, 100])) #7
print(fast_change(673, [1, 5, 10, 20, 50, 100])) #11
print(fast_change(724, [1, 5, 10, 20, 50, 100])) #12
print(fast_change(888, [1, 5, 10, 20, 50, 100])) #15

# Should take a few seconds to draw a tree.
sv_tree(100, 6)
