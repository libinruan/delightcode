<!-- ------------------------------- DDBear -------------------------------- -->
solution: https://www.lintcode.com/problem/391/solution/19730?fromId=164&_from=collection


算法
算法一 前缀和
在开始时间位置+1架飞机，在结束时间-1架飞机，求一遍前缀和，就是对应时间飞机的数量,

前缀和算法涉及到了对时间离散化，所以这里更推荐扫描线

算法二 扫描线
扫描线，把飞机按开始时间从小到大排序，如果开始时间相同，结束时间小的在前，

扫描一遍，当扫描到开始时间，就会多一架飞机,飞机数+1，当扫描到结束时间就少一架飞机，飞机数-1

答案取扫描过程中的最大飞机数


扫描线
```python
from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    """
    @param airplanes: an array of meeting time airplanes
    @return: the minimum number of conference rooms required
    """
    def countOfAirplanes(self, airplanes):
        # Write your code here
        room=[]
        #加入开始时间和结束时间，1是房间+1，-1是房间-1
        for i in airplanes:
            room.append((i.start,1))
            room.append((i.end,-1))
        tmp = 0
        ans = 0
        #排序
        room=sorted(room)
        #扫描一遍
        for idx, cost in room:
            tmp += cost
            ans = max(ans,tmp)
        return ans  
```

前缀和
LIPIN: 参考 919 会议室安排的写法
```python
class Solution:
    """
    @param airplanes: an array of meeting time airplanes
    @return: the minimum number of conference rooms required
    """
    def countOfAirplanes(self, airplanes):
        # Write your code here
        # 前缀和数组
        room = {}
        # 开始时间+1，结束时间-1
        for i in airplanes:
            room[i.start] = room.get(i.start, 0) + 1
            room[i.end] = room.get(i.end, 0) - 1
        ans = 0
        tmp = 0
        for i in sorted(room.keys()):
            tmp = tmp + room[i]
            ans = max(ans, tmp)
        return ans
```