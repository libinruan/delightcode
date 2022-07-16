这里我们可以用动态规划的解法，状态函数就是从上升子序列开头到当前位置的长度，方程
就是dp[i] = dp[i - 1] + 1。这里因为是累加的所以我们其实可以省略掉

O(n)的空间复杂度

```python
class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        size = len(A)
        if size < 1:
            return 0 
            
        if size < 2:
            return 1 
            
        dp1, dp2 = 1, 1 
        glomax = 0 
        
        for i in range(1, size):
            dp1 = dp1 + 1 if A[i] > A[i - 1] else 1 
            dp2 = dp2 + 1 if A[i] < A[i - 1] else 1 
            glomax = max(glomax, max(dp1, dp2))
            
        return glomax
```        