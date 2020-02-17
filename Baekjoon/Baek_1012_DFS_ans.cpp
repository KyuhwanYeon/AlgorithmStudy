#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
class DFS
{
public:
    int M, N, K;
    int cntWarm = 0;
    vector<vector<int>> map;      // 배추 맵
    vector<vector<bool>> visited; // 방문 여부를 저장하는 배열

    // Constructor
    DFS(int m, int n, int k);
    // Accessor
    void PrintMap();
    void StartDFS(); // 깊이 우선 탐색
    // Mutator
    void SetMap(vector<int> K);
    vector<vector<int>> adjNode(vector<int> curr);

private:
    void StartDFS(vector<int> curr);
};
// Define contructor
DFS::DFS(int m, int n, int k) : M(m), N(n), K(k)
{
    map.clear();
    map.resize(n, vector<int>(m, 0));      // n*m 행렬을 0 으로 채움 ,m이 가로 길이, n은 세로길이
    visited.resize(n, vector<bool>(m, 0)); // 방문 여부를 알리는 visit 또한 맵과 동일한사이즈로 설정
 //   cout << "Class is construced" << std::endl;
}
// Define accessors
void DFS::PrintMap()
{

    for (int i = 0; i < map.size(); i++)
    {
        for (int j = 0; j < map[0].size(); j++)
        {

            cout << map[i][j] << ",";
        }
        cout << std::endl;
    }
}

void DFS::StartDFS()
{
    vector<int> startPos(2);
    // initialzied with false visited
    for (int i = 0; i < visited.size(); i++)
    {
        fill(visited[i].begin(), visited[i].end(), false);
    }
    for (int i = 0; i < visited.size(); i++)
    {
        for (int j = 0; j < visited[0].size(); j++)
        {
            if (map[i][j] == true && visited[i][j] == false)
            {
                cntWarm += 1;
               // cout << "-- new DFS begins --" << endl;
                startPos[0] = i;
                startPos[1] = j;
                StartDFS(startPos);
            }
        }
    }
}

vector<vector<int>> DFS::adjNode(vector<int> curr)
{
    vector<vector<int>> adjNodeList;
    //check adjNode = 1;
    if (curr[1] + 1 < M && map[curr[0]][curr[1] + 1] == 1) // x+1, y
    {
        vector<int> tmpXplus1{curr[0], curr[1] + 1};
        adjNodeList.push_back(tmpXplus1);
    }
    if (curr[0] + 1 < N && map[curr[0] + 1][curr[1]] == 1) // x, y+1
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
void DFS::StartDFS(vector<int> curr)
{
    visited[curr[0]][curr[1]] = true;
  //  cout << " visit position " << curr[1] << ", " << curr[0] << endl;
    for (auto adj : adjNode(curr))
    {
        if (visited[adj[0]][adj[1]] == false)
        {
            StartDFS(adj);
        }
    };
}
// Define mutators
void DFS::SetMap(vector<int> K)
{
    map[K[0]][K[1]] = 1;
};
int main()
{
    int T;
    int M, N, K;
    int Kx, Ky;
    vector<int> Krow(2);
    T = 1;

    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        scanf("%d %d %d", &M, &N, &K);
        DFS dfs(M, N, K);
        for (int j = 0; j < K; j++)
        {
            scanf("%d %d", &Kx, &Ky);
            Krow[0] = Ky;
            Krow[1] = Kx;
            dfs.SetMap(Krow);
        }
      //  dfs.PrintMap();

        dfs.StartDFS();
        cout << dfs.cntWarm<<endl;
    }
    return 0;
}