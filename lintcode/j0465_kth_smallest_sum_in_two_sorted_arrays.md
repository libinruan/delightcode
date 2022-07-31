# TinLittle
一并上传这题的两种正解。

1。二分法，达到了题目要求的O((m + n) log maxSumDifference)时间。注意这里是最大和和最小和之差，而不是题里的最大数字值。这个lo < hi
的二分结束条件优于大家喜欢的left + 1 < right的模版，简单而且无需最后再判定一次。额外空间O(1)

2。堆和k路归并。这个也是真正达到了题目的O(k log min(m,n,k))时间要求。还没看到比我写的更简练的。注意，那些要用数组，set, 或dict
标记一个和是不是进过堆的解都不是正解。额外空间O(min(m,n,k))

```python
class Solution_binary_search:
    
    def kthSmallestSum(self, A, B, kth):
        
        m, n = len(A), len(B)
        lo, hi = A[0]+B[0], A[-1]+B[-1]+1 
        
        while lo < hi:
            mid = (lo+hi) // 2
            i, j, count = 0, n-1, 0
            while i < m and j >= 0:
                if A[i] + B[j] > mid:
                    j -= 1
                else:
                    count += j + 1
                    i += 1
            if count < kth:
                lo = mid + 1 
            else:
                hi = mid
                
        return lo
            
        
class Solution_heap:
         
    def kthSmallestSum(self, A, B, kth):
        
        m, n = len(A), len(B)
        if m < n:
            m, n, A, B = n, m, B, A 
        
        h = [(A[0]+B[j], 0, j) for j in range(min(n, kth))]
        
        for _ in range(kth):
            num, i, j = heappop(h)
            
            if i + 1 < m:
                heappush(h, (A[i+1]+B[j], i+1, j))
                
        return num
```

# Priortiy queue
O(k log min(n, m, k)). where n is the size of A, and m is the size of B.
严格时间复杂度为 O(min(n,m,k) + k log min(n,m,k)) 为建堆时间加上poppush时间

如果A或B的长度是 n m k 中的最小值，则选取较小的array作为master array。
如果k 是n m k 中最小，则无所谓谁是master array， 这里选取B作为master array

```python
import heapq
class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        # write your code here
        if not A or not B:
            return None 

        minheap = []
        heapsize = min(len(A), len(B), k)
        
        if heapsize == len(A):
            minheap = [ (A[i]+B[0], 'A', i, 0) for i in range(heapsize) ]
        else:
            minheap = [ (B[i]+A[0], 'B', i, 0) for i in range(heapsize) ]
        
        heapq.heapify(minheap)
        for _ in range(k):
            s, master_array, master_index, slave_index = heapq.heappop(minheap)
            master = A if master_array == 'A' else B
            slave = B if master is A else A
            if slave_index + 1 < len(slave):
                next_sum = master[master_index] + slave[slave_index+1]
                heapq.heappush(minheap, (next_sum, master_array, master_index, slave_index+1))
        
        return s
```        

```python
class Solution:
    
    """
    @param: A: an integer arrays sorted in ascending order
    @param: B: an integer arrays sorted in ascending order
    @param: k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        # write your code here
        
        m = min(len(A),k)
        n = min(len(B),k)
        
        visited = [[False]*n for _ in xrange(m)]
        
        from heapq import *
        
        heap = [(A[0]+B[0],(0,0))]
        
        for i in xrange(k):
            res , (x,y) = heappop(heap)
            if x+1 < m and visited[x+1][y] == False:
                heappush(heap,(A[x+1]+B[y],(x+1,y)))
                visited[x+1][y] = True
            if y+1<n and visited[x][y+1] == False:
                heappush(heap,(A[x]+B[y+1],(x,y+1)))
                visited[x][y+1] = True
        
        return res
```

# Priority queue
A, B两个sorted Array中任意两个元素的和其实
可以组成一个sorted matrix, 即任意行或列都是sorted,
直接转化成Kth Smallest Number in Sorted Matrix 进行求解
```python
class Solution:
    
    """
    @param: A: an integer arrays sorted in ascending order
    @param: B: an integer arrays sorted in ascending order
    @param: k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        # write your code here
        
        m = min(len(A),k)
        n = min(len(B),k)
        
        visited = [[False]*n for _ in xrange(m)]
        
        from heapq import *
        
        heap = [(A[0]+B[0],(0,0))]
        
        for i in xrange(k):
            res , (x,y) = heappop(heap)
            if x+1 < m and visited[x+1][y] == False:
                heappush(heap,(A[x+1]+B[y],(x+1,y)))
                visited[x+1][y] = True
            if y+1<n and visited[x][y+1] == False:
                heappush(heap,(A[x]+B[y+1],(x,y+1)))
                visited[x][y+1] = True
        
        return res
```

# Priority queue, bisect
![](https://i.postimg.cc/KzCHkJDL/Jiuzhang-vip-30days.png)
![](https://i.postimg.cc/HLhSRBKK/Jiuzhang-vip-30days.png)
![](https://i.postimg.cc/dVQ40bcp/Jiuzhang-vip-30days.png)

```python
from heapq import *

class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        # write your code here
        # 初始化 优先队列 ，我们优先队列的一个元素包括三个值 ：数字和大小，数字在数组A位置，数字在数组B位置
        heap = []
        for i in range(len(B)):
            heappush(heap, [A[0] + B[i], 0, i])
        while k > 1:
            k -= 1
            # 取出堆中最小值
            point = heappop(heap)
            value = point[0]
            aIdx = point[1]
            bIdx = point[2]
            # 已经是所在数组的最后一个元素了
            if (aIdx == len(A) - 1):
                continue
            else:
                # 压入该数组的下一个元素
                newvalue = A[aIdx + 1] + B[bIdx]
                heappush(heap, [newvalue, aIdx + 1, bIdx])
        return heappop(heap)[0]
```

```python
from heapq import *

class Solution:
    def calc(self, x, A, B):
        # AB长度
        n = len(A)
        m = len(B)
        # 小于等于x的数量
        num = 0
        # 双指针上下边界
        start = 0
        end = m - 1
        while start <= n - 1:
            while end >= 0:
                if A[start] + B[end] > x:
                    end -= 1
                else:
                    break
            # 因为A[start]+B[end]<=x 所以A[start]+B[0]....A[start]+B[end-1]都小于等于x
            num += end + 1
            start += 1
        return num
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        # write your code here
        # AB长度
        n = len(A)
        m = len(B)
        # 二分上下界
        left = A[0] + B[0] - 1
        right = A[n - 1] + B[m - 1] + 1
        while left + 1 < right:
            # 如果小于等于x的超过k个就缩小上界，否则提高下界
            mid = (int)(left + (right - left) // 2)
            if (self.calc(mid, A, B) >= k):
                right = mid
            else:
                left = mid
        return right
```