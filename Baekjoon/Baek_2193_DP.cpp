#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;

    scanf("%d", &N);
    int Nmax = 90;
    vector <vector<long>> dp;
    dp.resize(Nmax+1, vector<long>(2, 0));
    int InitLastVal = 1;
    dp[1][0] = 0;
    dp[1][1] = 1;
    dp[2][0] = 1;
    dp[2][1] = 0;
    for(int i=2; i<= N; i++)
    {
        dp[i][0] = dp[i-1][0]+dp[i-1][1];   //Bottom up
        dp[i][1] = dp[i-1][0];
    }
    cout<<dp[N][0]+dp[N][1];



    return 0;
}