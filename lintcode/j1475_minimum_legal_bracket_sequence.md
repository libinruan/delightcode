# solution 1
考虑将所有的"?"代替为")"，此时的代价为 \sum b[i]∑b[i] 随后遍历一遍，如果当前")"的数目已经超过"("的数目，则从前面所有出现过的"?"中选择一个替换代价最小的，将其变为"("，第i个"?"的替换代价为：a[i] - b[i]a[i]−b[i]。该过程可以使用优先队列或者线段树进行维护。 假设字符串长度为nn，则时间复杂度O(nlogn)O(nlogn)

```python
import Queue
class Solution:
    """
    @param s: The string s
    @param a: The cost array a
    @param b: the cost array b
    @return: Return the minimum cost
    """
    def getAnswer(self, s, a, b):
        # Write your code
        left = 0
        right = 0
        que = Queue.PriorityQueue()
        res = 0
        for i in b:
            res = res + i
        count = 0
        for i in range(0, len(s)):
            if s[i] == '(':
                left = left + 1
            if s[i] == ')':
                right = right + 1
            if s[i] == '?':
                que.put(a[count] - b[count])
                right = right + 1
                count = count + 1
                
            if right > left:
                if que.empty():
                    return -1;
                print(res)
                res = res + que.get()
                right = right - 1
                left = left + 1
        if right == left:
            return res
        else:
            return -1
```

# solution 2 線段樹
考虑将所有的"?"代替为")"，此时的代价为 \sum b[i]∑b[i] 随后遍历一遍，如果当前")"的数目已经超过"("的数目，则从前面所有出现过的"?"中选择一个替换代价最小的，将其变为"("，第i个"?"的替换代价为：a[i] - b[i]a[i]−b[i]。该过程可以使用优先队列或者线段树进行维护。 假设字符串长度为nn，则时间复杂度O(nlogn)O(nlogn)

```python
import Queue
class Solution:
    """
    @param s: The string s
    @param a: The cost array a
    @param b: the cost array b
    @return: Return the minimum cost
    """
    def getAnswer(self, s, a, b):
        # Write your code
        left = 0
        right = 0
        que = Queue.PriorityQueue()
        res = 0
        for i in b:
            res = res + i
        count = 0
        for i in range(0, len(s)):
            if s[i] == '(':
                left = left + 1
            if s[i] == ')':
                right = right + 1
            if s[i] == '?':
                que.put(a[count] - b[count])
                right = right + 1
                count = count + 1
                
            if right > left:
                if que.empty():
                    return -1;
                print(res)
                res = res + que.get()
                right = right - 1
                left = left + 1
        if right == left:
            return res
        else:
            return -1
```        

# solution 3
解题思路
关键在于想到这样的思路：先将?全部替换成)，再根据(和)的个数决定是否替换回来。
使用heap来做比较简单，线段树也是可以的（删除最小值的操作略微麻烦）。

题解代码

```python
from heapq import *

class Solution:
    """
    @param s: The string s
    @param a: The cost array a
    @param b: the cost array b
    @return: Return the minimum cost
    """
    def getAnswer(self, s, a, b):
        # Write your code here
        n = len(s)

        diff = 0 # count difference of '(' and ')'
        costs = []
        countQues = 0
        ret = sum(b)
        for i in range(n):
            if s[i] == '(':
                diff += 1
            else:
                diff -= 1

            if s[i] == '?':
                countQues += 1
                heappush(costs, a[countQues - 1] - b[countQues - 1])

            if diff < 0:
                if len(costs) > 0:
                    ret += heappop(costs)
                    diff += 2
                else:
                    break

        return ret if diff == 0 else -1
```    

# heapq + reduce dimension + heap
用 heapq 改写了一下 降维 + 堆的答案
```python
import heapq
class Solution:
    """
    @param s: The string s
    @param a: The cost array a
    @param b: the cost array b
    @return: Return the minimum cost
    """
    def getAnswer(self, s, a, b):
        # Write your code here
        heap = [] 
        answer = sum(b) 
        left, right = 0, 0 
        i = 0 
        for c in s: 
          if c == '(': 
            left += 1 
          elif c == ')': 
            right += 1 
          elif c == '?':
             heapq.heappush(heap, a[i] - b[i])
             i += 1 
             right += 1 
          
          if right > left: 
            if not heap: 
              return False 
            answer += heapq.heappop(heap) 
            left += 1 
            right -= 1 
        
        return answer if left == right else -1
```