# JZ: https://www.lintcode.com/problem/107/solution/16631

# DP
# state: dp[i] 表示前 i 个字符是否能够被划分为若干个单词
# function: dp[i] = or{dp[j] and j + 1~i 是一个单词}

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, wordSet):
        if not s:
            return True
            
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        max_length = max([
            len(word)
            for word in wordSet
        ]) if wordSet else 0
        
        for i in range(1, n + 1):
            for l in range(1, max_length + 1):
                if i < l:
                    break
                if not dp[i - l]:
                    continue
                word = s[i - l:i]
                if word in wordSet:
                    dp[i] = True
                    break
        
        return dp[n]

# brute force

# 方法1:暴力
# 对于这道题，我们首先考虑暴力的方法。本题相当于用多个字符串组成该字符串，那么我们就枚举所有可能的放入字符串的方法，通过深度优先搜索，尝试所有可能。
# 对于一个字符串，考虑这个字典中的单词是否是当前字符串的前缀。若不是，则跳过该单词。若是则将该前缀从字符串中删除后，判断剩下的字符串能否由字典里的单词组成。
# 由于题目的数据加强，此题已经无法使用常规的DFS方式通过，我们更推荐更优秀的DP来实现。

# 代码思路
# 使用深度优先搜索，记录字符串，字典，以及当前需要判断的字符串的起始点
# 从当前字符串的起始点开始判断

# 代码框架
# 定义dfs
#     递归的出口
#     如果起始点已经在字符串的尾部
#         停止，返回可以组成该字符串
#     如果还未到结尾，枚举下一个字符串。
#         对于每种可能，判断该字符串是否是原字符串的前缀
#         如果是前缀：
#             取出该字符串，判断剩下的是否可以
#     找完所有可能后，仍然不行，直接返回这段字符串无法找到答案
    
    
# 时间复杂度：O(2^n)，考虑当s = "aaaaaaaaaaab", dict = {"a", "aa", "aaa", ...., "aaaaaaaaa"}
# 空间复杂度：O(N)，递归深度最深为N层

# 相关问题：
# LintCode 582. Word Break II
# LintCode 683. Word break III
# LintCode 123. Word Search

# 相关课程
# 本题在JZ算法班、JZ算法高频题班中均有讲解。
# JZ算法班：https://www.jiuzhang.com/course/1/
# JZ算法高频题班：https://www.jiuzhang.com/course/9/

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        if len(s) == 0:
            return True
        return self.dfs(0, s, dict)
    
    # 递归的定义
    # 判断s[start_index: ]可以由dict中的单词组成
    def dfs(self, start_index, s, dict):
        # 递归的出口
        if start_index == len(s):
            return True
        
        # 递归的拆解
        for word in dict:
            if start_index + len(word) > len(s):
                continue 
            
            if s[start_index: start_index + len(word)] == word:
                # 判断s[start_index + len(word)] 是否满足条件
                if self.dfs(start_index + len(word), s, dict):
                    return True 
        return False

# DP

# 這題是很經典的dp 透過建立長度為n + 1的dp list
# dp[j]若為True 表示該數列可以透過dictionary組出0~j的字串
# dp = [False for _ in xrange(n + 1)]
# dp的狀態為：
# 從字的起點j 到字的終點i
# 如果可以透過dictionary組出0~j的字串(dp[j] == True)且s[j:i]在dictionary裡面
# 則可推出dp[i]是True
# 最後回傳dp[n]
# 這題的優化在兩個地方

# 若dp[i]已經為真 就break掉不需要剩下的計算 -> 原因是我們只需要知道有一種方法可以走到i即可
# 從i往回走j的長度最多也只可能是i-maxLen -> 不可能有比maxLen更長的dictionary key
# 沒有這兩個優化都會TLE

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if not s:
            return True
        if not dict:
            return False
        n = len(s)
        dp = [False for _ in xrange(n + 1)]
        maxLen = max([len(w) for w in dict])
        dp[0] = True
        for i in xrange(1, n + 1):
            for j in xrange(max(i - maxLen, 0), i):
                if not dp[j]:
                    continue
                if s[j:i] in dict:
                    dp[i] = True
                    break
        return dp[n]        