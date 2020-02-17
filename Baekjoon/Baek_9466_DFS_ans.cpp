#include <iostream>
#include <vector>

using namespace std;
class Graph
{
public:
    bool isLoop;
    vector<int> checkLoop;
    int cntNotTeam = 0;
    int totalCntNotTeam = 0;
    vector<int> y;
    vector<bool> visited;
    vector<vector<int>> adj;
    //Constructor
    Graph(vector<int> nvector);
    void StartDFS();

private:
    void StartDFS(int currX);
};

Graph::Graph(vector<int> nvector)
{
    vector<int> xandy(2);
    for (int i = 0; i < nvector.size(); i++)
    {
        y.push_back(nvector[i] - 1);
        xandy[0] = i;
        xandy[1] = y[i];
        //add edge
        adj.push_back(xandy);
        //set visited all false
        visited.push_back(false);
    };
}
void Graph::StartDFS()
{
    int curr = 0;
    for (int i = 0; i < y.size(); i++)
    {
        if (visited[i] == false)
        {
            //cout<<"New DFS "<<endl;
            StartDFS(i);
            totalCntNotTeam += cntNotTeam;
            checkLoop.clear();
        }
    }
}

void Graph::StartDFS(int currX)
{
    visited[currX] = true;
    checkLoop.push_back(currX);
    //cout << "visit: " << currX << endl;
    int next;
    next = adj[currX][1];
    cntNotTeam = 0;
    int LoopIdx = 0;

    if (visited[next] == true) // 루프를 체크할 때는, 다음번 노드가 무조건 visit상태이기 때문에 이와 같은 조건이 붙는다.
    {
        for (int i = 0; i < checkLoop.size(); i++)
        {
            if (checkLoop[i] == next)
            {
                break;
            }
            else
            {
                cntNotTeam += 1;
            }
        }
    }

    if (visited[next] == false)
    {
        StartDFS(next);
    }
}

////////////////////////////////////////////////////
int main()
{
    int T;
    int N;
    int tmpK;
    

    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        vector<int> Nvector;
        scanf("%d", &N);
        
        for (int j = 0; j < N; j++)
        {
            scanf("%d", &tmpK);
            Nvector.push_back(tmpK);
        }
        Graph graph(Nvector);
        graph.StartDFS();
        cout << graph.totalCntNotTeam<<endl;
    }
    
   /*
    N = 7;

    T = 1;

    vector<int> Nvector{3, 1, 3, 7, 3, 4, 6};
    //vector<int> Nvector{2, 3, 4, 5, 3, 7, 8, 9, 10, 8};
    Graph graph(Nvector);
    graph.StartDFS();
    cout << graph.totalCntNotTeam;
    */
    return 0;
}
