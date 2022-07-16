"""简单递归解法，最坏情况2^n。利用函数本身做dfs，当长度相加不等直接返回false,当一个string为空，直接判断另外一个string是否等于合并string。
然后根据第一个字符相等情况决定下一步递归输入。

DP - https://www.lintcode.com/problem/29/solution/19259?fromId=164&_from=collection
"""
class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3

        ans1 = False
        ans2 = False
        if s1[0] == s3[0]:
            ans1 = self.isInterleave(s1[1:], s2, s3[1:])
            
        if s2[0] == s3[0]:
            ans2 = self.isInterleave(s1, s2[1:], s3[1:])
            
        return ans1 or ans2


"""
动态规划递推加静态一维数组，当一个字符串为空是，只要直接比较另两个字符串就好了，你要是用滚动数组，面试的时候我保证你初始化会写错。
O(nm), O(m) where m is the length of s2.
"""
class Solution:
    
    def isInterleave(self, s1, s2, s3) -> bool:
        
        m, n = len(s1), len(s2)
        if m + n != len(s3): return False
        if m == 0 or n == 0: 
            return s1 == s3 or s2 == s3
        
        dp = [True] + [False for _ in range(n)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[j] = dp[j] and s1[i-1] is s3[i+j-1] or dp[j-1] and s2[j-1] is s3[i+j-1]

        return dp[n]


"""
DP + dynamic array optimization - https://www.lintcode.com/problem/29/solution/56333?fromId=164&_from=collection
O(nm), O(nm)
"""
class Solution:
    def is_interleave(self, s1: str, s2: str, s3: str) -> bool:
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)
        if(len1+len2!=len3):
            return False
        dp=[[False]*(len2+1) for i in range(len1+1)]
        dp[0][0]=True
        for i in range(1,len1+1):
            dp[i][0]=(dp[i-1][0] and s1[i-1]==s3[i-1])
        for i in range(1,len2+1):
            dp[0][i]=(dp[0][i-1] and s2[i-1]==s3[i-1])
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                dp[i][j]=(dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        return dp[-1][-1]