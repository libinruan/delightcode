# min heap
O(N log k)
## version 1
https://www.lintcode.com/problem/486/solution/16693
```python
import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        result = []
        heap = []
        for index, array in enumerate(arrays):
            if len(array) == 0:
                continue
            heapq.heappush(heap, (array[0], index, 0))
             
        while len(heap):
            val, x, y = heap[0]
            heapq.heappop(heap)
            result.append(val)
            if y + 1 < len(arrays[x]):
                heapq.heappush(heap, (arrays[x][y + 1], x, y + 1))
            
        return result
```

## version 2
https://www.lintcode.com/problem/486/solution/18464
```python

from heapq import *

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # 初始化 答案
        ans = []
        # 初始化 优先堆 ，我们堆的一个元素包括三个值 ：数字大小，数字在哪个数组里，数字在数组的哪个位置
        heap = []
        for i in range(len(arrays)):
            # 如果这个数组为空 则不用压入
            if len(arrays[i]) == 0:
                continue
            # arrays[i][0] 权值大小  i 在第i个数组   0 在该数组的0位置
            heappush(heap, [arrays[i][0], i, 0])
        while heap:
            # 取出堆中最小值
            point = heappop(heap)
            value = point[0]
            arraysIdx = point[1]
            idx = point[2]
            # 更新答案
            ans.append(value)
            # 已经是所在数组的最后一个元素了 
            if (idx == len(arrays[arraysIdx]) - 1):
                continue
            else:
                # 压入该数组的下一个元素
                newvalue = arrays[arraysIdx][idx + 1]
                heappush(heap, [newvalue, arraysIdx, idx + 1])
        return ans
        # write your code here

```

# Divide-and-Conquer (recursive method)
自顶向下的分治法
```python
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        return self.merge_range_arrays(arrays, 0, len(arrays) - 1)
        
    def merge_range_arrays(self, arrays, start, end):
        if start == end:
            return arrays[start]
        
        mid = (start + end) // 2
        left = self.merge_range_arrays(arrays, start, mid)
        right = self.merge_range_arrays(arrays, mid + 1, end)
        return self.merge_two_arrays(left, right)
        
    def merge_two_arrays(self, arr1, arr2):
        i, j = 0, 0
        array = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                array.append(arr1[i])
                i += 1
            else:
                array.append(arr2[j])
                j += 1
        while i < len(arr1):
            array.append(arr1[i])
            i += 1
        while j < len(arr2):
            array.append(arr2[j])
            j += 1
        return array
```

# Merge (non-recursive method)
https://www.lintcode.com/problem/486/solution/17793

probably time complexity: O (NK log K)
```python
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        while len(arrays) > 1:
            next_arrays = []
            for i in range(0, len(arrays), 2):
                if i + 1 < len(arrays):
                    array = self.merge_two_arrays(arrays[i], arrays[i + 1])
                else:
                    array = arrays[i]
                next_arrays.append(array)
            arrays = next_arrays
                
        return arrays[0]
        
    def merge_two_arrays(self, arr1, arr2):
        i, j = 0, 0
        array = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                array.append(arr1[i])
                i += 1
            else:
                array.append(arr2[j])
                j += 1
        while i < len(arr1):
            array.append(arr1[i])
            i += 1
        while j < len(arr2):
            array.append(arr2[j])
            j += 1
        return array
```

# Heap, D & C, Merge sort - variant 2
Merge sort 的三种解法，时间复杂度都是 O(NlogK)

直接使用 heap
从第一个元素开始，不断和后面的元素进行 merge
采用 merge sort 的思路，不断进行两两 merge

```python
############  第一种解法，直接用 heap ##################
import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        heap = []
        result = []
        for index, par in enumerate(arrays):
            if len(par) == 0:
                continue
            heapq.heappush(heap, [par[0], index, 0])
    
        while len(heap) > 0:
            val, i, j = heapq.heappop(heap)
            result.append(val)
        
            if j + 1 < len(arrays[i]):
                heapq.heappush(heap, [arrays[i][j + 1], i, j + 1])
                
        return result

#################### 第二种解法，将后面的元素不断和result 进行合并 ################
import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        cur = arrays[0]
        k = 1
        while k < len(arrays):
            cur = self.merge(cur, arrays[k])
            k += 1
        return cur
        
    
    def merge(self, a, b):
        a_left = 0
        b_left = 0
        index = 0
        result = [0 for _ in range(len(a) + len(b))]
    
        while a_left < len(a) and b_left < len(b):
            if a[a_left] < b[b_left]:
                result[index] = a[a_left]
                index += 1
                a_left += 1
            else:
                result[index] = b[b_left]
                index += 1
                b_left += 1
            
        while a_left < len(a):
            result[index] = a[a_left]
            index += 1
            a_left += 1
    
        while b_left < len(b):
            result[index] = b[b_left]
            index += 1
            b_left += 1
    
        return result
    
#####################  第三种解法，两两合并 ##################
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        start = 0
        end = len(arrays)- 1
        return self.sort(arrays, start, end)
        
        
        
    def sort(self, arrays, start, end):
        if start == end:
            return arrays[start]
        left = self.sort(arrays, start, (start + end) // 2)
        right = self.sort(arrays, (start +end) // 2 + 1, end)
        
        return self.merge(left, right)
    
    def merge(self, arr1, arr2):
        result = [0 for _ in range(len(arr1) + len(arr2))]
        left = 0
        right = 0
        index = 0
        
        while left < len(arr1) and right < len(arr2):
            if arr1[left] < arr2[right]:
                result[index] = arr1[left]
                index += 1
                left += 1
            else:
                result[index] = arr2[right]
                index += 1
                right += 1
        
        while left < len(arr1):
            result[index] = arr1[left]
            index += 1
            left += 1
        
        while right < len(arr2):
            result[index] = arr2[right]
            index += 1
            right += 1
        
        return result
```

# Heap, D & C, Merge sort - variant 3 (TinLittle)
两两合并的思路，看过的无外是两种，一个是自顶向下的基于递归的分制法，另一个是自底向上的迭代法。

这里给出一个原创的迭代变种，用到了堆，但不是那种从堆里一个个元素往外拿的方法。

这里解决的一个问题是当子数组长度不均匀时，如何优化选择拿哪两个子数组做下一次归并。最优选择是最短的两个数组先合并。如何快速简捷的找到
两个最短的数组呢？当然是用堆了。把每个自数组的长度和指针放入堆，每次弹出两个就是最小的两个。

建议把其它三种解法都掌握了以后再来看这个解法。可以开拓思路，对这题的可能的follow up也能准备的更好。

```python
class Solution:
    
    def mergekSortedArrays(self, arrays) -> list:
    
        h = [(len(array), i) for i, array in enumerate(arrays) if len(array) > 0]
        
        if not h: return []
        
        heapify(h)

        while h:
            if len(h) == 1:
                return arrays[h[0][1]]
                
            _, index_1 = heappop(h)
            _, index_2 = heappop(h)

            merged = self.merge_two_arrays(arrays[index_1], arrays[index_2])
            arrays[index_1] = merged 
            heappush(h, (len(merged), index_1))

    def merge_two_arrays(self, nums1, nums2):
        
        nums = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1 
            else:
                nums.append(nums2[j])
                j += 1 
        if i < len(nums1):
            nums.extend(nums1[i:])
        if j < len(nums2):
            nums.extend(nums2[j:])
        return nums
```