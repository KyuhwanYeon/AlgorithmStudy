# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:48:17 2019

@author: Kyuhwan
"""


X= 5
A = [1,3,1,4,2,3,5,4]
#%%
def solution(X, A):
    Leaves = []
    for i in range(X):
        Leaves.append(i+1)
    print(Leaves)
    cnt = 0
       
    for i, v in enumerate(A):
        for idx in Leaves:
            if v==idx:
                print(v)
                Leaves.remove(v)
                print(Leaves)
                cnt +=1
            if not Leaves:
                return i

    return -1
    
#%%
    
def solution(X, A):
    check = [0] * X
    check_sum = 0
    for i in range(len(A)):
        if check[A[i]-1] == 0:
            check[A[i]-1] = 1
            check_sum += 1
            print(check)
            if check_sum == X:
                return i
    return -1
a=solution(X,A)