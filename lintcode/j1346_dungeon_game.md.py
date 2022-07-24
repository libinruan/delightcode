# https://www.lintcode.com/problem/1346/solution

# 本题采用二分+dp check的做法
# 二分是对于答案进行二分。
# check的时候我们要用dp进行，考虑到起点用mid的血量开始到终点是否够，最后比较得出答案

public class Solution {
  private boolean canSurvive(int health, int[][] dungeon) {
    int n = dungeon.length, m = dungeon[0].length;
    int[][] f = new int[n][m];

    f[0][0] = dungeon[0][0] + health;
    if (f[0][0] <= 0) {
      return false;
    }
    
    for (int i = 1; i < n; i++) {
      f[i][0] = f[i - 1][0] == Integer.MIN_VALUE
                ? Integer.MIN_VALUE
                : f[i - 1][0] + dungeon[i][0];
      if (f[i][0] <= 0) {
        f[i][0] = Integer.MIN_VALUE;
      }
    }
    for (int i = 1; i < m; i++) {
      f[0][i] = f[0][i - 1] == Integer.MIN_VALUE
                ? Integer.MIN_VALUE
                : f[0][i - 1] + dungeon[0][i];
      if (f[0][i] <= 0) {
        f[0][i] = Integer.MIN_VALUE;
      }
    }
    
    for (int i = 1; i < n; i++) {
      for (int j = 1; j < m; j++) {
        f[i][j] = Math.max(f[i - 1][j], f[i][j - 1]);
        if (f[i][j] == Integer.MIN_VALUE) {
          continue;
        }
        f[i][j] += dungeon[i][j];
        if (f[i][j] <= 0) {
          f[i][j] = Integer.MIN_VALUE;
        }
      }
    }
    
    return f[n - 1][m - 1] > 0;
  }
  
  public int calculateMinimumHP(int[][] dungeon) {
    int start = 1, end = Integer.MAX_VALUE - 1;
    while (start + 1 < end) {
      int mid = (end - start) / 2 + start;
      if (canSurvive(mid, dungeon)) {
        end = mid;
      } else {
        start = mid;
      }
    }
    if (canSurvive(start, dungeon)) {
      return start;
    }
    return end;
  }
}



# https://www.lintcode.com/problem/1346/solution/58667
# answer 1
# 动态规划
# 思路及算法

# 几个要素：「M \times NM×N 的网格」「每次只能向右或者向下移动一步」，让人很容易
# 想到该题使用动态规划的方法。

# 但是我们发现，如果按照从左上往右下的顺序进行动态规划，对于每一条路径，我们需要
# 同时记录两个值。第一个是「从出发点到当前点的路径和」，第二个是「从出发点到当前
# 点所需的最小初始值」。... ... to be continued

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        n, m = len(dungeon), len(dungeon[0])
        BIG = 10**9
        dp = [[BIG] * (m + 1) for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)

        return dp[0][0]

# 复杂度分析

# 时间复杂度：O(N \times M)O(N×M)，其中 N,MN,M 为给定矩阵的长宽。

# 空间复杂度：O(N \times M)O(N×M)，其中 N,MN,M 为给定矩阵的长宽，注意这里可以利用滚动数组进行优化，优化后空间复杂度可以达到 O(N)O(N)。    



# answer 2
# end to start DP
# 首先用到了高频班提到过的 “正难则反”，
# 即 如果从start出发发现很难入手，
# 那就从end倒推回start.

# DP二维数组的定义是：
# 如果Knight需要在当前cell存活下去所需要的最小血量，
# 所以在bottom-right的终点处，先初始化为max(1, 1 - dungeon[m- 1][n - 1]),
# 翻译成自然语言就是：如果dungeon[m -1][n - 1]处不会掉血，那么需要的血量是1，
# 如果会掉血, 需要的血量是掉血量 + 1

# 之后再初始化最后一行（Knight只能往右走）和最后一列（骑士只能往下走）

# 最后再处理剩下的cell, 先挑选出min(往下走的next cell的最小血量， 往右走的next cell的最小血量)，记为curr
# 当前cell的最小血量就是max(curr - dungeon[ i ][ j ], 1)
class Solution:
    """
    @param dungeon: a 2D array
    @return: return a integer
    """
    def calculateMinimumHP(self, dungeon):
        # write your code here
        
        m, n = len(dungeon), len(dungeon[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        
        for j in range(n - 2, -1, -1):
            
            dp[m - 1][j] = max(dp[m - 1][j + 1] - dungeon[m - 1][j], 1)
            
        for i in range(m - 2, -1, -1):
            
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 1)
            
        for i in range(m - 2, -1, -1):
            
            for j in range(n - 2, -1, -1):
                
                curr = min(dp[i + 1][j], dp[i][j + 1])
                
                dp[i][j] = max(curr - dungeon[i][j], 1)
                
        return dp[0][0]
