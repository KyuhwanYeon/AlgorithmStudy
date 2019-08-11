
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 1,0, 20,:33:54 20,1,9

@author: Kyuhwan
그림 1,>과 같이 정사각형 모양의 지도가 있다. 1,은 집이 있는 곳을, 0,은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1,>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.


"""
# Test case: 
# A=[[0, 1, 1, 0, 1, 0, 0],[0, 1, 1, 0, 1, 0, 1],[1, 1, 1, 0, 1, 0, 1],[0, 0, 0, 0, 1, 1, 1],[0, 1, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1, 0],[0, 1, 1, 1, 0, 0, 0]]
# Map =A
#%% Read Input
NumRow = int(input())
Map = [[0]*NumRow for i in range(NumRow)]
for Idx1 in range(NumRow):
    TempInput= list(input())
    for Idx2, Number in enumerate(TempInput):
        Map[Idx1][Idx2] = int(Number)
#%% Solution DFS
def BFS_map(m,start_node):
    visit = list()
    queue = list()
    queue.append(start_node)
    while queue:
        nodeX, nodeY = queue.pop(0)    
        if [nodeX, nodeY] not in visit:
            visit.append([nodeX,nodeY])
            if nodeX+1 <len(m[0]) :
                if m[nodeX+1][nodeY] ==1:
                    queue.append([nodeX+1,nodeY])
            if nodeY+1 <len(m) :
                if m[nodeX][nodeY+1] ==1 : 
                    queue.append([nodeX,nodeY+1])
            if nodeX-1 >=0 :
                if m[nodeX-1][nodeY] ==1 : 
                    queue.append([nodeX-1,nodeY])
            if  nodeY-1 >=0 :
                if m[nodeX][nodeY-1] ==1:
                    queue.append([nodeX,nodeY-1])
    return visit

#%%  Set start position and run BFS

def set_startPos(m):
    startPosCandidate = []
    CheckHouseList = []
    HouseList = []
    for xidx in range(len(m[0])):
        for yidx in range(len(m)):
            startPosCandidate.append([xidx,yidx])
            
    for startPos in startPosCandidate: 
        if m[startPos[0]][startPos[1]] == 1:
            if  startPos not in CheckHouseList:
                tmpHouseList = BFS_map(m,startPos)
                CheckHouseList.extend(tmpHouseList)
                HouseList.append(tmpHouseList)
            
    print(len(HouseList))
    LengthList = []
    for i in range(len(HouseList)):
        LengthList.append(len(HouseList[i]))
    LengthList.sort()
    for i in LengthList:
        print(i)

#%%
set_startPos(Map)            
#%% bfs example
'''
def bfs(graph, start_node):
    visit = list()
    queue = list()
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit

if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D', 'G'],
        'D': ['C', 'E'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['C'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
        
    }
    print(bfs(graph, 'A'))
'''