# https://www.lintcode.com/problem/1139/description

# official 1
class Solution:
    """
    @param a: an array
    @param k: the kth
    @return: return the kth subarray
    """
    
    def check(self, x, a, k):
        tmp1 = 0
        tmp2 = 0
        now = a[0]
        l = -1
        r = 0
        n = len(a)
        all = n * (n + 1) // 2
        while l <= r and r < n:
            if now >= x:
                if now == x:
                    tmp2 = tmp2 + 1
                else:
                    tmp1 = tmp1 + 1
                tmp1 = tmp1 + n - r - 1
                l = l + 1
                now = now - a[l]
            else:
                r = r + 1
                if r < n:
                    now = now + a[r]
        if all - tmp1 - tmp2 < k and all - tmp1 >= k:
            return 0
        if all - tmp1 - tmp2 >= k:
            return 1
        return -1
    def thekthSubarray(self, a, k):
        # wrrite your code here
        n = len(a)
        sum = 0
        for i in range(n):
            sum = sum + a[i]
        l = 1
        r = sum
        while l <= r:
            mid = (l + r) // 2
            flag = self.check(mid, a, k)
            if flag == 0:
                return mid
            if flag == 1:
                r = mid - 1
            else:
                l = mid + 1



# https://www.lintcode.com/problem/1139/solution/17944
# answer 1 - 二分+双指针
class Solution:
    """
    @param a: an array
    @param k: the kth
    @return: return the kth subarray
    """
    def can(self, a, x):
        n = len(a)
        # res 子数组和超过x的数量
        # n*(n+1)/2-res  子数组和不超过x的数量
        res = 0
        # 双指针开始位置，结束位置
        # 对于每个start，找到最小的end，使得[start,end]求和大于x
        # [start,end],[start,end+1],[start,end+2].....[start,n-1] 求和都会大于x
        # 这样就找到了 n-end个区间使得 子数组和大于x
        # 若start1<start2,则对应的end1<=end2
        start = 0
        end = 0
        sum = a[start]
        while start < n:
            # 不停的扩展，end，直到子数组和大于x 或者end到达边界
            while sum <= x:
                end += 1
                if (end >= n):
                    break
                sum += a[end]
            # [start,end],[start,end+1],[start,end+2].....[start,n-1] 求和都会大于x
            if end < n:
                res += n - end
            # start移动到下一个位置
            sum -= a[start]
            start += 1
        # 总的子数组数量减去大于x的子数组的数量
        return (n + 1) * n // 2 - res
    def thekthSubarray(self, a, k):
        # wrrite your code here
        n = len(a)
        left = 0
        right = 0
        for i in range(n):
            right += a[i]
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.can(a, mid) >= k:
                right = mid
            else:
                left = mid
        return right



# https://www.lintcode.com/problem/1139/solution/62689
# 二分 + 滑动窗口
# answer 2-a 
class Solution:
    """
    @param a: an array
    @param k: the kth
    @return: return the kth subarray
    """
    def check(self, a, target):
        n = len(a)
        l = 0
        r = 0
        less = 0
        equal = 0
        cur = 0
        while l <= r and r < n:
            cur += a[r]
            if cur < target:
                less = less + r - l + 1
                r += 1
            else:
                while l <= r and cur >= target:
                    if cur == target:
                        equal += 1
                    cur -= a[l]
                    l += 1
                
                if cur == 0:
                    r = l
                else:
                    less = less + r - l + 1
                    r += 1
        return (less, equal)



    def thekth_subarray(self, a: List[int], k: int) -> int:
        n = len(a)
        l = a[0]
        r = sum(a)
        while l + 1 < r:
            mid = l + r >> 1
            less, equal = self.check(a, mid)
            if less + equal < k:
                l = mid
            else:
                r = mid
        
        less, equal = self.check(a, l)
        if less <= k and less + equal >= k:
            return l
        return r

# answer 2-b
from typing import (
    List,
)

class Solution:
    """
    @param a: an array
    @param k: the kth
    @return: return the kth subarray
    """
    def find(self, a, target):
        n = len(a)
        cur = 0
        l = 0
        r = 0
        cnt = 0
        while l <= r and r < n:
            cur += a[r]
            if cur < target:
                cnt += r - l + 1
                r += 1
            else:
                while l <= r and cur >= target:
                    cur -= a[l]
                    l += 1
                cnt += r - l + 1
                r += 1
        return cnt

    def thekth_subarray(self, a: List[int], k: int) -> int:
        n = len(a)
        l = a[0]
        r = sum(a)
        while l + 1 < r:
            mid = l + r >> 1
            less = self.find(a, mid)
            if less < k:
                l = mid
            else:
                r = mid
        
        if self.find(a, r) < k:
            return r
        return l