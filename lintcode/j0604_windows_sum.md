This is not free question. An advanced one is c0239_sliding_window_maximum.py

[Question](https://leetcode.com/problems/sliding-window-maximum/)


# 1 Pop or push each element at-max once. O(N)
Similar Questions:

https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
https://leetcode.com/problems/next-greater-element-i/
https://leetcode.com/problems/largest-rectangle-in-histogram/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


Monotone stack (queue contains all the candidates arranged in monotonically decreasing order)

    (1) Add to dequeue at tail using the rule where you pop all numbers from tail which are less than equal to the number. Think why? 300->50->27 and say 100 comes. 50 and/or 27 can never be the maximum in any range.

    (2) When you do the above, the largest number is at head. But you still need to test if front is within the range or not. Pop or push each element at-max once. O(N)

    So, to maintain the queue in order,

    (1-A) When moves to a new number, iterate through back of the queue, removes all numbers that are not greater than the new one, and then insert the new one to the back.

    (1-B) To remove a number outside the window, only compare whether the current index is greater than the front of queue. If so, remove it.

    WHY WE USE MONOTONE STACK HERE (IMPLEMENTED BY DEQUE)? 
    Ans: To find the max in this (monotonically decreasing) monotone stack, we only need to take the first one of the queue.

```python
class Solution(object):
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        queue = deque([]) # to cache (index, number) pairs
        res = []
        for i, num in enumerate(nums):
# 1-A FIRST, REMOVE THE OLDEST CANDIDATE THAT IS OUT OF THE CURRENT WINDOW            
            if queue and queue[0][0] < i - k + 1: # smaller the start index of the window
                queue.popleft()
# 1-B SECOND, REMOVE CANDIDATES IN THE CURRENT WINDOW SMALLER THAN TO-BE-ADDED CANDIDATE SHOULD BE REMOVED  
            while queue and queue[-1][1] < num:
                queue.pop()
# 1-C THIRD, PUSH THE NEW CANDIDATE INTO THE STACK
            queue.append([i, num])
# 1-D UPDATE THE RES ARRAY
            if i >= k - 1:
                res.append(queue[0][1])            
        return res
```

# 2 Brute force: O(n * k)

```python
class Solution(object):
    def get_max(self, nums: List[int], start: int, end: int) -> int:
        answer = -2**31
        for i in range(start, end+1):
            answer = max(answer, nums[i])
        return answer
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start,end = 0,k-1
        result = []
        while end < len(nums) and len(nums):
            result.append(self.get_max(nums, start, end))
            start, end = start+1, end+1
        return result
```

# 3 Max Heap Solution: O(n * log(n))

    (1) Add k elements and their indices to heap. Python has min-heap. So for max-heap, multiply by -1.

    (2) Set start = 0 and end = k-1 as the current range.

    (3) Extract the max from heap which is in range i.e. >= start. Add the max to the result list. 
        Now add the max back to the heap - it could be relevant to other ranges.

    Move the range by 1. Add the new last number to heap.

    This is an O(NlgN) solution.
    
    Note that we need not invest into thinking about deleting the obsolete entry every time the window slides.That would be very hard to implement. Instead we maintain the index in heap and "delete" when the maximum number is out of bounds.

```python
import heapq as h
class Solution(object):
    def get_next_max(self, heap, start):
        while True:
            x, idx = h.heappop(heap)
            if idx >= start:
                return x * -1, idx
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        heap = []
        for i in range(k):
            h.heappush(heap, (nums[i] * -1, i))
        result, start, end = [], 0, k-1
        while end < len(nums):
# GET AND UPDATE THE MAXIMUM OF THE JUST-SLID WINDOW WITH NEW CANDIDATE ADDED IN LAST ITERATION            
            x, idx = self.get_next_max(heap, start)
            result.append(x) 
            h.heappush(heap, (x * -1, idx)) # add it back 
# ADD NEW ELEMENT INTO THE MAX HEAP            
            start, end = start + 1, end + 1
            if end < len(nums):
                h.heappush(heap, (nums[end] * -1, end))
        return result
```        

