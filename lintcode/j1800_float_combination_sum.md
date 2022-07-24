# answer 1
sol: https://www.lintcode.com/problem/1800/solution/62457

考点：

dp

题目分析：

本题是一道常见的背包题目。题中显性的提示了target，如果背包题目做的比较多的同学应该能快速联想到动态规划的解法。更进一步的，这道题可以认为是一个分组背包问题，每个数字可以看成是包含两个互斥的物品放入。具体来说，对于每个小数，看作是向上取整和向下取整的两个物品，必须选择一个，考虑分组背包。在第二层循环即背包容量的循环中同时考虑两个物品，则可保证选择具有互斥性。

具体而言，假设dp矩阵代表了调整所需的最小和，i代表当前第i个物品，j代表当前的权重，x为当前矩阵元素A[i]，A代表了floor（x）, B代表了ceil（x）我们有

dp[j] = max(dp[j-A]+x-A, dp[j-B]+x-B)， 给定j>A and j>B

因此，我们只需要遍历两层循环，即可找到最小调整和。

但是本题的要求是，找到给定最小调整和情况下，对应的每个元素。因此需要额外引入一个矩阵path，来记录具体的位置信息。具体而言，该矩阵初始化为0，每次选择对应dp矩阵的分支，可以分别赋值为1,2。最后在找到最小调整和之后，根据结果进行回溯，即可确定对应位置上的数字。

假定给定输入为A=[1.2, 1.7]，这里给出一个示意图。



```python3
class Solution:
    """
    @param A: 
    @param target: 
    @return: nothing
    """
    def getArray(self, A, target):
        dp=[100000.0 for i in range(target + 1)]
        path = [[0 for i in range(len(A) + 1)]for i in range(target + 1)]
        res = [0 for i in range(len(A))]
        n = len(A)
        dp[0] = 0.0
        for i in range(n) :
            for j in range(target,-1,-1) :
                x , y = math.floor(A[i]) , math.ceil(A[i])
                if j < x and j < y :
                    break
                if j >= x and j >= y :					#两个物品均可以放入，必选其一
                    if dp[j - x] + A[i] - x < dp [j - y] + y - A[i] :
                        dp[j] = dp[j - x] + A[i] - x
                        path[j][i] = 1
                    else :
                        dp[j] = dp[j - y] + y - A[i]
                        path[j][i] = 2
                elif j >= x:							#只能放入向下取整整数，直接放入
                        dp[j] = dp[j - x] + A[i] - x
                        path[j][i] = 1
                elif j >= y:							#只能放入向上取整整数，直接放入
                        dp[j] = dp[j - y] + y - A[i]
                        path[j][i] = 2
        if dp[target] >= 10000 :
            return res
        else :
            ssum = target
            for i in range(n - 1,-1,-1) :		#答案的记录此处通过对背包状态回溯完成还原(同样可以参考背包路径问题)。
                if path[ssum][i] == 1 :
                    res[i] = math.floor(A[i])
                    ssum -= math.floor(A[i])
                elif path[ssum][i] == 2 :
                    res[i] = math.ceil(A[i])
                    ssum -= math.ceil(A[i])
        return res
```

