https://www.lintcode.com/problem/1507/

lp: hashmap 只適合找剛好等於某數值的數據。

返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。
如果没有和至少为 K 的非空子数组，返回 -1 。

> lp: review LintCode 1844. brute force, brute force with prefix_sum is applicable here as well.

# Official 1
使用`单调队列`的方法，时间复杂度 O(n) 是最优的

```python
from collections import deque
class Solution:
    """
    @param A: the array
    @param K: sum
    @return: the length
    """
    def shortestSubarray(self, A, K):
        mono_queue = deque([(0, -1)])
        shortest = float('inf')
        prefix_sum = 0
        for end in range(len(A)):
            prefix_sum += A[end]
            # pop left
            while mono_queue and prefix_sum - mono_queue[0][0] >= K:
                min_prefix_sum, index = mono_queue.popleft()
                shortest = min(shortest, end - index)
            # push right
            while mono_queue and mono_queue[-1][0] >= prefix_sum:
                mono_queue.pop()
            mono_queue.append((prefix_sum, end))
        
        if shortest == float('inf'):
            return -1
        return shortest
```

# Official 2
使用堆的方法。堆支持删除的时候用 lazy_deletion 的方法。

```python
from heapq import heappush, heappop
class Heap:
    
    def __init__(self):
        self.minheap = []
        self.deleted_set = set()
    
    def push(self, index, val):
        heappush(self.minheap, (val, index))
    
    def _lazy_deletion(self):
        while self.minheap and self.minheap[0][1] in self.deleted_set:
            heappop(self.minheap)
    
    def top(self):
        self._lazy_deletion()
        return self.minheap[0]
    
    def pop(self):
        self._lazy_deletion()
        heappop(self.minheap)
        
    def delete(self, index):
        self.deleted_set.add(index)
        
    def is_empty(self):
        return not bool(self.minheap)
        

class Solution:
    """
    @param A: the array
    @param K: sum
    @return: the length
    """
    def shortestSubarray(self, A, K):
        prefix_sum = self.get_prefix_sum(A)
        
        # do binary search to find the minimum length that
        # we could find a subarray within that length and sum >= K
        start, end = 1, len(A)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_valid(prefix_sum, K, mid):
                end = mid
            else:
                start = mid
        if self.is_valid(prefix_sum, K, start):
            return start
        if self.is_valid(prefix_sum, K, end):
            return end
        return -1
    
    def is_valid(self, prefix_sum, K, length):
        minheap = Heap()
        for end in range(len(prefix_sum)):
            index = end - length - 1
            minheap.delete(index)
            # find the maximum subarray
            if not minheap.is_empty() and prefix_sum[end] - minheap.top()[0] >= K:
                return True
            minheap.push(end, prefix_sum[end])
        return False
        
    def get_prefix_sum(self, A):
        prefix_sum = [0]
        for num in A:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum
```


# Official 3
使用线段树的做法

```python
class MySegmentTreeNode:
    
    def __init__(self, start, end, val):
        self.start, self.end = start, end
        self.val = val
        self.left_child, self.right_child = None, None
    
    
class MySegmentTree:
    
    def __init__(self, start, end):
        self.root = self.build_tree(start, end)
    
    def build_tree(self, start, end):
        node = MySegmentTreeNode(start, end, -float('inf'))
        if start == end:
            return node
            
        node.left_child = self.build_tree(start, (start + end) // 2)
        node.right_child = self.build_tree((start + end ) // 2 + 1, end)
        return node
    
    def insert(self, node, index, val):
        if node.start == index and node.end == index:
            node.val = val
            return
        if index <= node.left_child.end:
            self.insert(node.left_child, index, val)
        else:
            self.insert(node.right_child, index, val)
        node.val = max(node.left_child.val, node.right_child.val)
    
    def query(self, node, start, end):
        if end < start:
            return -float('inf')
        if node.start == start and node.end == end:
            return node.val
        if end <= node.left_child.end:
            return self.query(node.left_child, start, end)
        elif start >= node.right_child.start:
            return self.query(node.right_child, start, end)
        return max(
            self.query(node.left_child, start, node.left_child.end),
            self.query(node.right_child, node.right_child.start, end)
        )
        

class Solution:
    """
    @param A: the array
    @param K: sum
    @return: the length
    """
    def shortestSubarray(self, A, K):
        prefix_sum = self.get_prefix_sum(A)
        sum2index = self.get_sum2index(prefix_sum, K)
        
        st = MySegmentTree(0, len(sum2index) - 1)
        answer = float('inf')
        for end in range(len(A)):
            st.insert(st.root, sum2index[prefix_sum[end]], end)
            start = st.query(st.root, st.root.start, sum2index[prefix_sum[end + 1] - K])
            if start != -float('inf'):
                answer = min(answer, end - start + 1)
                
        return answer if answer != float('inf') else -1
        
    def get_prefix_sum(self, A):
        prefix_sum = [0]
        for num in A:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum
    
    def get_sum2index(self, prefix_sum, K):
        prefix_sum_set = set()
        for num in prefix_sum:
            prefix_sum_set.add(num)
            prefix_sum_set.add(num - K)
        
        sum2index = {}
        for index, num in enumerate(sorted(list(prefix_sum_set))):
            sum2index[num] = index
        
        return sum2index
```


# answer 1: sliding window

lp: O(log(n) * n) ~ O(n log(n))

我们用数组 P 表示数组 A 的前缀和，即 P[i] = A[0] + A[1] + ... + A[i - 1]。我们需要找到 x 和 y，使得 P[y] - P[x] >= K 且 y - x 最小。

我们用 opt(y) 表示对于固定的 y，最大的满足 P[x] <= P[y] - K 的 x，这样所有 y - opt(y) 中的最小值即为答案。我们可以发现两条性质：

如果 x1 < x2 且 P[x2] <= P[x1]，那么 opt(y) 的值不可能为 x1，这是因为 x2 比 x1 大，并且如果 x1 满足了 P[x1] <= P[y] - K，那么 P[x2] <= P[x1] <= P[y] - K，即 x2 同样满足 P[x2] <= P[y] - K。

如果 opt(y1) 的值为 x，那么我们以后就不用再考虑 x 了。这是因为如果有 y2 > y1 且 opt(y2) 的值也为 x，但此时 y2 - x 显然大于 y1 - x，不会作为所有 y - opt(y) 中的最小值。

算法

我们维护一个关于前缀和数组 P 的单调队列，它是一个双端队列（deque），其中存放了下标 x：x0, x1, ... 满足 P[x0], P[x1], ... 单调递增。这是为了满足性质一。

当我们遇到了一个新的下标 y 时，我们会在队尾移除若干元素，直到 P[x0], P[x1], ..., P[y] 单调递增。这同样是为了满足性质一。

同时，我们会在队首也移除若干元素，如果 P[y] >= P[x0] + K，则将队首元素移除，直到该不等式不满足。这是为了满足性质二。

```python
class Solution(object):
    def shortestSubarray(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        #Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = collections.deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1
```

# answer 2: double end queue
一个双端队列d，变量i从0开始到n（包含）遍历，队列中存放的是[0,i]之间可能的开始位置，i为结束位置。
如果d[0]满足条件（就是d[0]开始，i结束的字数组和至少为K），就删除它，然后再循环判断，直到d[0]不满足条件。
d中位置对应的值是从小到大的，0不满足，后面更不可能满足，所以不用再判断。
如果i比队尾元素小或相等，就删除队尾，循环判断，直到i比队尾元素大。

```python
class Solution:
    """
    @param A: the array
    @param K: sum
    @return: the length
    """
    def shortestSubarray(self, A, K):
        # Write your code here.
        N = len(A)
        B = [0] * (N + 1)
        for i in range(N): B[i + 1] = B[i] + A[i]
        d = collections.deque()
        res = N + 1
        for i in range(N + 1):
            while d and B[i] - B[d[0]] >= K: 
                res = min(res, i - d.popleft())
            while d and B[i] <= B[d[-1]]: 
                d.pop()
            d.append(i)
        return res if res <= N else -1
```


# answer 3: monotonic queue + prefix sum + sliding window
单调队列 + prefix sum + sliding window
维持一个单调递增的队列，我们需要找到的条件为，j > i 且sum[j] - sum[i] >= k, j - i 最短
for 循环遍历整个数组把它看成sliding window
出头队列逻辑： 如果当前的presum - 队列头的sum 大于等于k的话，因为头队列为最小起始点，所以后面的presum不可能找到更小的window了 所以可以直接把头部poll出来
出尾队列逻辑： 如果尾部比我当前prefix sum还大，维持单调递增，就直接poll出来
然后入队尾

注意点： prefix sum array 的长度要比数组长度大一位，因为有可能是正好所有数字加起来等于k，prefix 需要多一位才可以减，也正因为多了一位，再算长度的时候 j - i 不需要加1；
for 循环的长度也是prefix sum 的长度 而不是输入数组的长度
   （这个题也太tm难了，没刷过估计想不到deque的做法）      

```java
public class Solution {
    /**
     * @param A: the array
     * @param K: sum
     * @return: the length
     */
    public int shortestSubarray(int[] A, int K) {
        // Write your code here.
        if (A == null || A.length == 0) {
            return -1;
        }

        Deque<Integer> queue = new ArrayDeque<>();
        int[] prefixSum = new int[A.length + 1];
        for (int i = 0; i < A.length; i++) {
            prefixSum[i + 1] = prefixSum[i] + A[i];
        }
        int result = Integer.MAX_VALUE;
        for (int i = 0; i < prefixSum.length; i++) {
            while(!queue.isEmpty() && (prefixSum[i] - prefixSum[queue.peekFirst()]) >= K) {
                result = Math.min(result, i - queue.pollFirst());
            }
            while (!queue.isEmpty() && prefixSum[queue.peekLast()] >= prefixSum[i]) {
                queue.pollLast();
            }
            queue.offer(i);
        }

        return result == Integer.MAX_VALUE ? -1 : result;
    }
}
```
