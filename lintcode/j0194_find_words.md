<!-- ----------------------- hashmap + binary search ----------------------- -->
解题思路：哈希表 + 二分
当check每一个dict中的单词word时，对其每一个字符c，找到齐在str中第一次出现位置（下标满足≥start）
```python

class Solution:
    """
    @param str: the string
    @param dict: the dictionary
    @return: return words which  are subsequences of the string
    """
    def find_words(self, str: str, dict: List[str]) -> List[str]:
        def check(word, dic):
            start = 0  # ≥start
            for c in word:
                if c not in dic or start > dic[c][-1]:
                    return False
                idx = bisect.bisect_left(dic[c], start)
                start = dic[c][idx] + 1
            return True
        
        dic = collections.defaultdict(list)
        for i, c in enumerate(str):
            dic[c].append(i)
        return [word for word in dict if check(word, dic)]

```

<!-- --------------------- hashmap + binary serach II ---------------------- -->

Hash Map记录每个字母在大数组的所有位置，然后每个单词字符进行遍历，按顺序找字符在大数组出现的合法最小位置，找不到就跳过找下个词，都能找到就输出到结果。

位置数组有序，用自带的biscert轮子进行二分查找。for else控制流程很好用。

```python
from typing import (
    List,
)
import collections, bisect

class Solution:
    """
    @param str: the string
    @param dict: the dictionary
    @return: return words which  are subsequences of the string
    """
    def find_words(self, str: str, dict: List[str]) -> List[str]:
        # write your code here.
        dic = collections.defaultdict(list)
        result = []
        for i, char in enumerate(str):
            dic[char].append(i)
        for string in dict:
            pointer = -1
            for c in string:
                positions = dic[c]
                # find one closest number bigger than pointer in positions
                if not positions or positions[-1] < pointer: break
                pointer = positions[bisect.bisect(positions, pointer)]
            else:
                result.append(string)
        return result
```        

<!-- --------------------- hashmap + binary search III --------------------- -->
目前为止领扣Python3提交最快的。

要点，不用defaultdict，用setdefault，这样必要时可以激发KeyError

Pythonic，ask for forgiveness，not permission
函数化编程，易读，算法一目了然

```python
class Solution:
    
    def findWords(self, string, words):
        
        query = {}
        for i, c in enumerate(string):
            query.setdefault(c, []).append(i)
            
        def found(word):
            from bisect import bisect
            last = -1
            for c in word:
                try:
                    last = query[c][bisect(query[c], last)]
                except (IndexError, KeyError):
                    return False
            return True
        
        return list(filter(found, words))
```

<!-- ---------------------------- two pointers ----------------------------- -->
最暴力的，用双指针，对于每个单词loop一边string，这样下来假设string长n, dict单词数量m, 时间复杂度 O(n*m)

First optimization is to use a defaultdict to store each char's index.
And when we loop through the word from the dictionary, we can use binary search to find the index for the current char,
note that the index needs to be greater than the current index. This way we can achieve Time: O(m * lgn) space: O(n).

Second optimization is to use a matrix to store only the next char's index for each element in the string.
nextpos[2][0]=3 means at position 2, next 'a' will be at index 3.
nextpos[3][1]=4 means at position 3, next 'b' will be at index 4.
This way we can find next char's index at Time: O(1) Space(O(n^2))

```python
# brute force: use two pointers, for every word in dict, compare head to toe, O(n)
# opt 1: use defaultdict, key=cha, value=index1, index2. use binary search find next.O(lgn)
# opt 2: use matrix array, for each pos, store next char position for all 26 char. O(1)

class Solution:
    """
    @param str: the string
    @param dict: the dictionary
    @return: return words which  are subsequences of the string
    """
# opt 2
    def findWords(self, str, dict):
        if not str or not dict:
            return []
        n, ans = len(str), []
        nextpos = [[n] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(26):
                nextpos[i][j] = nextpos[i + 1][j]
                if ord(str[i]) - ord('a') == j:
                    nextpos[i][j] = i 
                    
        for word in dict:
            i, j, m = 0, 0, len(word)
            while i < n and j < m:
                i = nextpos[i][ord(word[j]) - ord('a')] + 1 
                if i == n + 1:
                    break
                j += 1 
            if j == m:
                ans.append(word)
        return ans 
#   opt1  
    def findWords(self, str, dict):
        # Write your code here.
        if not str or not dict:
            return []
        mapping = collections.defaultdict(list)
        for i in range(len(str)):
            mapping[str[i]].append(i)
        ans = []
        for word in dict:
            cur_index = -1
            for i in range(len(word)):
                ch = word[i]
                if ch not in mapping:
                    break 
                ch_list = mapping[ch]
                pos = self.binary_search(ch_list, cur_index)
                if pos == -1:
                    break
                # print(word[i], ch_list, pos, cur_index)
                cur_index = pos
                if i == len(word) - 1:
                    ans.append(word)
        return ans 
    
    def binary_search(self, ch_list, cur_index):
        if not ch_list:
            return -1 
        start, end = 0, len(ch_list) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2
            if ch_list[mid] <= cur_index:
                start = mid
            else:
                end = mid 
        if ch_list[start] > cur_index:
            return ch_list[start] 
        if ch_list[end] > cur_index:
            return ch_list[end] 
        return -1
```