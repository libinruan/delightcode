Snow
```python
class Solution(object):
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]        
```

这个题目其实是一个组合问题。对方向编号，向下是 0，向右是 1，那么从左下角走到右上角一定要经过 M 个 1 和 N 个 0。

这个题目可以转化为从 M+N 个不同的盒子中挑出M个盒子有多少种方法。答案是C(M+N, M) 或者 C(M+N, N) 的组合数。

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        total = m + n - 2
        v = n - 1
        def permutation(m, n):
            son = 1
            for i in range(m, m - n, -1):
                son *= i
            mom = 1
            for i in range(n, 0, -1):
                mom *= i
            return son / mom
        return permutation(total, min(v, total -v))
```


方法：组合数学
time O(min(m, n)) space O(1)
source: https://www.lintcode.com/problem/114/solution/56849?fromId=164&_from=collection
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)
```

方法：动态规划
time O(mn) space O(mn)
source: https://www.lintcode.com/problem/114/solution/56849?fromId=164&_from=collection
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]
```