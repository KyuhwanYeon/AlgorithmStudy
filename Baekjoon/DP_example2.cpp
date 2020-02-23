#include <cstdio>
#include <vector>
using namespace std;
 
int main(){
    int N;
    scanf("%d", &N);
    vector<int> dp(N+1, 0);
    dp[1] = 1;
    for(int i=2; i<=N; i++)
        dp[i] = dp[i-1] + dp[i-2];
    printf("%d\n", dp[N]);
}
