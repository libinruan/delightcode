# Solution 1 by purple rosewood
https://www.lintcode.com/problem/1778/solution/57395
```python
from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array A
    @return: Return the number of good starting indexes
    """
    def odd_even_jumps(self, a: List[int]) -> int:
        N = len(a)

        def make(b):
            ans = [None] * N
            stack = []  # invariant: stack is decreasing
            for i in b:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        b = sorted(range(N), key = lambda i: a[i])
        oddnext = make(b)
        b.sort(key = lambda i: -a[i])
        evennext = make(b)

        odd = [False] * N
        even = [False] * N
        odd[N-1] = even[N-1] = True

        for i in range(N-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        return sum(odd)
```

# Solution 2 by dreamy butterfly
https://www.lintcode.com/problem/1778/solution/22671

单调栈+BFS版

先用单调栈把图构出来。 需要做两遍， 一遍数要越来越大， 一遍数要越来越小。 然后我
们知道， 单调栈是找左右两遍第一个比自己大or小的数。 所以我们不能直接对数字进行单
调栈， 而是要把index, num丢到一起， 按照num排序以后， 对index做单调栈。 这里有个
要主要的点， 就是你排序的时候， num是正着还是倒着排， 决定了你是奇数跳还是偶数
跳。 然后单调栈， 永远用递减栈来找自己右边的数。

BFS， 然后我们从最后一个数开始。 最后一步可以是奇也可以是偶， 找到所有奇出发的
点， 就是答案。 这里要注意一点儿了， 为了保证我们不会在每次都去纠结上一步是奇数
还是偶数， 我们这里用了一个分裂node的办法， 直接把每个数建成2个node， 一个奇的一
个偶的， 构图时候就这么做， 所以bfs就变得巨简单

```python
class Solution:
    """
    @param A: An integer array A
    @return: Return the number of good starting indexes
    """
    def oddEvenJumps(self, A):
        if not A:
            return 0
        graph = self.build_graph(A)
        queue = collections.deque([(0, len(A) - 1, A[-1]), (1, len(A) - 1, A[-1])])
        results = []
        while queue:
            curr = queue.popleft()
            if curr[0] == 1:
                results.append((curr[1], curr[2]))
            for neighbor in graph[curr]:
                queue.append(neighbor)
        return len(results)
    
    def build_graph(self, A):
        index_num_pair = [(index, num) for index, num in enumerate(A)]
        graph = collections.defaultdict(list)

        index_num_pair.sort(key = lambda pair:pair[1])
        stack = []
        for i in range(len(index_num_pair)):
            while stack and stack[-1][0] <= index_num_pair[i][0]:
                poped = stack.pop()
                graph[(0, index_num_pair[i][0], index_num_pair[i][1])].append((1, poped[0], poped[1]))
            stack.append(index_num_pair[i])

        index_num_pair.sort(key = lambda pair:pair[1], reverse = True)
        stack = []
        for i in range(len(index_num_pair)):
            while stack and stack[-1][0] <= index_num_pair[i][0]:
                poped = stack.pop()
                graph[(1, index_num_pair[i][0], index_num_pair[i][1])].append((0, poped[0], poped[1]))
            stack.append(index_num_pair[i])
        return graph
```

# monotonic stack, DP by dashing fox
https://www.lintcode.com/problem/1778/solution/17744
```python
class Solution:
    """
    @param A: An integer array A
    @return: Return the number of good starting indexes
    """
    def oddEvenJumps(self, A):
        # change A into value index pair.
        pairs = sorted([(value, index) for index, value in enumerate(A)])
        odd_jump = self.get_jump(list(reversed(pairs)))
        
        # for the same value, sort index in desc order.
        pairs = sorted(pairs, key=lambda x: (x[0], -x[1]))
        even_jump = self.get_jump(pairs)

        # dp = array of n x 2
        # dp[i][0] can we jump to n - 1 when we arrive i by even jumps
        # dp[i][1] can we jump to n - 1 when we arrive i by odd jumps
        n = len(A)
        dp = [[False, False] for _ in range(n)]
        dp[n - 1][0] = dp[n - 1][1] = True
        
        answer = 1
        for i in range(n - 2, -1, -1):
            dp[i][0] = dp[odd_jump[i]][1] if odd_jump[i] is not None else False
            dp[i][1] = dp[even_jump[i]][0] if even_jump[i] is not None else False
            if dp[i][0] == True:
                answer += 1
        return answer
        
    def get_jump(self, pairs):
        jump, stack = [None] * len(pairs), []
        for value, index in pairs:
            self.mono_desc_push(stack, index)
            jump[index] = stack[-2] if len(stack) > 1 else None
        return jump
        
    def mono_desc_push(self, stack, val):
        while stack and stack[-1] <= val:
            stack.pop()
        stack.append(val)
```