# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:23:31 2019

@author: Kyuhwan

"""


"""
Problem:

A game for one player is played on a board consisting of N consecutive squares, numbered from 0 to N − 1. There is a number written on each square. A non-empty array A of N integers contains the numbers written on the squares. Moreover, some squares can be marked during the game.

At the beginning of the game, there is a pebble on square number 0 and this is the only square on the board which is marked. The goal of the game is to move the pebble to square number N − 1.

During each turn we throw a six-sided die, with numbers from 1 to 6 on its faces, and consider the number K, which shows on the upper face after the die comes to rest. Then we move the pebble standing on square number I to square number I + K, providing that square number I + K exists. If square number I + K does not exist, we throw the die again until we obtain a valid move. Finally, we mark square number I + K.

After the game finishes (when the pebble is standing on square number N − 1), we calculate the result. The result of the game is the sum of the numbers written on all marked squares.

For example, given the following array:

    A[0] = 1
    A[1] = -2
    A[2] = 0
    A[3] = 9
    A[4] = -1
    A[5] = -2
one possible game could be as follows:

the pebble is on square number 0, which is marked;
we throw 3; the pebble moves from square number 0 to square number 3; we mark square number 3;
we throw 5; the pebble does not move, since there is no square number 8 on the board;
we throw 2; the pebble moves to square number 5; we mark this square and the game ends.
The marked squares are 0, 3 and 5, so the result of the game is 1 + 9 + (−2) = 8. This is the maximal possible result that can be achieved on this board.

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the maximal result that can be achieved on the board represented by array A.

For example, given the array

    A[0] = 1
    A[1] = -2
    A[2] = 0
    A[3] = 9
    A[4] = -1
    A[5] = -2
the function should return 8, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""
#%%
A = [1,-2, 0, 9, -1, 2,3,6,4]

# Don't have to count all of cases because we throw the dice(1~6)
# Therefore, we solve this problem in this way
# 1. Calculate max values for each location of A[index]
#   -> max(A[index]) = max(A[index:index-6])+A[index]  
#     (If we are location A[index], then we can arrive the range A[index+1:index+6])
# 2. Find last max values of A[n]

def solution(A):
    maxValueA =[A[0]] *(len(A))
    print(maxValueA)
    for idx in range(0, len(A)):
        if idx == 0:  # Initial location
            continue;   
        elif idx-6<0: # If current location is under the dice 6
            maxValueA[idx] = max(maxValueA[0:idx])+A[idx]         
        else:
            maxValueA[idx] = max(maxValueA[idx-6:idx])+A[idx]     
    return(maxValueA[-1])


solution(A)    
    # write your code in Python 3.6
    #%%
NR_POSSIBLE_ROLLS = 6
MIN_VALUE = 0
 

def solution(A):
    # The first six items are used for padding only, so that we can have
    # a unified for loop, no matter how many squares are there in input.
    # The first item is never accessed.
    max_so_far = [A[0]] * (len(A) + 6)
    for index in range(1, len(A)):
        # Because we have a fixed length of window as 6, the time
        # complexity of max(max_so_far[index : index + 6]) is O(1).
        max_so_far[index + 6] = max(max_so_far[index : index + 6]) +A[index]
        print(max_so_far)
    return max_so_far[-1]
#%%

solution(A)