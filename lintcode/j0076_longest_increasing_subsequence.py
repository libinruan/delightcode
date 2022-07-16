from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)

    DP: https://www.lintcode.com/problem/76/solution/56400?fromId=164&_from=collection
    Binary Search: https://www.lintcode.com/problem/76/solution/56408?fromId=164&_from=collection
    """
    def longest_increasing_subsequence(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: # 我較大，同伴答案加一。
                    dp[i] = max(dp[i], dp[j] + 1)

        res = max(dp) # 不能用 dp[-1]，因为有可能有负的元素。
        return res

class Solution:
    def longest_increasing_subsequence(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)