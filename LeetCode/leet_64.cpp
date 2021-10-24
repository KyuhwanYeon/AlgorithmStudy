#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
class Solution
{
public:
  int minPathSum(vector<vector<int>> &grid)
  {

    int answer = 0;
    // Initialize
    vector<vector<int>> dp = grid;
    for (int i = 0; i < grid.size(); i++)
    {
      for (int j = 0; j < grid[0].size(); j++)
      {
        dp[i][j] = 0;
      }
    }
    // Execption case
    if (dp.size() == 0 && dp[0].size() == 0)
    {
      return grid[0][0];
    }

    // Dynamic programming
    for (int i = 0; i < dp.size(); i++)
    {
      for (int j = 0; j < dp[0].size(); j++)
      {
        if (i == 0 && j == 0)
        {
          dp[i][j] = grid[i][j];
        }
        else if (i > 0 && j > 0)
        {
          dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1]);
        }
        else if (i > 0)
        {
          dp[i][j] = grid[i][j] + dp[i - 1][j];
        }
        else if (j > 0)
        {
          dp[i][j] = grid[i][j] + dp[i][j - 1];
        }
      }
    }
    return dp[dp.size() - 1][dp[0].size() - 1];
  }
};

int main(int argc, char **argv)
{
  vector<vector<int>> tc = {{1, 3, 1}, {1, 5, 1}, {4, 2, 1}};
  Solution solution;
  int tc_result = solution.minPathSum(tc);

  printf("test! %d", tc_result);
}