# solution 1 
https://www.lintcode.com/problem/1426/solution/19437
逆递推
假设跳跃前能力为E,要跳的高度为H，那么跳跃后的能量就是2E-H，
那么跳跃后的能量加上高度就是跳跃前的两倍，然后从后往前逆推可以获得答案
```python
class Solution:
    """
    @param height: the Building height
    @return: The minimum unit of initial energy required to complete the game
    """
    def LeastEnergy(self, height):
        E = 0
        for i in range(len(height) - 1,-1,-1):
            E = (E + height[i] + 1) / 2
        return math.floor(E)
```
为啥要+1? 
是为了求 Math.ceiling(x / 2)， 假设 2*E = 3， E应该取2 而不是1,否则就会出现负数的E。

# solution 2 DDBear
https://www.lintcode.com/problem/1426/solution/23129
算法：dp / 二分

本题不建议用二分，在题目标准数据下，很容易造成值溢出，故二分只提供python代码

dp做法：
很显然，我们可以从尾部开始往头部走，保证一路没有小于0的情况，那么最后的头部就是确定的E(0)

令f(n)=E(n), 则f(n+1) = 2f(n) - H(n+1) >= 0,所以 f(n) = Math.ceil((f(n+1) + H(n+1))/2)

最后用递推从n -> 0 即可求出f(0),也就是E(0)

复杂度分析

时间复杂度O(n)
n为heightheight的大小
空间复杂度O(1)
不用额外空间
二分做法：
通过观察可以发现，E(0)不会大于最大的height

那么我们二分0-max(height)这个区间，对于每一个mid，遍历一次height，判断能否在跳跃过程中保证能量不为负数，不断寻找最小的E(0）

复杂度分析

时间复杂度O(nlogm)
n为height的大小，m为height的最大值
空间复杂度O(1)
不用额外空间

```python
# dp
class Solution:
    """
    @param height: the Building height
    @return: The minimum unit of initial energy required to complete the game
    """
    def LeastEnergy(self, height):
        E = 0
        # 倒序递推
        for i in range(len(height) - 1,-1,-1):
            E = (E + height[i] + 1) / 2
        return math.floor(E)
# 二分
class Solution:
    """
    @param height: the Building height
    @return: The minimum unit of initial energy required to complete the game
    """
    def LeastEnergy(self, height):
        # 二分区间[0,max(height)]
        left, right = 0, max(height)
        while left +1 < right:
            mid = int(left + (right - left) / 2)
            # 二分区间
            if self.check(mid,height):  
                right = mid
            else:
                left = mid
        if self.check(left,height):
            return left
        return right
    def check(self,power,height):
        for i in range(len(height)):
            if power > height[i]:
                power += power - height[i]
            else:
                power -= height[i] - power
            # 判断是否存在能量值小于0的情况
            if power < 0:
                return False
        return True
```

# solution 3 bisect
https://www.lintcode.com/problem/1426/solution/23130
```python
class Solution:
    """
    @param height: the Building height
    @return: The minimum unit of initial energy required to complete the game
    """
    def LeastEnergy(self, height):
        low = 0
        high = sum(height)
        while (low + 1 < high):
            mid = low + (high - low) // 2
            if self.is_energy_enough(mid, height):
                high = mid
            else:
                low = mid
        if self.is_energy_enough(low, height):
            return low
        else:
            return high
        
    def is_energy_enough(self, energy, height):
        energy_left = energy
        for h in height:
            energy_left = 2 * energy_left - h
            if energy_left < 0:
                return False
        return True
```