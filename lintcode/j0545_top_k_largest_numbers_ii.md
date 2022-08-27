Description
Implement a data structure, provide two interfaces:

add(number). Add a new number in the data structure.
topk(). Return the top k largest numbers in this data structure. k is given when we create the data structure.

https://www.lintcode.com/problem/545/description


# Official answer
用一个最大堆维护这些数字，当遇到add(number)这个操作时，就将元素加入到最大堆中，当遇到topk操作时就分K次取出最大堆顶元素，返回这些元素，然后将刚才加入的元素放回最大堆即可

> Tech - To create a heap, use a list initialized to [], or you can transform a populated list into a heap via function heapify().
>
> [Source](https://docs.python.org/3/library/heapq.html)


```python
import heapq

class Solution:

    # @param {int} k an integer
    def __init__(self, k):
        self.k = k
        self.heap = []
        
    # @param {int} num an integer
    def add(self, num):
        heapq.heappush(self.heap, num)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

    # @return {int[]} the top k largest numbers in array
    def topk(self):
        return sorted(self.heap, reverse=True)

```