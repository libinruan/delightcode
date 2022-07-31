# two pointers
url: 
```python
class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum5(self, nums, target):
        # Write your code here
        l, r = 0, len(nums)-1
        cnt = 0
        nums.sort()
        while l < r:
            value = nums[l] + nums[r]
            if value > target:
                r -= 1
            else:
                cnt += r - l
                l += 1
        return cnt
```

# Bisect, two pointers
url: https://www.lintcode.com/problem/609/solution/20008

## Bisect
```python
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        # 排序
        nums.sort()
        # 数组长度
        n = len(nums)
        # 答案
        ans = 0
        # 对于每个i，二分找到最大的j nums[i]+nums[j]<=target
        for i in range(n):
            # 确定二分上下界
            left = i
            right = n
            pos = i
            while left + 1 < right:
                mid = (int)(left + (right - left) // 2)
                # 不大于target 可以提高下界
                if nums[i] + nums[mid] <= target:
                    left = mid
                    pos = mid
                # 缩小上界
                else:
                    right = mid
            ans += pos - i
        return ans
```

## two pointers
```python
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """

    def twoSum5(self, nums, target):
        # write your code here
        # 排序
        nums.sort()

        # 数组长度
        n = len(nums)

        # 答案
        ans = 0

        # 双指针上下界
        start = 0
        end = n - 1

        while start <= n - 1:

            # 找到最小的end nums[start]+nums[end]<=target
            while end >= 0:
                if nums[start] + nums[end] > target:
                    end -= 1
                else:
                    break
            
            # 只记录start<end的情况
            if end > start:
                ans += end - start
            else:
                break

            start += 1
        return ans
```


# Bisect, two pointers (much conciser version)
```python
import bisect
class SolutionBisect:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):

        nums.sort()
        
        totalPairs = 0
        
        for i, num in enumerate(nums):
            otherNum = target - num 
            j = bisect.bisect(nums, otherNum, i)
            if j == i:
                break
            totalPairs += j - 1 - i 
            
        return totalPairs
        
class SolutionTwoPointers:
    
    def twoSum5(self, nums, target):
        
        nums.sort()
        
        totalPairs = 0
        
        left, right = 0, len(nums) - 1 
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1 
            else:
                totalPairs += right - left
                left += 1 
                
        return totalPairs
```