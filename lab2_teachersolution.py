def dot(L,K):
    '''dot product of equal-length lists'''
    if L == []:
        return 0
    else:
        return (L[0]*K[0])+dot(L[1:],K[1:])

def test_dot():
    print (dot([5,3], [6,4]) == 42)

def explode(s):
    '''list of characters in string s'''
    if s == '':
        return []
    else:
        return [s[0]] + explode(s[1:])

def test_explode():
    print(explode('abc') == ['a','b','c'])

def myFilter(f,L):
    '''assume f is a unary function to boolean
    return the lists of elements of L for'''

def even(n): return n%2 == 0
def test_myFilter():
    print(myFilter(even, [1,2,5,6,7]) == [2,6])
