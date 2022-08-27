Description
Given an array of integers and an integer k, you need to find the minimum size of continuous no-empty subarrays whose sum equals to k, and return its length.

if there are no such subarray, return -1.

# O(n)

Hint: 用前缀和把问题转化成Two Sum，然后再用哈希表(sum2index)解决。
LP: note that one feature of this solution: for the same key in sum2index, a subsequent update with value I' is larger than its predecessor I for sure, that is, I' > I.  

LP: if the question is to ask the "longest" subarray, then we need to add one condition before the update of dict sum2index.

```python
            if prefix_Sum[end + 1] not in sum2index:
                sum2index[prefix_sum[end + 1]] = end + 1
```

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
        sum2index = {0: 0}  # lp: zero-based index
        for end in range(len(nums)):
            # find prefix_sum[end + 1] - prefix_sum[start] = k
            # => prefix_sum[start] = prefix_sum[end + 1] - k
            # lp: end + 1的加一是因為initialize with 0 (index 0)。
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

# brute force O(n^3)
```python
for left in ...:  # O(n)
    for right in ...:  # O(n)
        for i in range(left, right + 1):  # O(n)
            check if k is reached
```

# brute force with prefix O(n^2)
```python
create prefixSum array  # O(n)
for left in ...:  # O(n)
    for right in ...:  # O(n)
        # for i in range(left, right + 1):  # O(n)
        check if k is reached
```

