#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>

using namespace std;
class Graph
{
public:
    vector<vector<int>> map;
    vector<vector<bool>> visited;
    vector<int> start;
    vector<int> end;
    queue<vector<int>> Q;
    bool exit = false;
    int level = 1;

    // Constructor
    Graph(vector<vector<int>> map_);

    void BFS(); // 너비 우선 탐색
private:
    vector<vector<int>> adjNode(vector<int> curr);
};

Graph::Graph(vector<vector<int>> map_) : map(map_)
{
    start.push_back(0);
    start.push_back(0); //set start position {0,0}
    end.push_back(map_.size()-1);
    end.push_back(map_[0].size()-1); // set end position {N,M} 위치 이기 때문에 -1씩해줌
    visited.resize(map_.size(), vector<bool>(map_[0].size(), false));
}

vector<vector<int>> Graph::adjNode(vector<int> curr)
{
    vector<vector<int>> adjNodeList;
    //check adjNode = 1;
    if (curr[1] + 1 < map[0].size() && map[curr[0]][curr[1] + 1] == 1) // x+1, y
    {
        vector<int> tmpXplus1{curr[0], curr[1] + 1};
        adjNodeList.emplace_back(tmpXplus1);
    }
    if (curr[0] + 1 < map.size() && map[curr[0] + 1][curr[1]] == 1) // x, y+1
    {
        vector<int> tmpYplus1{curr[0] + 1, curr[1]};
        adjNodeList.push_back(tmpYplus1);
    }
    if (curr[1] - 1 >= 0 && map[curr[0]][curr[1] - 1] == 1) // x-1, y
    {
        vector<int> tmpXminus1{curr[0], curr[1] - 1};
        adjNodeList.push_back(tmpXminus1);
    }
    if (curr[0] - 1 >= 0 && map[curr[0] - 1][curr[1]] == 1) // x, y-1
    {
        vector<int> tmpYminus1{curr[0] - 1, curr[1]};
        adjNodeList.push_back(tmpYminus1);
    }

    return adjNodeList;
}

void Graph::BFS()
{

    Q.push(start);        // start 지점에서 시작!
    visited[0][0] = true; // start 방문

    while (!exit)
    {
        int qSize = Q.size();
        //cout << "------ level " << level << " ------" << endl;
        for (int i = 0; i < qSize; i++) //  Q의 크기 안에서 탐색
        {
            vector<int> curr = Q.front(); // Q의 맨 앞의 것을 현재 지점
            Q.pop();                      // 현재지점값을 Q에서 빼주고
                                          // cout << "node " << curr << " visited" << endl;
            vector<vector<int>> currAdj = adjNode(curr);

            for (vector<int> next : currAdj) // 현재 노드에 연결되어있는 노드들 중에서 탐색
            {
                if (visited[next[0]][next[1]] == false) //만약 다음 노드가 방문이 되어있지 않았다면
                {
                    visited[next[0]][next[1]] = true; //방문
                    Q.push(next);

                    if (next[0] == end[0] && next[1] == end[1])
                    {
                        exit = true; // End 값을 찾았으면 탈출!
                        break;
                    }
                }
            }
            
            if (exit == true)
            {
                break;
            }
        }
        level++;
        if (exit == true)
        {
            break;
        }
    }
}

vector<int> explode_string(string const &str) {
  vector<char> result(str.length());
  copy(begin(str), end(str), begin(result));
  vector<int> result_int;
  for (int i = 0; i<result.size(); i++)
  {
      result_int.push_back((int)result[i]-48);
  }

  return result_int;
}

int main()
{
    int N, M, K;
    vector<vector<int>> Map;
    
    vector<int> row_vec;
    scanf("%d" "%d", &N, &M);
    for (int i = 0; i < N; i++)
    {
        cin.clear();
        string row;
        cin>>row;
        row_vec= explode_string(row);
        Map.push_back(row_vec);
    }

    Graph graph(Map);
    graph.BFS();
    cout<<graph.level;
}