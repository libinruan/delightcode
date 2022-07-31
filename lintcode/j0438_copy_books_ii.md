# bisect
与437类似，可以用二分法。判断标准为：给定某个时间，所有人能copy的总数量是否大于n。
![](https://i.postimg.cc/3JwTvJpF/Jiuzhang-vip-30days.png)

```python
class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    # 返回是否能够在mid的时间内复印完成n本书
    def check(self, times, n, mid):
        sum = 0
        for i in times:
            sum += mid // i
        return sum >= n
        
    def copyBooksII(self, n, times):
        left, right = 0, n * times[0]
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.check(times, n, mid):
                right = mid
            else:
                left = mid
        if self.check(times, n, left):
            return left;
        return right
```

# Greedy
![](https://i.postimg.cc/FzNhqy7M/Jiuzhang-vip-30days.png)
```python
class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copyBooksII(self, n, times):
        k = len(times)
        times = sorted(times)
        min_sum = 0
        # 存储每个人花费的总时间
        sum = [0] * k
        for i in range(1, n + 1):
            pos = 0
            for j in range(k):
                if sum[j] + times[j] <= min_sum:
                    # 如果增加一本书给j复印不增加时间，任选其中一种即可
                    pos = j
                    break
                elif sum[j] + times[j] < sum[pos] + times[pos]:
                    # 如果必须有增加时间，选择最少的一种
                    pos = j
            # 被选择的这个人花费的总时间增加
            sum[pos] += times[pos]
            # 最少需要的分钟数 = 每个人花费的总时间的最大值
            min_sum = max(min_sum, sum[pos])
        return min_sum
```

# bisect
二分答案，用的是left<=right模板，不是left+1<right
```python

public class Solution {
    /**
     * @param n: An integer
     * @param times: an array of integers
     * @return: an integer
     */
    public int copyBooksII(int n, int[] times) {
        int minTime = Integer.MAX_VALUE;
        int maxTime = 0;
        
        for(int time: times) {
            minTime=Math.min(minTime, time);
            maxTime=Math.max(maxTime, time);
        }
        
        int left = minTime, right = maxTime * n;
        
        while(left<=right) {
            int mid = (left+right)/2;
            int count = countNumOfBooks(times, mid);
            if(count>=n) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        
        return left;
    }
    
    private int countNumOfBooks(int[] times, int time) {
        int n = 0;
        for(int t: times) {
            n+=time/t;
        }
        return n;
    }
}
```


# bisect iii

二分答案，最小时间是times中的最小值， 最大时间是最慢的人copy所有的书
检查方程， 就是在给定的时间里，所有人并行工作，最多能copy多少本书。
```python

import sys

class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copyBooksII(self, n, times):
        # write your code here
        left = sys.maxsize
        right = 0
        for time in times:
            left = min(left, time)
            right = max(right, time)
        
        right *= n 
              
        while left + 1 < right:
            mid = (left + right) // 2
            if self.copyBooks(times, mid) >= n:
                right = mid
            else:
                left = mid
        
        if self.copyBooks(times, left) >= n:
            return left
        
        return right
        
    def copyBooks(self, times, limit):
        count = 0;
        for time in times:
            count += limit // time
        
        return count
```

# bisect iv
binary search + greedy
开始加了个sort 可能可以加快速度 因为helper fucntion判断会加快

```python

class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copyBooksII(self, n, times):
        # write your code here
        if n == 0:
            return 0
        if n < 0 or not times:
            return -1
        
        times.sort() # faster to get count >= n
        start, end = min(times), min(times) * n
        
        while start < end - 1:
            mid = (start + end) // 2
            # compare the counts of the finished-copy books
            if self.finish(n, times, mid):
                end = mid
            else:
                start = mid
        if self.finish(n, times, start):
            return start
        return end
    
    def finish(self, n, times, total_time):
        count = 0
        for time in times:
            count += total_time // time
            if count >= n:
                return True
        return False
```