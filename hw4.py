#
# Author: Asif Uddin
# Date: 28 September 2019
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#

from cs115 import map

def pascal_row(n):
    '''given a value n, it computes the pascal row'''
    if n == 0: return [1]
    if n == 1: return [1,1]
    else: return pascal_row(0)+middle(pascal_row(n-1))+pascal_row(0)

def middle(before):
    '''calculates the values that go in the middle of the pascal row'''
    if len(before) < 2: return []
    else: return [before[0] + before[1]] + middle(before[1:])

def pascal_triangle(n):
    '''computes the pascal_triangle'''
    return map(pascal_row,range(n+1))

def test_pascal_row():
    '''
    tests pascal_row (at least 4 asserts)
    tests for row 0,1,5,10
    '''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(5) == [1,5,10,10,5,1]
    assert pascal_row(10) == [1,10,45,120,210,252,210,120,45,10,1]


def test_pascal_triangle():
    '''
    tests pascal_triangle (at least 4 asserts)
    tests for triangle 0,1,5,10
    '''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(10) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1],[1,9,36,84,126,126,84,36,9,1],[1,10,45,120,210,252,210,120,45,10,1]]
    
