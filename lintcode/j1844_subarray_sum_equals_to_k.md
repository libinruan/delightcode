冲刺班的解题思路，用前缀和把问题转化成Two Sum，然后再用哈希表解决。
```python
class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsKII(self, nums, k):
        prefix_sum = self.get_prefix_sum(nums)
        
        answer = float('inf')
        sum2index = {0: 0}
        for end in range(len(nums)):
            # find prefix_sum[end + 1] - prefix_sum[start] = k
            # => prefix_sum[start] = prefix_sum[end + 1] - k
            if prefix_sum[end + 1] - k in sum2index:
               length = end + 1 - sum2index[prefix_sum[end + 1] - k] 
               answer = min(answer, length)
            sum2index[prefix_sum[end + 1]] = end + 1
            
        return -1 if answer == float('inf') else answer
        
    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum
```