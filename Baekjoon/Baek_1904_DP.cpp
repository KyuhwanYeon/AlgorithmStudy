#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;

    scanf("%d", &N);
    long Nmax = 1000000;
    vector <long> dp;
    dp.resize(Nmax+1,-1);
    dp[1] = 1;
    dp[2] =2;
    for(int i=3; i<= N; i++)
    {
        dp[i] = dp[i-1]+dp[i-2];   //Bottom up
        dp[i] = dp[i] % 15746;  // 15746 으로 나눈 나머지로 저장
    }
    cout<<dp[N];



    return 0;
}