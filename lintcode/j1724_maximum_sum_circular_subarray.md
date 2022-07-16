Prefix sum + Monotone queue:
solution: https://www.lintcode.com/problem/1724/solution/59625?fromId=164&_from=collection
```python
from typing import (
    List,
)

class Solution:
    def max_subarray_sum_circular(self, a: List[int]) -> int:
        N = len(a)

        # Compute P[j] = sum(B[:j]) for the fixed array B = a+a
        P = [0]
        for _ in range(2):
            for x in a:
                P.append(P[-1] + x)

        # Want largest P[j] - P[i] with 1 <= j-i <= N
        # For each j, want smallest P[i] with i >= j-N
        ans = a[0]
        deque = collections.deque([0]) # i's, increasing by P[i]
        for j in range(1, len(P)):
            # If the smallest i is too small, remove it.
            if deque[0] < j-N:
                deque.popleft()

            # The optimal i is deque[0], for cand. answer P[j] - P[i].
            ans = max(ans, P[j] - P[deque[0]])

            # Remove any i1's with P[i2] <= P[i1].
            while deque and P[j] <= P[deque[-1]]:
                deque.pop()

            deque.append(j)

        return ans
```

前缀和+单调栈版本
403的降级版。 和403一样， 只不过这个题目， 求直接求sum。 那么就不需要记录index了。
```python
class Solution:
    """
    @param A: the array
    @return: Maximum Sum Circular Subarray
    """
    def maxSubarraySumCircular(self, A):
        if not A:
            return []
        prefix_sum = [0] * len(A) * 2
        prefix_sum[0] = A[0]
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + A[i % len(A)]

        stack = collections.deque([0])
        max_range_sum = -float('inf')
        for i in range(1, len(prefix_sum)):
            if prefix_sum[i] - prefix_sum[stack[0]] > max_range_sum:
                max_range_sum = prefix_sum[i] - prefix_sum[stack[0]]
            while stack and prefix_sum[stack[-1]] >= prefix_sum[i]:
                stack.pop()
            stack.append(i)

            if stack[0] <= i - len(A):
                stack.popleft()
        return max_range_sum
```

模板题， 扫一遍做max subarray， 扫一遍做min subarray
然后你要转化思想就是， 如果最大值要依靠那个环形， 说明最小值不依靠环形。

```python
class Solution:
    """
    @param A: the array
    @return: Maximum Sum Circular Subarray
    """
    def maxSubarraySumCircular(self, A):

        #### case 1: max appear in the middle
        max_here, max_so_far = -float('inf'), -float('inf')
        for a in A:
            max_here = max(max_here + a,  a)
            max_so_far = max(max_so_far, max_here)

        
        #### case 2: max appear at two ends, so in the middle is min 
        min_here, min_so_far = float('inf'), float('inf')
        Ap = A[1:-1]   ### min cannot appear at two ends
        for a in Ap:
            min_here = min(min_here + a,  a)
            min_so_far = min(min_so_far, min_here)

        return max(max_so_far, sum(A) - min_so_far)
```