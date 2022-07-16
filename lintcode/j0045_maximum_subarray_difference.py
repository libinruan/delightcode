import sys
class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings

    sol - Yulia - https://www.lintcode.com/problem/45/solution/17491?fromId=164&_from=collection
    challenge: O(n) time and O(n) space.
    """
    def maxDiffSubArrays(self, nums):
        # 分别找顺序、逆序的max&min
        left_max = self._maximum_subarray(nums)
        right_max = self._maximum_subarray(nums[::-1])[::-1]
        
        left_min = self._maximum_subarray(self._negate_array(nums))
        left_min = self._negate_array(left_min)
        right_min = self._maximum_subarray(self._negate_array(nums)[::-1])[::-1]
        right_min = self._negate_array(right_min)
        
        # 枚举分割线的位置
        max_diff = - sys.maxsize - 1
        for i in range(len(nums) - 1):
            max_diff = max(max_diff, 
                           abs(left_max[i] - right_min[i + 1]),
                           abs(left_min[i] - right_max[i + 1]))
        return max_diff
    
    def _negate_array(self, nums):
        return list(map(lambda x: -x, nums))
    
    def _maximum_subarray(self, nums):
        max_sum = - sys.maxsize - 1
        max_sums = []
        prev_min_sum = 0
        curr_sum = 0
        
        for i, num in enumerate(nums):
            curr_sum += num
            max_sum = max(max_sum, curr_sum - prev_min_sum)
            max_sums.append(max_sum)
            prev_min_sum = min(prev_min_sum, curr_sum)
        
        return max_sums