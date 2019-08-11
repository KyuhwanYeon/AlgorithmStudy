# -*- coding: utf-8 -*-
"""
Created on Sun Aug 1,1, 0,1,:33:28 20,1,9

@author: Kyuhwan
래 <그림 1,>과 같이 여러개의 정사각형칸들로 이루어진 정사각형 모양의 종이가 주어져 있고, 각 정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있다. 주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 한다.



전체 종이의 크기가 N×N(N=2k, k는 1, 이상 7 이하의 자연수) 이라면 종이를 자르는 규칙은 다음과 같다.

전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서 <그림 2>의 I, II, III, IV와 같이 똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다. 나누어진 종이 I, II, III, IV 각각에 대해서도 앞에서와 마찬가지로 모두 같은 색으로 칠해져 있지 않으면 같은 방법으로 똑같은 크기의 네 개의 색종이로 나눈다. 이와 같은 과정을 잘라진 종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복한다.

위와 같은 규칙에 따라 잘랐을 때 <그림 3>은 <그림 1,>의 종이를 처음 나눈 후의 상태를, <그림 4>는 두 번째 나눈 후의 상태를, <그림 5>는 최종적으로 만들어진 다양한 크기의 9장의 하얀색 색종이와 7장의 파란색 색종이를 보여주고 있다.



입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램을 작성하시오.
"""

# Test case: 

#A=[[1, 1, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 1, 1],[0, 0, 0, 0, 1, 1, 0, 0],[0, 0, 0, 0, 1, 1, 0, 0],[1, 0, 0, 0, 1, 1, 1, 1],[0, 1, 0, 0, 1, 1, 1, 1],[0, 0, 1, 1, 1, 1, 1, 1],[0, 0, 1, 1, 1, 1, 1, 1]]

NumRow = int(input())
Map = [[0]*NumRow for i in range(NumRow)]
for Idx1 in range(NumRow):
    TempInput= map(int, input().split())
    for Idx2, Number in enumerate(TempInput):
        Map[Idx1][Idx2] = int(Number)

global CntZero
CntZero = 0
global CntOne
CntOne = 0
def CheckColor(SubA):
    global CntZero
    global CntOne

    ZeroCheck = 0            
    OneCheck = 1
    
    for y in SubA:
        for xyVal in y:
            ZeroCheck = ZeroCheck +xyVal
            OneCheck = OneCheck*xyVal

    if ZeroCheck == 0:
        CntZero += 1    
    elif OneCheck == 1:
        CntOne += 1 
    else:
        return Divide(SubA)


        
def Divide(A):
    
    if len(A) == 1:
        return 1
    elif len(A)%2 ==0:
        
        SubA_y_1 = A[0:int(len(A)/2)]
        SubA_y_2 = A[int(len(A)/2):]
        SubA_xy_11 = [SubX[0:int(len(A)/2)] for SubX in SubA_y_1]
        SubA_xy_12 = [SubX[0:int(len(A)/2)] for SubX in SubA_y_2]
        SubA_xy_21 = [SubX[int(len(A)/2):] for SubX in SubA_y_1]
        SubA_xy_22 = [SubX[int(len(A)/2):] for SubX in SubA_y_2]        
        CheckColor(SubA_xy_11)
        CheckColor(SubA_xy_12)
        CheckColor(SubA_xy_21)
        CheckColor(SubA_xy_22)

                                
Divide(Map)
print(CntZero)
print(CntOne)    