# answe 1
# https://www.lintcode.com/problem/633/solution/16920
class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        start, end = 1, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if self.smaller_than_or_equal_to(nums, mid) > mid:
                end = mid
            else:
                start = mid
                
        if self.smaller_than_or_equal_to(nums, start) > start:
            return start
            
        return end
        
    def smaller_than_or_equal_to(self, nums, val):
        count = 0
        for num in nums:
            if num <= val:
                count += 1
        return count



# answer 2       
# https://www.lintcode.com/problem/633/solution/20162
# [这里有解释映射](http://bookshadow.com/weblog/2015/09/28/leetcode-find-duplicate-number/)
class Solution:
    # @param {int[]} nums an array containing n + 1 integers which is between 1 and n
    # @return {int} the duplicate one
    def findDuplicate(self, nums):
        # Write your code here
        if len(nums) <= 1:
            return -1

        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0;
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return slow