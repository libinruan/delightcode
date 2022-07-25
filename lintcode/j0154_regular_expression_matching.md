# answer 1 - 和 Wildcard Matching 同样模板的代码。使用了记忆化搜索（Memoization Search）
# https://www.lintcode.com/problem/154/solution/16738
class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, source, pattern):
        return self.is_match_helper(source, 0, pattern, 0, {})
        
        
    # source 从 i 开始的后缀能否匹配上 pattern 从 j 开始的后缀
    # 能 return True
    def is_match_helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        # source is empty
        if len(source) == i:
            return self.is_empty(pattern[j:])
            
        if len(pattern) == j:
            return False
            
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1, pattern, j, memo) or \
                self.is_match_helper(source, i, pattern, j + 2, memo)
        else:                
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1, pattern, j + 1, memo)
        
        memo[(i, j)] = matched
        return matched
        
        
    def is_match_char(self, s, p):
        return s == p or p == '.'
        
    def is_empty(self, pattern):
        if len(pattern) % 2 == 1:
            return False
        
        for i in range(len(pattern) // 2):
            if pattern[i * 2 + 1] != '*':
                return False
        return True



# answer 2
# https://www.lintcode.com/problem/154/solution/17132
class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    hash = None
    def isMatch(self, s, p):
        if self.hash is None:
            self.hash = {}
        key = s + p					
        if key in self.hash:
            return self.hash[key]
            
        if p == '':              #如果p串为空
            return s == ''		 #判断s串是否为空
        if s == '':              #如果s串为空
            if len(p) % 2 == 1:  
                return False
            i = 1
            while i < len(p):    #需要满足"x*x*"的形式
                if p[i] != '*':
                    return False
                i += 2
            return True
        
        if len(p) > 1 and p[1] == '*':   #如果p串中的当前字符为'*'
            if p[0] == '.':              #如果p中为.
                self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[2:]) #.去匹配s[0]并且''||.和*不去匹配，用p[2]匹配
            elif p[0] == s[0]:							
                self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[2:]) 
            else:
                self.hash[key] = self.isMatch(s, p[2:])  
        elif p[0] == '.':
            self.hash[key] = self.isMatch(s[1:], p[1:])  #继续向下匹配
        else:
            self.hash[key] = s[0] == p[0] and self.isMatch(s[1:], p[1:])  #继续向下匹配
        
        return self.hash[key]

class Solution(object):
    # DP
    def isMatch(self, s, p):
        dp = [[False for i in range(0,len(p) + 1)] for j in range(0, len(s) + 1)]
        dp[0][0] = True   #dp[0][0]初始化为true，由此开始转移
        for i in range(1, len(p) + 1):
            if (p[i - 1] == '*'):		
                dp[0][i] = dp[0][i - 2]  
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':     
                    dp[i][j] = dp[i][j - 2]    
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':  #'*'不去匹配
                        dp[i][j] |= dp[i-1][j]
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':  #如果两字符相同或者为.
                        dp[i][j] = dp[i - 1][j - 1]    #当前状态由前一个转移而来
    
        return dp[len(s)][len(p)]

    # 懒癌版
    def isMatch(self, s, p):
        return re.match(p + '$', s) != None      



# answer 3 DP
# https://www.lintcode.com/problem/154/solution/56953
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]       



# answer 4 DP + one-dimensional array
# https://www.lintcode.com/problem/154/solution/17873
class Solution:
    
    def isMatch(self, query, pattern) -> bool:
        
        m, n = len(query), len(pattern)
        
        f = [False for _ in range(n+1)]
        f[0] = True
        for j in range(2, n+1, 2):
            f[j] = f[j-2] if pattern[j-1] is '*' else f[j]
        
        for i in range(1, m+1):
            upper_left, f[0] = f[0], False
            for j in range(1, n+1):
                top = f[j]
                if pattern[j-1] is '*':
                    f[j] = f[j-2] 
                    f[j] |= top and (pattern[j-2] is query[i-1] or pattern[j-2] is '.')
                elif pattern[j-1] is query[i-1] or pattern[j-1] is '.':
                    f[j] = upper_left
                else:
                    f[j] = False # can't leave out this since there is no setting cells to False globally
                upper_left = top 
        
        return f[n] 