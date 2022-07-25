class Solution1:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays

    数组，prefix_max[i] suffix_max[i]
    分别代表前缀数组在i时，最大的sum 和后缀数组在i时最大的sum
    要构造这样一个数据结构，需要构造一个数组满足，包含i时，为最大的数组和
    即为max(prefix_sum[i - 1] + nums[i], nums[i])， 当prefix_sum[i - 1] 为负数的时将他舍去
    构造玩prefix_max 和 suffix_max 即遍历他两相加的情况即可    

    https://www.lintcode.com/problem/42/solution/17670?fromId=164&_from=collection
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        n = len(nums)       
        prefix_max = [0] * n
        suffix_max = [0] * n
        prefix_sum = [0] * n
        suffix_sum = [0] * n
        prefix_max[0] = prefix_sum[0] = nums[0]
        suffix_max[-1] = suffix_sum[-1] = nums[-1]
        
        for i in range(1, n):
            prefix_sum[i] = max(prefix_sum[i - 1] + nums[i], nums[i])
            prefix_max[i] = max(prefix_max[i - 1], prefix_sum[i])
        
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = max(suffix_sum[i + 1] + nums[i], nums[i])
            suffix_max[i] = max(suffix_max[i + 1], suffix_sum[i])
        
        max_sum = -sys.maxsize
        for i in range(n - 1):
            print(prefix_max[i], suffix_max[i + 1])
            max_sum = max(max_sum, prefix_max[i] + suffix_max[i + 1])
        
        return max_sum     

class Solution2:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays

    left[i] 代表从最左边到 i 位置所能取得的最大 subarray sum;
    right[i] 代表从最右边到 i 位置所能取得的最大 subarray sum;
    两个数组都是 global 解

    https://www.lintcode.com/problem/42/solution/16867?fromId=164&_from=collection
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        if not nums:
            return 0
            
        n = len(nums)
        left = [0] * n
        right = [0] * n
        
        left[0] = nums[0]
        max_so_far = nums[0]
        max_ending_here = nums[0]
        for i in range(1, n):
            max_ending_here = max(nums[i], nums[i] + max_ending_here)
            max_so_far = max(max_so_far, max_ending_here)
            
            left[i] = max_so_far
            
        
        right[n - 1] = nums[n - 1]
        max_so_far = nums[n - 1]
        max_ending_here = nums[n - 1]
        for i in range(n - 2, -1, -1):
            max_ending_here = max(nums[i], nums[i] + max_ending_here)
            max_so_far = max(max_so_far, max_ending_here)
            
            right[i] = max_so_far   
        
        res = -sys.maxint - 1
        for i in range(n - 1):
            res = max(res, left[i] + right[i + 1])
        return res


   