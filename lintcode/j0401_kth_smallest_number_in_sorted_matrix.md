<!-- ------------------------------ TinLittle ------------------------------ -->
传说中的时间O(klog(min(m,n,k)))，空间O(min(m,n,k))的最优解。

矩阵高度m，宽度n，m 和 n 那个短就用那个建堆。k如果更短的话，堆长就是k。

建了堆后，就只需向下或向右走，弹一个进一个，而不是弹一个进两个，所以堆的大小不会再长。

一题多解更能帮助总结规律，掌握技能。和常见的归并法一起换着刷两次，能帮你加深堆应用的理解。

```python
from heapq import heapify, heappush, heappop

class Solution:
    
    def kthSmallest(self, matrix, kth):
        
        m, n = len(matrix), len(matrix[0])
        
        if m < n:
            return self.kthSmallest_horizontal(matrix, kth)
            
        return self.kthSmallest_vertical(matrix, kth)
        
    def kthSmallest_vertical(self, matrix, kth):
        
        m, n = len(matrix), len(matrix[0])
        
        min_heap = [(matrix[0][j], 0, j) for j in range(min(n, kth))]
        heapify(min_heap)
        
        for _ in range(kth):
            
            top, i, j = heappop(min_heap)
            
            if i + 1 < m:
                heappush(min_heap, (matrix[i+1][j], i+1, j))
                
        return top
    
    def kthSmallest_horizontal(self, matrix, kth):
        
        m, n = len(matrix), len(matrix[0])
        
        min_heap = [(matrix[i][0], i, 0) for i in range(min(m, kth))]
        heapify(min_heap)
        
        for _ in range(kth):
            
            left, i, j = heappop(min_heap)
            
            if j + 1 < n:
                heappush(min_heap, (matrix[i][j+1], i, j+1))
                
        return left
```

<!-- ------------------------------ somebody ------------------------------- -->

solution: https://www.lintcode.com/problem/401/solution/19308?fromId=164&_from=collection

算法
算法一 暴力
题目指出n个数组是有序的，那我们可以借鉴归并排序的思想

每次遍历n个有序数组的数组第一个元素，找出最小的那个，记得把最小的那个从它原先的数组给删除

一直执行k次就找到第k小值了

每次找最小的是O(N)的，所以总复杂度是O(NK)的

算法二 优先队列优化
根据算法一，来进行优化，我们可以通过一些有序集合来找最小值，比如set map 堆 平衡树一类都可以，我们这里用堆来加速求最小值的操作

优先队列
- 先将每个有序数组的第一个元素压入优先队列中
- 不停的从优先队列中取出最小元素（也就是堆顶），再将这个最小元素所在的有序数组的下一个元素压入队列中 eg. 最小元素为x，它是第j个数组的第p个元素，那么我们把第j个数组的第p+1个元素压入队列
- 取出操作做k次就得到了第k小值


算法三
如果序列有序，则可以用一种更有效率的查找方法来查找序列中的记录，这就是折半查找法，又称为二分搜索。

折半查找的基本思想：减少一半的查找序列的长度，分而治之地进行关键字的查找。他的查找过程是：先确定待查找记录的所在的范围，然后逐渐缩小查找的范围，直至找到该记录为止（也可能查找失败）。

在最简单的形式中，二分查找对具有指定左索引和右索引的连续序列进行操作。这就是所谓的查找空间。二分查找维护查找空间的左、右和中间指示符，并比较查找目标或将查找条件应用于集合的中间值；如果条件不满足或值不相等，则清除目标不可能存在的那一半，并在剩下的一半上继续查找，直到成功为止。如果查以空的一半结束，则无法满足条件，并且无法找到目标。

See detailed explanation on the binary search solution: https://www.lintcode.com/problem/401/solution/19308?fromId=164&_from=collection

复杂度分析
算法一
时间复杂度
每次找最小的是**O(N)O(N)的，所以总复杂度是O(NK)O(NK)**的

空间复杂度
不用多开辟空间

算法二
时间复杂度
因为一开始队列里面最多n个元素，我们每次取出一个元素，有可能再压入一个新元素，所以队列元素数量的上限就是n，所以我们每次压入元素和取出元素都是logNlogN的，要执行k次，所以总复杂度**O(KlogN)O(KlogN)**

空间复杂度
开辟的堆的空间是**O(N)O(N)**的

算法三
时间复杂度
二分上下界分别是数组的最大值和最小值 O(logMX)O(logMX)

二分判定 枚举n个数组**O(N)O(N)** 每个数组用一次upper_boundupper 
b
​
 ound 时间复杂度**O(logM)O(logM)**

所以总的时间复杂度是** O(NlogMlogMX)O(NlogMlogMX)**

空间复杂度
并不需要多开辟空间

```python
# Method II
from heapq import *

class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        # write your code here
        # 初始化 优先堆 ，我们堆的一个元素包括三个值 ：数字大小，数字在哪个数组里，数字在数组的哪个位置
        heap = []
        for i in range(len(matrix)):
            # 如果这个数组为空 则不用压入
            if len(matrix[i]) == 0:
                continue
            # matrix[i][0] 权值大小  i 在第i个数组   0 在该数组的0位置
            heappush(heap, [matrix[i][0], i, 0])
        while k > 1:
            k -= 1
            # 取出堆中最小值
            point = heappop(heap)
            value = point[0]
            arraysIdx = point[1]
            idx = point[2]
            # 已经是所在数组的最后一个元素了
            if (idx == len(matrix[arraysIdx]) - 1):
                continue
            else:
                # 压入该数组的下一个元素
                newvalue = matrix[arraysIdx][idx + 1]
                heappush(heap, [newvalue, arraysIdx, idx + 1])
        return heappop(heap)[0]
```

```python
# Method III
class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    # 计算有多少个数比x大
    def calc(self, x, matrix):
        n = len(matrix)
        num = 0
        for i in range(n):
            
            #二分查找这个数组里比x大的有多少个
            left = -1
            right = len(matrix[i])
            pos = -1
            while left + 1 < right:
                mid = left + (right - left) // 2
                mid = int(mid)
                if matrix[i][mid] > x:
                    right = mid
                    pos = mid
                else:
                    left = mid
            if pos != -1:
                num += len(matrix[i]) - pos
        return num
    def kthSmallest(self, matrix, k):
        # write your code here
        left = matrix[0][0]
        right = matrix[0][0]
        
        #行数与列数
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                # 确定二分的上下界
                left = min(left, matrix[i][j])
                right = max(right, matrix[i][j])
        left -= 1
        right += 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            mid = int(mid)
            # 判定mid是不是第k小
            num = self.calc(mid, matrix)
            
            #小于等于x超出k个 缩小上界
            if (n * m - num >= k):
                right = mid
            #提高下界
            else:
                left = mid
        return right
```

