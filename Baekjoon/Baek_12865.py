# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 10:29:56 2019

@author: Kyuhwan

이 문제는 아주 평범한 배낭에 관한 문제이다.

한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 아직 행군을 해본 적이 없는 준서는 최대 K무게까지의 배낭만 들고 다닐 수 있다. 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
"""


#%% Test case
'''
N= 4 
K = 7 # Size of bag
Item = [[6, 13],[4, 8],[3, 6],[5, 12]]'''
#%%  Input

N,K = map(int, input().split())
ItemMatrix = [[0]*2 for _ in range(N) ]
    
for idx in range(N):
    TempItemSize, TempItemValue= map(int, input().split())
    ItemMatrix[idx][0] = TempItemSize
    ItemMatrix[idx][1] = TempItemValue
#%%


def pack(MaxCapacity, item):
    NumItem = len(item)
    ValueMatrix = [[0]*(MaxCapacity+1) for _ in range(NumItem+1) ]
    
    for itemIdx in range(NumItem+1):
        for BagSize in range(MaxCapacity+1):u
            if itemIdx>=1:
                itemSize= item[itemIdx-1][0]
                itemValue = item[itemIdx-1][1]
            else:
                itemSize =0
                itemValue = 0
            
            if itemIdx == 0 or BagSize ==0:
                ValueMatrix[itemIdx][BagSize] = 0
            elif BagSize < itemSize:
                ValueMatrix[itemIdx][BagSize] = ValueMatrix[itemIdx-1][BagSize]
            elif BagSize >= itemSize: # Bag has available space for the item
                ValueMatrix[itemIdx][BagSize] = max(ValueMatrix[itemIdx-1][BagSize-itemSize]+ itemValue , ValueMatrix[itemIdx-1][BagSize])
    print(ValueMatrix[NumItem][MaxCapacity])

pack(K, ItemMatrix)


        #%%
'''
x = 10

dp = [0 for _ in range(x+1)]
#%%
dp[1] = 0

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    if not i % 2 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
    if not i % 3 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1

print(dp[x])

#%% https://gsmesie692.tistory.com/113

memo = {1:1, 2:1}
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    if n not in memo:
        memo[n] = fib(n-1) +fib(n-2)
    return memo[n]
print(fib(10))

'''