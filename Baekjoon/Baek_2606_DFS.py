# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:06:50 2019

@author: Kyuhwan

백준 2606 
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.



어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

출력
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
"""

NumCom=int(input())
NumRelation= int(input())
RelationSet = []
for Idx in range(NumRelation):
    com1, com2 = map(int, input().split())
    RelationSet.append([com1-1,com2-1])

# DFS: stack / 인접 행렬
# Create relation matrix (NumCom X NumCom)

Matrix = [[0]*NumCom for i in range(NumCom)]
# Set relation
for Relation in RelationSet:
    Matrix[Relation[0]][Relation[1]] = 1
    Matrix[Relation[1]][Relation[0]] = 1 # 양방향이므로 

def virusDFS(VirusMat,root):
    stack = [root]
    infected = []
    while stack:
        CurCom = stack.pop()
        for ComIdx,ComConnected in enumerate(VirusMat[CurCom]):
            if ComConnected ==1:
                if ComIdx not in infected:
                    stack.append(ComIdx)
        if CurCom not in infected:
            infected.append(CurCom)
    return len(infected)-1

print(virusDFS(Matrix,0))    


#%% 다른사람풀이 
N = int(input())
M = int(input())
 
graph = {i: list() for i in range(1, N + 1)}
 
for _ in range(M):
    a, b = map(int, input().split(' '))
    # 양방향임 이거때문에 몇번 재채점함
    graph[a].append(b)
    graph[b].append(a)
 
check = {i: False for i in range(1, N + 1)}
 
# bfs 구현 이게 왜 최단거리?
# 플로이드 와샬 쓰면 n^3인데..
q = [1]
count = 0
 
while q:
    now = q.pop(0)
    if check[now]:
        continue
    check[now] = True
    if now != 1:
        count += 1
    for i in graph[now]:
        if not check[i]:
            q.append(i)
 
print(count)

#%% DFS list example

graph={
1:[2,3],
2:[1,4,5,7],
3:[1,5,9],
4:[2,6],
5:[2,3,7,8],
6:[4],
7:[5,2],
8:[5],
9:[3],
}
def DFS(graph,root):
    stack=[root]
    visited=[]
    while stack:
        n=stack.pop()
        for i in graph[n]:
            if i not in visited:
                stack.append(i)
        if n not in visited:
            visited.append(n)
        print('v',visited)
    return visited
print(DFS(graph,1))


