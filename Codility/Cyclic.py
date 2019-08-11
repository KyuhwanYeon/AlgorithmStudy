# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 10:14:21 2019

@author: Kyuhwan
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
A= [3,8,7,9,6]
K=1

def solution(A, K):
    TempA=A
    for i in range(K):
        TempB = TempA[-1:]
        TempC = TempA[:-1]
        TempB += TempC
        TempA=TempB
    # write your code in Python 3.6
    print(TempB)
    pass

#%%
solution(A,K)