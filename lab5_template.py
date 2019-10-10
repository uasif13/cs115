'''
Created on October 2, 2019
@author:   Asif Uddin
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 5
'''
import time
from cs115 import map

words = []
HITS = 10

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    memo = {}
    def fED(first,second):
        if (first, second) in memo:
            return memo[(first,second)]
        elif first == '':
            memo[(first,second)] = len(second)
            return len(second)        
        elif second == '':
            memo[(first,second)] = len(first)
            return len(first)
        elif first[0] == second[0]:
            answer = fED(first[1:],second[1:])
            memo[(first,second)] = answer
            return answer
        else:
            subsitution = 1 + fED(first[1:],second[1:])
            deletion = 1 + fED(first[1:],second)
            insertion = 1 + fED(first,second[1:])
            answer = min(subsitution,deletion,insertion)
            memo[(first,second)] = answer
            return answer
    return fED(first,second)
    pass  # TODO

def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return map(lambda x: (fastED(user_input,x),x),words)
    pass  # TODO

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
