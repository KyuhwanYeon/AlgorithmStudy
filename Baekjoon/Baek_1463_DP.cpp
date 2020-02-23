#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector <long> dp;
int func(int N)
{
    if (N== 1){return 0;}
    int minCnt;
    if (dp[N] != -1){return dp[N];}
    minCnt = func(N-1)+1;
    if (N%3 == 0){minCnt = min(minCnt,func(N/3)+1);}
    if (N%2 == 0){minCnt = min(minCnt,func(N/2)+1);}
    dp[N]= minCnt;
    return minCnt;

}
int main()
{
    int N,M;
    long Nmax = 1000001;
    dp.resize(Nmax, -1);

    scanf("%d", &N);
    cout<<func(N);
    return 0;
}