# two pointers

## variant 1
url: https://www.lintcode.com/problem/443/solution/19344
```python
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        if len(nums) < 2 or not nums :
            return 0
        
        nums.sort()
        
        count = 0
        l, r = 0, n - 1
        while l < r:
            if nums[l] + nums[r] <= target:
                l += 1
            else:
                count += r - l
                r -= 1
                
        return count
```

## variant 2 (DDBear)
https://www.lintcode.com/problem/443/solution/24304
```python

class Solution:

    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """

    def twoSum2(self, nums, target):
        n = len(nums)
        nums.sort()
        result = 0
        l, r = 0, n - 1
        while l < r:
            #若l指向元素与r指向元素的和不大于target
            if nums[l] + nums[r] <= target:
                l += 1
            #否则，nums[r]可以与nums[l + 1 : r + 1]这r - l个元素配对
            else:
                result += r - l
                r -= 1
        return result
```