Description

Given an array of integers, find a contiguous subarray which has the largest sum. Can you do it in time complexity O(n)?

https://www.lintcode.com/problem/41/description

# official
```python
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        #prefix_sum记录前i个数的和，max_Sum记录全局最大值，min_Sum记录前i个数中0-k的最小值
        min_sum, max_sum = 0, -sys.maxsize
        prefix_sum = 0
        
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
            
        return max_sum
```

# DP, Greedy, prefix sum

这题众所周知可以用prefix sum来解决但是有一个关键点：不能单纯求出prefixSum的最大值和最小值 然后相减因为最小值有可能出现在最大值之后 那么这样就构不成一个subarray。

所以 当沿着array index一个个往下走的时候 我们只需要知道“到目前为止“前面的prefix sum的最小值即可 而不是全局的最小值

```python
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray1(self, nums):
        #dp sulution
        if len(nums) == 0: return 0
        dp = [0 for x in range(len(nums))]  # 
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i-1]) + nums[i]
        max_value = -sys.maxsize - 1
        for v in dp:
            max_value = max(max_value, v)
        return max_value

    def maxSubArray2(self, nums):
        #prefix sum Solution
        if len(nums) == 0: return 0
        prefix_sum = 0
        min_sum = 0
        max_slice = -sys.maxsize - 1
        for n in nums:
            prefix_sum += n 
            max_slice = max(max_slice, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
        return max_slice 

    def maxSubArray3(self, nums):
        #greedy
        if len(nums) == 0: return 0 
        sum = 0 
        slice = -sys.maxsize - 1 
        for n in nums:
            sum += n 
            slice = max(slice, sum)
            sum = max(0, sum)
        return slice                
```

# DP
本题可以用动态规划来解。

> dp[i] = the maximum subarray whose end element is nums[i]
>
> ~Lipin

```python
# Version 1: DP
class Solution:
    """
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        
        if nums is None or len(nums) == 0:
            return 0
            
        dp = [0]*len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
                continue
            
            dp[i] = nums[i] + max(0, dp[i-1])
            
        return max(dp)

# Version 2: DP (Sapce Optimized)                    
class Solution:
    """
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        
        if nums is None or len(nums) == 0:
            return 0
        
        max_sum = local_max_sum = nums[0]
        
        for i in range(1, len(nums)):
            local_max_sum = nums[i] + max(0, local_max_sum)
            max_sum = max(max_sum, local_max_sum)
            
        return max_sum
```