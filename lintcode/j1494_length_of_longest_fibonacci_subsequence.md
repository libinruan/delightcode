# Dynamic programming 1
sol: https://www.lintcode.com/problem/1494/solution/58026
```python
from typing import (
    List,
)

class Solution:
    """
    @param a: 
    @return: the length
    """
    def lengthof_longest_fibonacci_subsequence(self, a: List[int]) -> int:
        # Write your code here.
        index = {x: i for i, x in enumerate(a)}
        longest = collections.defaultdict(lambda: 2)

        ans = 0
        for k, z in enumerate(a):
            for j in range(k):
                i = index.get(z - a[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0
```



# Brute force - Set
sol: https://www.lintcode.com/problem/1494/solution/58023
```python
from typing import (
    List,
)

class Solution:
    """
    @param a: 
    @return: the length
    """
    def lengthof_longest_fibonacci_subsequence(self, a: List[int]) -> int:
        # Write your code here.
        S = set(a)
        ans = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                x, y = a[j], a[i] + a[j]
                length = 2
                while y in S:
                    x, y = y, x + y
                    length += 1
                ans = max(ans, length)
        return ans if ans >= 3 else 0
```



# Array, Binary Search
sol: https://www.lintcode.com/problem/1494/solution/30407
```python
class Solution:
    """
    @param A: 
    @return: the length
    """
    def binarySearch(self,begin,end,target,A):
        while begin <= end:
            mid = int((end - begin) / 2) + begin;
            if A[mid] == target: 
                return mid;
            elif A[mid] > target:
                end = mid - 1;
            else:
                begin = mid + 1;
        return -1;
    def lengthofLongestFibonacciSubsequence(self, A):
        # Write your code here
        if len(A) <= 2:
            return len(A);
        maxLen = -1;
        for i in range(0,len(A) - 2):
            for j in range(i + 1, len(A)):
                l = 2;
                k = j + 1;
                pre = A[i];
                cur = A[j];
                while k < len(A):
                    mid = self.binarySearch(k, len(A) - 1, pre + cur, A);
                    print(mid)
                    if not mid == -1:
                        l += 1;
                        pre = cur;
                        cur = A[mid];
                        k = mid + 1;
                    else:
                        break;
                maxLen = max(l,maxLen);
        if maxLen >= 3: 
            return maxLen;
        else: 
            return 0;
        return 0;
```



# Hashmap + DP*
sol: https://www.lintcode.com/problem/1494/solution/33028
```python
class Solution:
    """
    @param A: 
    @return: the length
    """
    def lengthofLongestFibonacciSubsequence(self, A):
        # 最长的斐波拉契数列长度初始化为2
        n,maxLen = len(A),2
        # hashMap[num]记录num在A中的下标
        um = dict()
        # 将A中的每个元素值与下标关联起来
        for i in range(n):
            um[A[i]] = i;
        # dp[i][j]记录以元素i、j结尾的斐波拉契数列的长度
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1,n):
                # 只有没有查找过的时候才有必要查找，否则会重复
                if dp[i][j] == 0:
                    x,y,nextVal = i,j,A[i] + A[j]
                    dp[x][y] = 2
                    # 如果A中存在nextVal（下一个元素），继续往下递推出下一个元素
                    while nextVal in um:
                        # 获取下一个元素的下标
                        z = um[nextVal]
                        # 由于又寻找到了一个元素，所以标记以A[y]、A[z]结尾的元素已经找到
                        dp[y][z] = dp[x][y] + 1
                        # 更新下标，为下一次求下一个元素的下一个元素做准备
                        x = y
                        y = z
                        # 当前下一个需要寻找的元素
                        nextVal = A[x] + A[y]
                    # 更新最大长度
                    if dp[x][y] > maxLen:
                        maxLen = dp[x][y]
        if maxLen == 2:
            return 0
        return maxLen
```