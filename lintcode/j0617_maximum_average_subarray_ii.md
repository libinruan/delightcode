<!-- ------------------------------- DDBear -------------------------------- -->
算法：二分答案 I
solution: https://www.lintcode.com/problem/617/solution/17825?fromId=164&_from=collection
```python
# O(Nlog(max_val - min_val)), O(1)

class Solution:

    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        #设置二分的左右边界分别为数组中的最小值和最大值
        left, right = min(nums), max(nums)
        while left + 1e-5 < right:
            mid = left + (right - left) / 2
            #判断平均值mid是否可行
            #若可行则说明答案大于等于mid，那么左边界等于mid
            #否则说明答案小于mid，右边界等于mid
            if self.check(nums, k, mid):
                left = mid
            else:
                right = mid
        return left

    def check(self, nums, k, avg):
        #rightSum表示当前指向位置的前缀和
        #leftSum表示当前指向位置左侧k个位置的前缀和
        #minLeftSum表示左侧最小的前缀和
        rightSum = 0.0
        leftSum = 0.0 
        minLeftSum = 0.0
        for i in range(k):
            rightSum += nums[i] - avg
        for i in range(k, len(nums) + 1):
            if rightSum - minLeftSum >= 0:
                return True
            if i < len(nums):
                rightSum += nums[i] - avg
                leftSum += nums[i - k] - avg
                minLeftSum = min(minLeftSum, leftSum)
        return False
```

<!-- ------------------------------ Great Dog ------------------------------ -->
方法：二分查找 II
solution: https://www.lintcode.com/problem/617/solution/59492?fromId=164&_from=collection
```python
# O(Nlog(max_val - min_val)), O(1)
from typing import (
    List,
)

class Solution:
    def max_average(self, nums: List[int], k: int) -> float:
        max_val = max(nums)
        min_val = min(nums)
        prev_mid, error = max_val, float('inf')
        while error > 0.00001:
            mid = (max_val + min_val) / 2
            if self.check(nums, mid, k):
                min_val = mid
            else:
                max_val = mid
            error = abs(prev_mid - mid)
            prev_mid = mid
        return min_val
    
    def check(self, nums, mid, k):
        sums, prev, min_sums = 0, 0, 0
        for i in range(k):
            sums += nums[i] - mid
        if sums >= 0:
            return True
        for i in range(k, len(nums)):
            sums += nums[i] - mid
            prev += nums[i - k] - mid
            min_sums = min(prev, min_sums)
            if sums > min_sums:
                return True
        return False
```

<!-- ------------------------------ kailai27 ------------------------------- -->
方法：prefixSum

初看是一道普通的prefixSum题
但考察的prefixSum的剪枝

1.初级解法：
求出prefixSum,通过遍历所有可能的substring
打擂台的方式 求出(prefixSum[i] - prefixSum[j]) / (j - i) 的最小值
由于这个最小值中起决定性作用的有两个条件(prefixSum[i] - prefixSum[j]) 和(j - i)
所以无法用全循环保存最小值的情况来减枝,只能全部遍历所以.
时间复杂度即为完整遍历prefixSum: O(n^2)

2.高级解法：
即假设我们要求的平均值为target，当所有数同时减去target，我们可以去掉(j - i) 这个条件
因为当对所有数同时减去target时，/(j - i) 就变得没有意义了，我们只在乎大于0还是小于0

这样，我们的问题就可以转化为用二分法来寻找满足 target 最大 且满足有subrange为0的target，prefix 仅用作判断条件
时间复杂度为O(nlgn)

```python
class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        if nums is None or len(nums) < k:
            return -1
        
        start = min(nums)
        end = max(nums)
        
        while start + 1e-6 < end: # Leetcode: The answer with the calculation error less than 10-5 will be accepted. 
            mid = (start + end) / 2
            if self.has_bigger_avg(mid, nums, k):
                start = mid
            else:
                end = mid
        
        return start
    
    
    def has_bigger_avg(self, avg, nums, k):
        prefix_sum = [0]
        min_sum = sys.maxsize
        for i in range(len(nums)):
            prefix_sum.append(nums[i] - avg + prefix_sum[-1])
            if i < k - 1:
                continue
            min_sum = min(min_sum, prefix_sum[i + 1 - k])
            
            if prefix_sum[-1] - min_sum >= 0:
                return True
        
        return False
```