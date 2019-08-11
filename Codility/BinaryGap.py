# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 00:05:31 2019

@author: Kyuhwan

Task description
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

# My solution
def solution(N):
    BinaryList = []
    TempN= N
    while(1):
        
        if TempN%2 == 1:
            if TempN == 1:            
                TempN= (TempN-1)/2
                BinaryList.append(1)
                BinaryList.reverse()
                break;
    
            else:
                TempN= (TempN-1)/2
                BinaryList.append(1) 
        elif TempN%2 == 0:
            if TempN == 2:            
                TempN= (TempN)/2
                BinaryList.append(0) 
                BinaryList.append(1)
                BinaryList.reverse()
                break;
            else:
                TempN= TempN/2
                BinaryList.append(0)

    MaxZeroArrCnt = 0;
    MaxZeroArr = [];
    ZeroIdx = 0;
    for idx in range(len(BinaryList)):
        
        if BinaryList[idx] == 0:
            if idx-ZeroIdx >= 1:
                MaxZeroArrCnt = MaxZeroArrCnt+1
                
    
            ZeroIdx = idx
        else:
            MaxZeroArr.append(MaxZeroArrCnt);
            MaxZeroArrCnt = 0;
    return (max(MaxZeroArr))        
        

#%%
solution(1041)

#Other
def solution(N):
    N = bin(N)[2:] # 함수의 인자로 받은 N을 2진수로 바꾼다, format(N, 'b') 도 가능
    arr = []

    for idx, value in enumerate(N):
        if value == '1':
            arr.append(idx) # 2진수 N의 각 자릿수 중에 1에 해당하는 자릿수의 인덱스 값을 찾아 빈 배열에 담는다.

    arr2 = []    

    for i in range(len(arr)-1):
        arr2.append(arr[i+1] - arr[i] - 1) # 배열에 담긴 요소를 인접한 요소와 뺀 결과를 새로운 빈 배열에 담는다.

    return max(arr2) # 그 중에서 최댓값을 리턴한다.
solution(1041)