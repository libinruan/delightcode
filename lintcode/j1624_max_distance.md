# BFS by DDBear
https://www.lintcode.com/problem/624/solution/17860
```python
class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        visited = {}
        queue = collections.deque()
        queue.append(s)
        # 初始化为极大值
        ans = sys.maxsize
        while len(queue) > 0:
            s = queue.popleft()
            for word in dict:
                pos = s.find(word)
                while pos != -1:
                    if s == word:
                        ans = 0
                        break
                    # tvisited为删除下标pos开始的word之后的字符串
                    tvisited = s[:pos] + s[pos + len(word):]
                    # 如果这个字符串没有出现过，压入队列，更新答案
                    if tvisited not in visited:
                        visited[tvisited] = 1
                        # 更新剩下的字符串的最短长度
                        ans = min(ans, len(tvisited))
                        queue.append(tvisited)
                    # 寻找s中下标从pos+1开始到末尾第一次出现的word的首下标
                    pos = s.find(word, pos + 1)
            if ans == 0:
                break
        return ans
```

# BFS varaint 1
```python
class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    
    def minLength(self, s, dict):
        # write your code here
        queue = collections.deque([s])
        visited = set([s])
        answer = len(s)
        while queue:
            cur_str = queue.popleft()
            answer = min(answer, len(cur_str))
            for sub_str in self.find_substrings(cur_str, dict):
                if sub_str not in visited:
                    visited.add(sub_str)
                    queue.append(sub_str)
        return answer
        
    def find_substrings(self, s, dict):
        results = []
        for word in dict:
            found = s.find(word)
            while found != -1:
                substring = s[:found] + s[found + len(word):]
                results.append(substring)
                found = s.find(word, found + 1) # searching start from found + 1
        return results
```

# Memorized DFS
https://www.lintcode.com/problem/624/solution/58447
```python
class Solution:
    """
    @param s: a string
    @param dict: a set of n substrings
    @return: the minimum length
    """
    def min_length(self, s: str, dict: Set[str]) -> int:
        @lru_cache(None)
        def dfs(s):
            res = len(s)
            for sub in dict:
                pos = s.find(sub)
                while pos != -1:
                    new_str = s[:pos] + s[pos + len(sub):]
                    res = min(res, dfs(new_str))
                    pos = s.find(sub, pos + 1)
            return res
        
        return dfs(s)
```


# DFS variant 1
https://www.lintcode.com/problem/624/solution/23788
```python
def minLength(self, s, word_dict):
    # write your code here
    visited = set([s])
    self.min_len = len(s)
    self.dfs(s, word_dict, visited)
    return self.min_len

def dfs(self, s, word_dict, visited):
    if s == '':
        return 0
    all_next = []
    # Find all substrings after remove one item in word_dict
    for item in word_dict:
        pos = s.find(item, 0)
        while pos != -1:
            all_next.append(s[: pos] + s[pos + len(item): ])
            pos = s.find(item, pos + len(item))
     
    for next_s in all_next:
        if next_s in visited:
            continue
        self.min_len = min(self.min_len, len(next_s))
        visited.add(next_s)
        self.dfs(next_s, word_dict, visited)
```