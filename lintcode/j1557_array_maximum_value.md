https://www.lintcode.com/problem/1557/solution/27104

# solution 1

算法：dp + 前缀和

用一个数组dp[i] 表示 前i个数构成的子数组能够获得的最大价值

建立递推式的时候考虑两种情况

没有区间包含a[i]。那么b[i]不计入最大价值中，有 dp[i] = dp[i - 1]
存在一个区间[k , i] , 满足 k < i 且 a[k] = a[i]， 那么 dp[i] = max{dp[k-1] + (a[k] + a[k+1] + .. + a[i])} 显然可以预处理一个前缀数组sum[]来解决处理a[k]+a[k+1] + .. + a[i].
转移方程式就变成了：dp[i] = max{dp[k-1] + sum[i] - sum[k-1]} = sum[i] + max{dp[k-1] - sum[k-1]}

如果在 i 前面存在多个 k 满足 a[i] = a[k]，通过最大的 dp[k-1] - sum[k-1] 来转移dp方程。

用一个新数组value，即对于每一个出现的数a[k](这里用一个visit数组去记录是否出现新的a[k]),都维护一下 value[a[k]] = max{dp[k-1] - sum[k-1]}，那么遍历到a[i]时，只需要根据 value[a[i]]的值来转移即可，最后的答案就是dp[n]

复杂度分析

时间复杂度O(n)
n为数组的大小
空间复杂度O(n)
n为数组的大小

```python
MAXNUM = 1010
class Solution:
    """
    @param a: The array a
    @param b: The array b
    @return: Return the maximum value
    """
    def getAnswer(self, a, b):
        n = len(a)
        dp = [0] * (n + 1)
        pre = [0] * (n + 1)
        value = [0] * MAXNUM
        vis = [False] * MAXNUM
        # 前缀和
        for i in range(1,n + 1):
            pre[i] = pre[i - 1] + b[i - 1]
        for i in range(1,n + 1):
            # a[k]第一次出现
            if vis[a[i - 1]] == False:
                vis[a[i - 1]] = 1
                dp[i] = dp[i - 1]
                value[a[i - 1]] = dp[i - 1] - pre[i - 1]
            # a[k]非第一次出现
            else:
                dp[i] = max(dp[i - 1], value[a[i - 1]] + pre[i])
                value[a[i - 1]] = max(value[a[i - 1]], dp[i - 1] - pre[i - 1])
        return dp[n]
```

# solution 2
定义数组 dp[i] 表示 前i个数构成的子数组能够获得的最大价值。 则 dp[n] 即为我们需要输出的答案。

结合题意，求解dp[i]时需要考虑两种情况：

没有任何区间包含a[i]。那么b[i]最终不计入最大价值中，有 dp[i] = dp[i - 1]
存在一个区间[k , i] , 满足 k < i 且 a[k] = a[i]， 那么 dp[i] = max{dp[k-1] + (a[k] + a[k+1] + .. + a[i])}
如果处理一个前缀和数组， 记为sum，那么第二种情况的dp方程可以转化为：

dp[i] = max{dp[k-1] + sum[i] - sum[k-1]} = sum[i] + max{dp[k-1] - sum[k-1]}

故如果在 i 前面存在多个 k 满足 a[i] = a[k]， 我们只需要找到最大的 dp[k-1] - sum[k-1] 来转移dp方程。
这个可以使用一个新数组Mx来维护，即对于每一个出现的数a[k]，我们都维护一下： Mx[a[k]] = max{dp[k-1] - sum[k-1]}

那么遍历到a[i]时，只需要根据 Mx[a[i]]的值来转移即可。

时间复杂度: O(n)
```python
class Solution:
    """
    @param a: The array a
    @param b: The array b
    @return: Return the maximum value
    """
    def getAnswer(self, a, b):
        # Write your code here
        s = [0 for i in range(0, len(a))]
        dp = [0 for i in range(0, len(a))]
        same = [[] for i in range(0, 1010)]
        same[a[0]].append(0)
        s[0] = b[0]
        for i in range(1, len(a)):
        	s[i] = s[i - 1] + b[i]
        	same[a[i]].append(i)
        maxx = 0
        for j in range(1, len(same[a[0]])):
        	dp[same[a[0]][j]] = s[same[a[0]][j]]
        same[a[0]].pop(0)
        for i in range(1, len(a)):
        	if dp[i - 1] > maxx:
        		maxx = dp[i - 1]
        	for j in range(1, len(same[a[i]])):
        		if dp[same[a[i]][j]] < maxx + s[same[a[i]][j]] - s[i - 1]:
        			dp[same[a[i]][j]] = maxx + s[same[a[i]][j]] - s[i - 1]
        	same[a[i]].pop(0)
        if dp[len(a) - 1] > maxx:
        	maxx = dp[len(a) - 1]
        return maxx
```