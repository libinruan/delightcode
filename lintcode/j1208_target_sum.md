回溯
```python
class Solution:
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)
```

动态规划 I
```python
from typing import (
    List,
)
class Solution:
    def find_target_sum_ways(self, nums: List[int], s: int) -> int:
        diff = sum(nums) - s
        if diff < 0 or diff % 2: return 0
        n, neg = len(nums), diff >> 1
        dp = [[0 for _ in range(neg + 1)] for __ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(neg + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num: dp[i][j] += dp[i - 1][j - num]
        return dp[n][neg]
```

动态规划 II 使用滚动数组的方式
```python
from typing import (
    List,
)
class Solution:
    def find_target_sum_ways(self, nums: List[int], s: int) -> int:
        diff = sum(nums) - s
        if diff < 0 or diff % 2: return 0
        neg = diff >> 1
        dp = [0 for _ in range(neg + 1)]
        dp[0] = 1
        for num in nums:
            for j in range(neg, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[neg]
```

DFS
```python
class Solution(object):
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)
```