#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

class Map
{
public:
    vector<vector<int>> grid{{0, 1, 0, 0, 0, 0}, {0, 1, 0, 0, 0, 0}, {0, 1, 0, 0, 0, 0}, {0, 1, 0, 0, 0, 0}, {0, 0, 0, 1, 1, 0}};
    int mapWidth = grid[0].size();
    int mapHeight = grid.size();

private:
};

class Planner : Map
{
public:
    vector<int> start{0, 0};
    vector<int> goal{mapHeight - 1, mapWidth - 1};
    int cost = 1;
    string movements_arrows[4] = {"^", "<", "v", ">"};

    vector<vector<int>> movements{
        {-1, 0},
        {0, -1},
        {1, 0},
        {0, 1}};

private:
};
template <typename T>
void Print2DVector(T vec2d)
{
    for (int i = 0; i < vec2d.size(); i++)
    {
        for (int j = 0; j < vec2d[0].size(); j++)
        {
            cout << vec2d[i][j] << " ";
        }
        cout << endl;
    }
}

vector<vector<int>> nextList(Map map, Planner planner, vector<int> curr, vector<vector<bool>> closelist, vector<vector<int>> &action)
{
    vector<vector<int>> nextList;
    int i = 0;

    for (vector<int> movement : planner.movements)
    {
        vector<int> next{curr[1] + movement[0], curr[2] + movement[1]};
        if (next[0] < map.grid.size() && next[0] >= 0 && next[1] < map.grid[1].size() && next[1] >= 0 && map.grid[next[0]][next[1]] == 0)
        {
            if (closelist[next[0]][next[1]] == false)  // 방문하지 않았고
            {
                action[next[0]][next[1]] = i;
                nextList.push_back(next);
            }
        }
        i++;
    }
    return nextList;
}
void FindShortestPath( Planner planner, Map map,vector<vector<int>> action, vector<vector<string>> &path)
{
    int x= planner.goal[1];
    int y =planner.goal[0];
    path[y][x] = "*";

    while(x != planner.start[1] && y!=planner.start[0])
    {
        x = x-planner.movements[action[y][x]][1];
        y = y-planner.movements[action[y][x]][0];
        path[y][x] = planner.movements_arrows[action[y][x]];

    }

}
void PrintStates(int expansion, queue<vector<int>> openlist, vector<int> curr)
{
    cout << endl;
    cout << "Expansion#: " << expansion << endl;
    cout << "Cell Picked: [" << curr[0] << " " << curr[1] << " " << curr[2] << "]" << endl;
    cout << "Openlist: ";
    queue<vector<int>> copy = openlist;
    for (int i = 0; i < openlist.size(); i++)
    {
        vector<int> tmp = copy.front();
        copy.pop();
        cout << "[ " << tmp[0] << " " << tmp[1] << " " << tmp[2] << "]"
             << " ";
    }
    cout << endl;
}
void Search(Map map, Planner planner)
{
    queue<vector<int>> openlist;
    vector<vector<bool>> closelist(map.mapHeight, vector<bool>(map.mapWidth, false));
    vector<vector<int>> expansionvector(map.mapHeight, vector<int>(map.mapWidth, -1));
    vector<vector<int>> action(map.mapHeight, vector<int>(map.mapWidth, -1));
    vector<vector<string>> path(map.mapHeight, vector<string>(map.mapWidth, "-"));
    closelist[planner.start[0]][planner.start[1]] = true;
    int g = 0;
    int nextg = 0;
    openlist.push({g, planner.start[0], planner.start[1]});
    bool exit = false;
    int expansion = 0;
    while (!exit)
    {
        int qSize = openlist.size();
        for (int i = 0; i < qSize; i++) //  Q의 크기 안에서 탐색
        {
            vector<int> curr = openlist.front(); // Q의 맨 앞의 것을 현재 지점
            openlist.pop();                      // 현재지점값을 Q에서 빼주고
            vector<vector<int>> nextList_ = nextList(map, planner, curr, closelist, action);
            nextg = curr[0] + planner.cost;
            // 현재 상태에서 Q의 크기만큼만 인접 노드 조사하고 방문!
            for (vector<int> next : nextList_) // 현재 노드에 연결되어있는 노드들 중에서 탐색
            {
                closelist[next[0]][next[1]] = true;       //방문
                openlist.push({nextg, next[0], next[1]}); // 방문된 지점들을 Q에 추가해서 다음번 탐색에서 이용
            }
            expansionvector[curr[1]][curr[2]] = expansion;
            PrintStates(expansion, openlist, curr);
            expansion++;

            if (curr[1] == planner.goal[0] && curr[2] == planner.goal[1])
            {
                cout << "[" << curr[0] << ", " << curr[1] << ", " << curr[2] << "]" << endl;
                exit = true; // End 값을 찾았으면 탈출!
                break;
            }
        }
    }
    Print2DVector(action);
    cout<<"-------------------------"<<endl;
    FindShortestPath(planner, map, action,path);
    Print2DVector(path);
    Print2DVector(expansionvector);
}
int main()
{
    // Instantiate map and planner objects
    Map map;
    Planner planner;

    // Print classes variables
    // cout << "Map:" << endl;
    // Print2DVector(map.grid);
    // cout << "Start: " << planner.start[0] << " , " << planner.start[1] << endl;
    // cout << "Goal: " << planner.goal[0] << " , " << planner.goal[1] << endl;
    // cout << "Cost: " << planner.cost << endl;
    // cout << "Robot Movements: " << planner.movements_arrows[0] << " , " << planner.movements_arrows[1] << " , " << planner.movements_arrows[2] << " , " << planner.movements_arrows[3] << endl;
    // cout << "Delta:" << endl;
    // Print2DVector(planner.movements);
    Search(map, planner);

    return 0;
}
