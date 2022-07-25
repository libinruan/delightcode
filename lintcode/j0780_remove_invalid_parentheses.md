# answer 1
# https://www.lintcode.com/problem/780/solution/56903
from typing import (
    List,
)

class Solution:
    """
    @param s: The input string
    @return: Return all possible results
             we will sort your return value in output
    """
    def remove_invalid_parentheses(self, s: str) -> List[str]:
        # Write your code here
        res = []
        lremove, rremove = 0, 0
        for c in s:
            if c == '(':
                lremove += 1
            elif c == ')':
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

        def isValid(str):
            cnt = 0
            for c in str:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def helper(s, start, lremove, rremove):
            if lremove == 0 and rremove == 0:
                if isValid(s):
                    res.append(s)
                return

            for  i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue
                # 如果剩余的字符无法满足去掉的数量要求，直接返回
                if lremove + rremove > len(s) - i:
                    break
                # 尝试去掉一个左括号
                if lremove > 0 and s[i] == '(':
                    helper(s[:i] + s[i + 1:], i, lremove - 1, rremove);
                # 尝试去掉一个右括号
                if rremove > 0 and s[i] == ')':
                    helper(s[:i] + s[i + 1:], i, lremove, rremove - 1);
                # 统计当前字符串中已有的括号数量

        helper(s, 0, lremove, rremove)
        return res



# answer 2
# https://www.lintcode.com/problem/780/solution/56905
from typing import (
    List,
)

class Solution:
    """
    @param s: The input string
    @return: Return all possible results
             we will sort your return value in output
    """
    def remove_invalid_parentheses(self, s: str) -> List[str]:
        # Write your code here
        def isValid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        ans = []
        currSet = set([s])

        while True:
            for ss in currSet:
                if isValid(ss):
                    ans.append(ss)
            if len(ans) > 0:
                return ans
            nextSet = set()
            for ss in currSet:
                for i in range(len(ss)):
                    if i > 0 and ss[i] == s[i - 1]:
                        continue
                    if ss[i] == '(' or ss[i] == ')':
                        nextSet.add(ss[:i] + ss[i + 1:])
            currSet = nextSet
        return ans



# answer 3
# https://www.lintcode.com/problem/780/solution/16759
from collections import deque
class Solution:
    def removeInvalidParentheses(self, s):
        if not s:
            return ['']
        queue = deque([s])
        result, visited = [], set([s])
        found = False
        while queue:
            cur = queue.popleft()
            if self.is_valid_parentheses(cur):
                found = True
                result.append(cur)
            elif not found:
                for i in range(len(cur)):
                    if cur[i] == '(' or cur[i] == ')':
                        t = cur[:i] + cur[i + 1:]
                        if t not in visited:
                            queue.append(t)
                            visited.add(t)
        return result
        
    def is_valid_parentheses(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1 
            elif c == ')':
                if cnt == 0:
                    return False
                cnt -= 1 
        return cnt == 0         
