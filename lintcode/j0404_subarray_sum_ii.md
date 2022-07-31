# Intro

使用同向双指针的九章模板,时间复杂度O(n)。 注意有个坑就是right指针需要保证在left
指针右边，所以需要加上

if (right <= left) {
right = left + 1;
}

的逻辑，令狐冲老师的算法班互动课有详细的讲述。

如果不加上上面逻辑，start, end某个值为0或者负数就会出错。（为0的时候，左右指针重
叠，会重复计算很多空array，负数的时候右指针会到左指针左边）。


# Bisect by DDBear
https://www.lintcode.com/problem/404/solution/23519


```python

class Solution:

    """

    @param A: An integer array

    @param start: An integer

    @param end: An integer

    @return: the number of possible answer

    """

    def subarraySumII(self, A, start, end):

        # write your code here

        n = len(A)

        ans = 0

        #求出前缀和数组

        pre = [0]

        for i in range(n):

            pre.append(pre[i] + A[i])

        for right in range(1, n + 1):

            #特判

            if A[right - 1] > end or pre[right] < start:

                continue

            #二分求第一个一个大于等于pre[right] - end的位置leftStart

            leftStart = self.findStart(pre, right, pre[right] - end)

            #二分求最后一个一个小于等于pre[right] -  start的位置leftEnd

            leftEnd = self.findEnd(pre, right, pre[right] - start)

            #累加答案

            ans += leftEnd - leftStart + 1

        return ans

    def findStart(self, pre, m, value):

        l = 0 

        r = m - 1

        while l + 1 < r:

            mid = (l + r) // 2

            if pre[mid] >= value:

                r = mid

            else:

                l = mid

        if pre[l] >= value:

            return l

        return r

        

    def findEnd(self, pre, m, value):

        l = 0

        r = m - 1

        while l + 1 < r:

            mid = (l + r) // 2

            if pre[mid] <= value:

                l = mid

            else:

                r = mid

        if pre[r] <= value:

            return r

        return l
```


# Two pointers
https://www.lintcode.com/problem/404/solution/23519
```python

class Solution:

    """

    @param A: An integer array

    @param start: An integer

    @param end: An integer

    @return: the number of possible answer

    """

    def subarraySumII(self, A, start, end):

        # write your code here

        n = len(A)

        ans = 0

        if end == 0:

            return 0

        sumStart = A[0]

        sumEnd = A[0]

        leftStart= 0

        leftEnd = 0

        if A[0] >= start and A[0] <= end:

            ans += 1

        

        for right in range(1, n):

            #移动右指针，累加前缀和

            sumStart += A[right]

            sumEnd += A[right]

            #移动左指针1

            while sumStart > end:

                sumStart -= A[leftStart]

                leftStart += 1

            

            #移动左指针2

            while sumEnd - A[leftEnd] >= start:

                sumEnd -= A[leftEnd]

                leftEnd += 1

            

            #若满足条件累加答案

            if sumEnd >= start and sumStart <= end:

                ans += leftEnd - leftStart + 1

            

        

        return ans
```


# Three pointers
https://www.lintcode.com/problem/404/solution/18426
```python
class Solution:
    def subarraySumII(self, A, start, end):
        n = len(A)
        if n == 0:
            return 0
        left_sum, right_sum = 0, 0
        left, right, i = 0, 0, 0
        res = 0
        for i in range(n):
            if A[i] > end: # reset
                left, right = i + 1, i + 1
                left_sum, right_sum = 0, 0
                continue
            while left <= n - 1 and left_sum + A[left] < start:
                left_sum += A[left]
                left += 1
            while right <= n - 1  and right_sum + A[right] <= end:
                right_sum += A[right]
                right += 1
            res += right - left
            left_sum -= A[i]
            right_sum -= A[i]
        return res
```


# Sliding windows

## version 1
https://www.lintcode.com/problem/404/solution/35708
```python
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        if not A:
            return 0
        return self.atMostK(A, end) - self.atMostK(A, start - 1)

    def atMostK(self, nums, k):
        if k <= 0:
            return 0

        n = len(nums)
        i = j = 0
        count = 0
        subsum = 0
        while j < n:
            c = nums[j]
            j += 1
            subsum += c

            while subsum > k:
                d = nums[i]
                i += 1
                subsum -= d

            count += j - i

        return count
```

## version 2
https://www.lintcode.com/problem/404/solution/19493
```python
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        l, r = 0, 0
        s1, s2 = 0, 0
        ans = 0
        for i in range(len(A)):
            while l <= i or l < len(A) and s1 < start:
                s1 += A[l]
                l += 1
            while r <= i or r < len(A) and s2 <= end:
                s2 += A[r]
                r += 1
            if start <= s1 <= end:
                if s2 > end:
                    ans += r - l
                else:
                    ans += r - l + 1
            s1 -= A[i]
            s2 -= A[i]
        return ans
```

# presum 结合二分法

思路还是用的 presum 结合二分法去做，二分法用的 `start＋1<end` 这样子的模板写的

```python
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        # write your code here
        n = len(A)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + A[i-1]
        
        cnt = 0
        for i in range(1, n+1):
            l = presum[i] - end
            r = presum[i] - start
            cnt += self.find(presum, r+1) - self.find(presum, l)
        return cnt
    
    def find(self, presum, target):
        m = len(presum)
        if presum[m-1] < target:
            return m
        
        start, end = 0, m - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if target <= presum[mid]:
                end = mid 
            else:
                start = mid
        
        if presum[end] < target:
            return end + 1
        if presum[start] < target:
            return start + 1
        return 0
```