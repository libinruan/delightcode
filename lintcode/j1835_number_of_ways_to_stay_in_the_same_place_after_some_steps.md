"""
dp - https://www.lintcode.com/problem/1835/solution/59231?fromId=164&_from=collection
"""
class Solution:
    def num_ways(self, steps: int, arr_len: int) -> int:
        mod = 10**9 + 7
        maxColumn = min(arr_len - 1, steps)

        dp = [0] * (maxColumn + 1)
        dp[0] = 1

        for i in range(1, steps + 1):
            dpNext = [0] * (maxColumn + 1)
            for j in range(0, maxColumn + 1):
                dpNext[j] = dp[j]
                if j - 1 >= 0:
                    dpNext[j] = (dpNext[j] + dp[j - 1]) % mod
                if j + 1 <= maxColumn:
                    dpNext[j] = (dpNext[j] + dp[j + 1]) % mod
            dp = dpNext
        
        return dp[0]