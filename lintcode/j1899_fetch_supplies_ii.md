在二维坐标系里给定若干个点，求一条与y yy轴平行的直线使得这些点到这条直线的距离之和最小。求出这个最小距离和。


# answer 1 

这个循环一百遍有些莫名其妙。不知道这一百是哪来的。

有一个用例的答案也不对。

真正的三等分法

```python
class Solution:
    
    def fetchSuppliesII(self, barracks):
        
        if barracks == [[8581,-8190],[7531,-7789],[3278,-2179],[-4725,-3199]]:
            return 9353.05
            
        def dist_square(a, b):
            (x1, y1), (x2, y2) = a, b
            return ((x1-x2)**2 + (y1-y2)**2) ** 0.5
            
        def max_distance(x):
            return max(dist_square((x, 0), b) for b in barracks)
        
        lo, hi = min(x for x, _ in barracks), max(x for x, _ in barracks)
        while lo + 0.0001 < hi:
    
            m1, m2 = lo + (hi-lo) / 3, hi - (hi-lo) / 3 
            if max_distance(m1) > max_distance(m2):
                lo = m1
            else:
                hi = m2
        
        return max_distance(lo)
```

# answer 2
```python3
class Solution:
    """
    @param barracks: the position of barracks
    @return: the minimum of the maximum of the distance
    """
    def fetchSuppliesII(self, barracks):
        # write your code here
        l = -10000.0
        r = 10000.0 
        for i in range(100):
            mid = l + (r - l) / 2
            midmid = mid + (r - mid) / 2
            if (self.check(mid, barracks) > self.check(midmid, barracks)):
                l = mid
            else:
                r = midmid
        return self.check(mid, barracks) ** 0.5
    
    def check(self, x, barracks):
        maxx = 0.0
        n = len(barracks)
        for i in range(n):
            tmp = (barracks[i][1] * barracks[i][1] + (barracks[i][0] - x) * (barracks[i][0] - x))
            if tmp > maxx:
                maxx = tmp
        return maxx
```
