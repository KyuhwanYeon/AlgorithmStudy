#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
class Graph
{
public:
    int N, start, end;
    bool exit = false;
    int level = 0;
    vector<vector<int>> adjNode;
    vector<bool> visited;
    queue<int> Q;

    // Constructor
    Graph(int n, int strt, int end);

    void BFS(); // 너비 우선 탐색
    void sortList();
    void addEdge(int u, int v);

private:
    void BFS(vector<int> curr);
};

// Define contructor
Graph::Graph(int n, int strt, int end) : N(n), start(strt), end(end)
{
    adjNode.resize(N);
    visited.resize(N, false);
}
void Graph::sortList()
{
    for (int i = 0; i < N; i++)
        sort(adjNode[i].begin(), adjNode[i].end());
}
void Graph::addEdge(int u, int v)
{
    adjNode[u].push_back(v);
    adjNode[v].push_back(u);
}

void Graph::BFS()
{
    Q.push(start);         // start 지점에서 시작!
    visited[start] = true; // start 방문

    while (!exit)
    {

        int qSize = Q.size();
        //  cout << "------ level " << level << " ------" << endl;
        for (int i = 0; i < qSize; i++) //  Q의 크기 안에서 탐색
        {
            int curr = Q.front(); // Q의 맨 앞의 것을 현재 지점
            Q.pop();              // 현재지점값을 Q에서 빼주고
                                  // cout << "node " << curr << " visited" << endl;

            for (int next : adjNode[curr]) // 현재 노드에 연결되어있는 노드들 중에서 탐색
            {
                if (visited[next] == false) //만약 다음 노드가 방문이 되어있지 않았다면
                {
                    visited[next] = true; //방문

                    Q.push(next); // Q에 다음 노드를 삽입
                    if (next == end)
                    {
                        exit = true; // End 값을 찾았으면 탈출!
                    }
                }
            }
            
            if (exit == true)
            {
                break;
            }
        }
        level += 1; // 다음 level로 진입
        if (Q.empty() == 1 && exit ==false)
        {
            level = -1;
            exit = true;
        } // 완전 탐색이 되어서 Q에 암것도 없으면 종료
    }
}
int main()
{
    int N;
    int R;
    int start, end;

    scanf("%d", &N);
    scanf("%d" "%d", &start, &end);
    Graph graph(N, start - 1, end - 1);
    scanf("%d", &R);
    for (int i = 0; i < R; i++)
    {
        int k1, k2;
        scanf("%d %d", &k1, &k2);

        graph.addEdge(k1 - 1, k2 - 1);
    }
    graph.sortList();
    graph.BFS();
    cout << graph.level<<endl;

    return 0;
}