<!-- -------------------------------- 草莓有点疼 -------------------------------- -->
solution: https://www.lintcode.com/problem/513/solution/57220?fromId=164&_from=collection
```python
# O(sqrt(N)), O(1)
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def num_squares(self, n: int) -> int:
        def is_perfect_square(x):
            y = int(x**0.5)
            return y * y == x
            
        def check_answer4(x):
            while x % 4 == 0:
                x //= 4
            return x % 8 == 7

        if is_perfect_square(n):
            return 1
        if check_answer4(n):
            return 4
        for i in range(1, int(n**0.5)+1):
            j = n - i * i
            if is_perfect_square(j):
                return 2
        return 3
```

<!-- ------------------------------- chuishi -------------------------------- -->
做法1:
算法：dp
我们用f[i]表示i最少能被几个完全平方数来表示。

首先我们对dp数组赋予初值，对于每个完全平方数的f=1。

利用记忆化搜索来完成查找。对于i，我们考虑i的前继状态，也就是哪几个状态可以加上一个完全平方数抵达i。

对于所有能够抵达i的状态，取他们的最小值+1即可。

上述过程的状态转移方程为 f[i] = min{f[i], f[i - j * j] + 1} (j*j <= i)

边界: f[i*i] = 1

复杂度分析
时间复杂度O(n)
  * 枚举了数组的长度

空间复杂度O(n^(3/2))
  * 对于每个数，它的前继状态都有sqrt(i)个，i为这个数的大小。

  * 所以总的复杂度为sqrt(1)+sqrt(2)+....sqrt(n)约等于O(n^(3/2))

  * 证明过程太复杂，就不在此给出。


```python
def numSquares(self, n):
        # write your code here
        dp = []
        import sys
        for i in range(n+1):
            dp.append(sys.maxint)
        i = 0
        while i * i <= n:
            dp[i*i] = 1
            i += 1

        
        for i in range(n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i-j*j] + 1)
                j += 1
        return dp[n]
```

    

做法2:
##算法：数学做法

涉及四平方和定理

参考 http://www.cnblogs.com/grandyang/p/4800552.html

根据四平方和定理，我们可以发现，一个数能被四个数之内的平方和表示。

我们直接循环，判断这个数能否被1~到3个数的平方和表示即可，若不行，直接输出4
复杂度分析
时间复杂度O(n)

两重循环的上限为sqrt(n)，相乘即可。
空间复杂度O(1)

消耗了常数的空间

```python
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def num_squares(self, n: int) -> int:
        def is_perfect_square(x):
            y = int(x**0.5)
            return y * y == x
            
        def check_answer4(x):
            while x % 4 == 0:
                x //= 4
            return x % 8 == 7

        if is_perfect_square(n):
            return 1
        if check_answer4(n):
            return 4
        for i in range(1, int(n**0.5)+1):
            j = n - i * i
            if is_perfect_square(j):
                return 2
        return 3
```