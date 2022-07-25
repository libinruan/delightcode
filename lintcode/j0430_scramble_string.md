# anaswer 1
# https://www.lintcode.com/problem/430/solution/20067
class Solution:
    def isScramble(self, s1, s2):
        n = len(s1)
        # f[i][j][k] 表示 s1[i : i + k] 攀爬能否得到 s2[j : j + k]
        f = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                f[i][j][1] = s1[i] == s2[j]
        for k in range(2, n + 1):
            for i in range(0, n - k + 1):
                for j in range(0, n - k + 1):
                    for t in range(1, k):
                        if f[i][j][t] and f[i + t][j + t][k - t]:
                            f[i][j][k] = True
                            break
                        if f[i][j + k - t][t] and f[i + t][j][k - t]:
                            f[i][j][k] = True
                            break
        return f[0][0][n]
        
class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(list(s1)) != sorted(list(s2)):
            return False
        length = len(s1)
        for i in range(1, length):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[length-i:]) and self.isScramble(s1[i:], s2[:length-i]):
                return True
        return False



# answer 2
# https://www.lintcode.com/problem/430/solution/18547
class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """
    def isScramble(self, s1, s2):
        size = len(s1)
        if size != len(s2):
            return False
        # 非字符集合相等的提前剪枝
        sort_s1 = sorted(s1)
        sort_s2 = sorted(s2)
        if sort_s1 != sort_s2:
            return False
        # dp[n][i][j]表示s1[i..i+n-1]和s2[j..j+n-1]两个子串是否是scramble的
        # 迭代起点，对长度为1的直接比较计算出结果; 其他的初始化为false
        dp = [[[False for _ in range(size)] for _ in range(size)] for _ in range(size+1)]
        for i in range(size + 1):
            for j in range(size):
                for k in range(size):
                    if i == 0 or i == 1 and s1[j] == s2[k]:
                        dp[i][j][k] = True
                    else:
                        dp[i][j][k] = False
        # 依次计算长度更大的, 对于长度为n的情况，直接看所有的子串划分情况是否有一个满足的
        # 由于n是递增的，因此子串的都是已经计算过的
        for n in range(2,size + 1):
            for i in range(size - n + 1):
                for j in range(size - n +1):
                    # 计算长度为n的, s1[i, i+n-1]和s2[j, j+n-1]是否是scramble的
                    # 通过遍历所有子串划分是否存在有一个满足即可
                    for k in range(1,n):# k是s1部分的左子串的长度
                        if dp[k][i][j] and dp[n-k][i+k][j+k] or dp[k][i][j+n-k] and dp[n-k][i+k][j]:
                            dp[n][i][j] = True
                            break
        # 最后结果就是s1[0,size]和s2[0,size]是否匹配
        return dp[size][0][0]



# answer 3
# https://www.lintcode.com/problem/430/solution/17800
class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """
    def isScramble(self, s1, s2):
        # write your code here
        return self.dfs(s1, s2, {})
    
    def dfs(self, s1, s2, memo):
        
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        
        if len(s1) != len(s2):
            return False
        
        if s1 == s2:
            return True
        
        s1_list = list(s1)
        s2_list = list(s2)
        if s1_list.sort() != s2_list.sort():
            return False
        
        for i in range(1, len(s1)):
            if (self.dfs(s1[:i], s2[:i], memo) and self.dfs(s1[i:], s2[i:], memo)) or (self.dfs(s1[:i], s2[-i:], memo) and self.dfs(s1[i:], s2[:-i], memo)):
                memo[(s1, s2)] = True
                return True
        
        memo[(s1, s2)] = False
        return False        



# answer 4
# https://www.lintcode.com/problem/430/solution/34013
# 记忆化搜索非常好理解。
# s1 只会做 2 件事：（1）分割；（2）交换。
# s1 和 s2 的匹配问题的子问题就是：在 s1 中能不能找到一个分割点 k，使得 s1[:k] == s2[:k] and s1[k:] == s2[k:]（没交换）或 s1[:k] == s2[(n-k):n] and s1[k:] == s2[:(n-k)]（交换过）？
# 对于这两个串，有 n^2 * n^2 = n^4 种子串匹配方案。
# 配上一个记忆化的表，就能很方便地写出记忆化搜索（递归）
class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """
    def isScramble(self, s1, s2):
        n = len(s1)

        f = dict()

        f[(0, 0, 0, 0)] = True

        return self.dfs(s1, s2, 0, n, 0, n, f)
    
    def dfs(self, s1, s2, i1, j1, i2, j2, f):
        if (i1, j1, i2, j2) in f:
            return f[(i1, j1, i2, j2)]
        elif j1 - i1 != j2 - i2:
            f[(i1, j1, i2, j2)] = False
            return f[(i1, j1, i2, j2)]
        elif i1 + 1 == j1:
            f[(i1, j1, i2, j2)] = s1[i1] == s2[i2]
            return f[(i1, j1, i2, j2)]
        else:
            for k in range(i1 + 1, j1):
                if self.dfs(s1, s2, i1, k, i2, i2 + (k - i1), f) and \
                    self.dfs(s1, s2, k, j1, i2 + (k - i1), j2, f):
                    f[(i1, j1, i2, j2)] = True
                    return f[(i1, j1, i2, j2)]
                if self.dfs(s1, s2, i1, k, j2 - (k - i1), j2, f) and \
                    self.dfs(s1, s2, k, j1, i2, j2 - (k - i1), f):
                    f[(i1, j1, i2, j2)] = True
                    return f[(i1, j1, i2, j2)]
            f[(i1, j1, i2, j2)] = False
            return f[(i1, j1, i2, j2)]