# two pointers
## version 1
two pointer
大擂台，相等就返回0；
不等就选最小的；

```python
class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        nums.sort()
        i, j = 0, len(nums)  - 1

        diff = sys.maxsize
        while i < j:
            if nums[i] + nums[j] < target:
                diff = min(diff, target - nums[i] - nums[j])
                i += 1
            else:
                diff = min(diff, nums[i] + nums[j] - target)
                j -= 1

        return diff
```

## version 2
url: https://www.lintcode.com/problem/533/solution/62434
```python
from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    # Method: Two-Pointer(approach)
    def two_sum_closest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1: return abs(nums[0] - target)

        res = sys.maxsize
        nums.sort() 
        l, r = 0, n - 1
        while l < r:
            x = nums[l] + nums[r]
            if x > target:
                res = min(res, abs(x - target))
                r -= 1
            elif x < target:
                res = min(res, abs(x - target))
                l += 1
            else:
                return 0 
        
        return res
```


## version 3
https://www.lintcode.com/problem/533/solution/57414
```python
    def two_sum_closest(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        min_diff = float('inf')
        while left < right:
            min_diff = min(min_diff, abs(target - nums[left] - nums[right]))
            if nums[left] + nums[right] == target:
                return 0
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1      
        return min_diff
```