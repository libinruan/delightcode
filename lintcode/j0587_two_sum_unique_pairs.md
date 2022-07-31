# Hashmap
url: https://www.lintcode.com/problem/587/solution/17125
```python
class Solution:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if len(nums) <= 1:
            return 0
        used = {}
        num = 0
        for each in nums:
            if target - each in used and used[target - each] == 0:
                num += 1
                used[target - each] = 1
                used[each] = 1
            if each not in used:
                used[each] = 0
        return num
```


# Sorting, array
## version 1
url: https://www.lintcode.com/problem/587/solution/17498
```python
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        
        count = 0
        left, right = 0, len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] == target:
                count, left, right = count + 1, left + 1, right - 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        
        return count
```

## version 2
url: https://www.lintcode.com/problem/587/solution/17418
```python
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        
        count = 0
        left, right = 0, len(nums) - 1
        last_pair = (None, None)
        
        while left < right:
            if nums[left] + nums[right] == target:
                if (nums[left], nums[right]) != last_pair:
                    count += 1
                last_pair = (nums[left], nums[right])
                left, right = left + 1, right - 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        
        return count
```
