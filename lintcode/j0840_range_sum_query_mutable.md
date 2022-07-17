一道维护序列"单点修改, 区间查询"的模板题.

可以用树状数组, 区间树, 平衡树等数据结构解决.

而这道题目比较简单, 并且需要维护的区间信息为区间和(具有可加性, 可用前缀和相减求得区间和),

所以推荐使用树状数组: 一种简洁, 优美的数据结构.

source: https://www.lintcode.com/problem/840/solution/18217?fromId=164&_from=collection

```python
class NumArray(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = nums
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        for i in range(self.n):
            self.add(i, self.arr[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.add(i, val - self.arr[i])
        self.arr[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j) - self.sum(i - 1)
        
    def lowbit(self, x):
        return x & (-x)
    
    def add(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] += val
            idx += self.lowbit(idx)
    
    def sum(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= self.lowbit(idx)
        return res
```

<!-- ----------------------------- adnil81300 ------------------------------ -->
分享一个基于数组的线段树构造代码，感觉更简洁，更好记忆， 基于node的线段树实在有点长。
```python
class NumArray:

    def __init__(self, nums):
        self.size = len(nums)
        self.tree_arr = self.size * [0] + nums
        for i in range(self.size - 1, 0, -1):
            # i's sons are 2i, 2i + 1
            self.tree_arr[i] = self.tree_arr[i << 1] + self.tree_arr[i << 1 | 1]

    def update(self, i: int, val: int) -> None:
        i += self.size
        self.tree_arr[i] = val
        while i > 1:
            # if i is odd, left is i - 1, if i is even, right is i + 1
            self.tree_arr[i >> 1] = self.tree_arr[i] + self.tree_arr[i ^ 1]
            i >>= 1

    def sumRange(self, i: int, j: int) -> int:
        l = i + self.size
        r = j + self.size
        res = 0
        while l <= r:
            if l & 1:
                res += self.tree_arr[l]
                l += 1
            l >>= 1
            if not r & 1:
                res += self.tree_arr[r]
                r -= 1
            r >>= 1
        return res
```
NOTE
1. self.tree_arr[i] = self.tree_arr[i << 1] + self.tree_arr[i << 1 | 1] 可以写成tree_arr[i * 2] + tree_arr[i * 2 + 1]。

<!-- ------------------------------ xfsm1912 ------------------------------- -->
根据令狐老师前天新更新的代码改写的Python版本，用的方法是树状数组
```python
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = [0 for i in range(len(nums))]
        self.bitree = [0 for i in range(len(nums) + 1)]
        
        for i in range(len(nums)):
            self.update(i, nums[i])
            

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        delta = val - self.arr[i]
        self.arr[i] = val
        index = i + 1
        
        while index <= len(self.arr):
            self.bitree[index - 1] += delta
            index += self.lowbit(index)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getPrefixSum(j) - self.getPrefixSum(i - 1)
        
    def getPrefixSum(self, i):
        sum = 0
        index = i + 1 
        while index > 0:
            sum += self.bitree[index - 1]
            index -= self.lowbit(index)
            
        return sum 
        
    def lowbit(self, x):
        return x&-x

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)        
```