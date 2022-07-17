这题的正解有三种。

当 k 接近 1 时，用计数排序，counting sort，时间O(N)，空间O(k)
当 k 在 1 和 N 之间中位数，用彩虹排序，rainbow sort，时间O(nLogK)，空间O(logK)--递归栈的深度
当 k 接近 N 时，直接用快速排序。
这里给出计数排序和彩虹排序的解。

source: https://www.lintcode.com/problem/143/solution/17513?fromId=164&_from=collection

```python
class Solution_counting_sort:
    
    def sortColors2(self, colors, k):
        
        counter = [0 for _ in range(k+1)]
        
        for color in colors:
            counter[color] += 1 
            
        index = 0
        for color, count in enumerate(counter):
            for _ in range(count):
                colors[index] = color 
                index += 1 
        
class Solution_rainbow_sort:
    
    def sortColors2(self, colors, k):
        
        self.color_partition(colors, 0, len(colors)-1, 1, k)
        
    def color_partition(self, colors, start, end, lo, hi):
        
        if lo == hi or start == end:
            return
        
        k = (lo+hi) // 2
        
        pivot = colors[end]
        left, right = start, end 
        while left <= right:
            while left <= right and colors[left] <= k:
                left += 1 
            while left <= right and colors[right] > k:
                right -= 1 
                
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1 
                right -= 1 
                
        self.color_partition(colors, start, right, lo, k)
        self.color_partition(colors, left, end, k+1, hi)
```

<!-- ------------------------------ Quicksort ------------------------------ -->
基于QuickSort的算法，区别是pivot使用k的二分，所以时间复杂度是 O(nlogk). 运行时间554ms。
*需要注意的点：在partrition的时候，左右两边需要严格分为 < pivot 和 >= pivot。 这点和二分的模版不同
```python
class quickSort(object):
    def __init__(self,nums,pivot):
        self.A = nums
        self.sort(0,len(self.A)-1,0,pivot)
        
    def sort(self,start,end,pstart,pend):
        if start >= end or pstart>=pend:
            return 
        pivot = pstart + (pend-pstart)/2
        l,r = start,end
        while l <= r:
            while l<=r and self.A[l] <= pivot:
                l += 1
            while l<= r and self.A[r] > pivot:
                r -= 1
            if l<=r:
                self.A[l],self.A[r] = self.A[r],self.A[l]
                l += 1
                r -= 1
        #print pivot,self.A
        self.sort(start,r,pstart,pivot)
        self.sort(l,end,pivot+1,pend)
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        
        quickSort(colors,k)
```
