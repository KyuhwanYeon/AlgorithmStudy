#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;
class Graph
{

public:
    bool isLoop;
    int cntNotTeam = 0;
    vector<int> x;
    vector<int> y;
    vector<bool> visited;
    vector<vector<int>> adj;
    //Constructor
    Graph(vector<int> nvector);
    void StartDFS();

private:
    void StartDFS(int currX, int startPos);
};
Graph::Graph(vector<int> nvector)
{
    vector<int> xandy(2);
    for (int i = 0; i < nvector.size(); i++)
    {
        x.push_back(i);
        y.push_back(nvector[i] - 1);
        xandy[0] = x[i];
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
        if (visited[i] ==false)

        {
        isLoop = false;
        StartDFS(i, i);
        //cout << "isLoop: " << isLoop << endl;
        if (isLoop ==false)
        {
            cntNotTeam +=1;
        }
        }
    }
}

void Graph::StartDFS(int currX, int startPos)
{
    visited[currX] = true;
   // cout << "visit: " << currX << endl;
    int next;
    next = adj[currX][1];
    if (next == startPos)
    {
        isLoop =true;
    }
    if (visited[next] == false)
    {

        StartDFS(next, startPos);
    }
}

int main()
{
    int T;
    int N;
    N = 7;

    T = 1;

    vector<int> Nvector{3, 1, 3, 7, 3, 4, 6};
    Graph graph(Nvector);
    graph.StartDFS();
    cout<<graph.cntNotTeam;

    return 0;
}
