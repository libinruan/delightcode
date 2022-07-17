<!-- ------------------------------ JeremyXu ------------------------------- -->
非常值得总结的二分答案的题目
思路就是，对于 完成时间 进行二分查找，
找到第一个 不多于K个人能在给定的完成时间里完成 复印len(pages)本书 这一任务的 完成时间

完成时间的lower bound: max(pages), 理解为一共有len(pages)个人，每个人只复印一本书
完成时间的upper bound: sum(pages), 理解为只有一个人要独自复印所有的书
```python
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here        
        if not pages:            
            return 0             
        start = max(pages)
        end = sum(pages)        
        while start + 1 < end:            
            mid = start + (end - start) // 2             
            if self.can_complete(pages, k, mid):                
                end = mid                 
            else:                
                start = mid                 
        if self.can_complete(pages, k, start):            
            return start             
        # Since even if there is only one person,
        # he or she can copy all books, just return end.
        return end 
        
    def can_complete(self, pages, k, tl):        
        num = 1         
        pageSum = 0        
        for page in pages:            
            if pageSum + page <= tl:                
                pageSum += page                 
            else:                
                num += 1 
                pageSum = page                 
        return num <= k
```

<!-- ------------------------------ kailai27 ------------------------------- -->
用了和之前的 Maximum Average Subarray相同的思想
不过比Maximum Average Subarray简单些
首先又是range问题，或者可以说是subarray问题，array内的数值无法sort，而且因为需要求验的值很多，所以没法用dp
所以这题的解决方法自然而然落到 binary search
核心1：确定 start 和 end的数值
start很好确定，但是end，不但和array中最大的元素有关，还和 max_num * len(nums) // k有关
即当k很小时元素很多时，end也会变得很大，确定end条件是解题关键之一
核心2：缩小end 和start 范围的条件
即当前minutes * k 能copy完所有的书
用当前minutes for循环nums，只要 num < minute 就minute -= num 直到minute被减完，再换新的。
结束之后返回 count <= k（第二关键） 即代表当前的minutes是能copy完所有书的
```python
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if pages is None or len(pages) == 0:
            return 0
        # write your code here
        start = 0
        end = max(pages) * len(pages) // k + 1
        end = max(end, max(pages))
        while start + 1 < end:
            print(start, end)
            mid = (start + end) // 2
            if self.greater(mid, pages, k):
                end = mid
            else:
                start = mid
                
        print(start, end)
        if self.greater(start, pages, k):
            return start
        return end
    
    def greater(self, minutes, nums, k):
        temp = minutes
        count = 0
        for num in nums:
            if num > minutes:
                return False
            if temp - num >= 0:
                temp = temp - num
            elif temp - num < 0:
                count += 1
                temp = minutes - num
        return count + 1 <= k
```