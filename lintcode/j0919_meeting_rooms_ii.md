<!-- ------------------------------- DDBear -------------------------------- -->
算法

算法一 前缀和
在开始时间位置+1房间，在结束时间-1房间，求一遍前缀和，就是对应时间房间的数量,
我们的房间数量要满足所有时间的需求，所以答案就是对所有时间所需要的最少房间取最大值，这样就能满足所有时间的开会需求了。
前缀和算法涉及到了对时间离散化，所以这里更推荐扫描线

算法二 扫描线
扫描线，把所有的时间排序，按照开始时间升序，开始时间相同结束时间升序的方式进行排序，如果时间相同，结束时间在前，
扫描一遍，当扫描到开始时间，就会多一个房间，当扫描到结束时间就少一个房间，这样扫描到i时候就是i时间所需要的最少的房间
我们的房间数量要满足所有时间的需求，所以答案就是对所有时间所需要的最少房间取最大值，这样就能满足所有时间的开会需求了。

复杂度分析
时间复杂度

算法一 前缀和
前缀和 O(Time) Time表示最大时间

算法二 扫描线
扫描线 O(NlogN) N是会议数量

空间复杂度
算法一 前缀和
前缀和 O(Time) Time表示最大时间

算法二 扫描线
扫描线 O(N) N是会议数量

代码
扫描线

```python
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        room=[]
        #加入开始时间和结束时间，1是房间+1，-1是房间-1
        for i in intervals:
            room.append((i.start,1))
            room.append((i.end,-1))
        tmp=0
        ans=0
        #排序
        room=sorted(room)
        #扫描一遍
        for idx,cost in room:
            tmp+=cost
            ans=max(ans,tmp)
        return ans
```

前缀和
```python
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        # 前缀和数组
        room = {}
        # 开始时间+1，结束时间-1
        for i in intervals:
            room[i.start] = room.get(i.start, 0) + 1
            room[i.end] = room.get(i.end, 0) - 1
        ans = 0
        tmp = 0
        for i in sorted(room.keys()):
            tmp = tmp + room[i]
            ans = max(ans, tmp)
        return ans
```

<!-- ------------------------------ Great Dog ------------------------------ -->

方法：有序化 - https://www.lintcode.com/problem/919/solution/57831?fromId=164&_from=collection
提供给我们的会议时间可以确定一天中所有事件的时间顺序。我们拿到了每个会议的开始和
结束时间，这有助于我们定义此顺序。

根据会议的开始时间来安排会议有助于我们了解这些会议的自然顺序。然而，仅仅知道会议
的开始时间，还不足以告诉我们会议的持续时间。我们还需要按照结束时间排序会议，因为
一个“会议结束”事件告诉我们必然有对应的“会议开始”事件，更重要的是，“会议结束”事件
可以告诉我们，一个之前被占用的会议室现在空闲了。

一个会议由其开始和结束时间定义。然而，在本算法中，我们需要 分别 处理开始时间和结
束时间。这乍一听可能不太合理，毕竟开始和结束时间都是会议的一部分，如果我们将两个
属性分离并分别处理，会议自身的身份就消失了。但是，这样做其实是可取的，因为：

当我们遇到“会议结束”事件时，意味着一些较早开始的会议已经结束。我们并不关心到底是
哪个会议结束。我们所需要的只是 一些 会议结束,从而提供一个空房间。

算法

1. 分别将开始时间和结束时间存进两个数组。
2. 分别对开始时间和结束时间进行排序。请注意，这将打乱开始时间和结束时间的原始对应关系。它们将被分别处理。
3. 考虑两个指针：s_ptr 和 e_ptr ，分别代表开始指针和结束指针。开始指针遍历每个会议，结束指针帮助我们跟踪会议是否结束。
4. 当考虑 s_ptr 指向的特定会议时，检查该开始时间是否大于 e_ptr 指向的会议。若如此，则说明 s_ptr 开始时，已经有会议结束。于是我们可以重用房间。否则，我们就需要开新房间。
5. 若有会议结束，换而言之，start[s_ptr] >= end[e_ptr] ，则自增 e_ptr 。
6. 重复这一过程，直到 s_ptr 处理完所有会议。

```python
# O(NlogN), O(N)
class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i.start for i in intervals])
        end_timings = sorted(i.end for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1
            start_pointer += 1

        return used_rooms
```

方法：优先队列
我们无法按任意顺序处理给定的会议。处理会议的最基本方式是按其 开始时间 顺序排序，
这也是我们采取的顺序。这就是我们将遵循的顺序。毕竟，在担心下午5：00的会议之前，
你肯定应该先安排上午9：00的会议，不是吗？

算法

- 按照 开始时间 对会议进行排序。

- 初始化一个新的 最小堆，将第一个会议的结束时间加入到堆中。我们只需要记录会议的结束时间，告诉我们什么时候房间会空。

- 对每个会议，检查堆的最小元素（即堆顶部的房间）是否空闲。
1. 若房间空闲，则从堆顶拿出该元素，将其改为我们处理的会议的结束时间，加回到堆中。
2. 若房间不空闲。开新房间，并加入到堆中。

- 处理完所有会议后，堆的大小即为开的房间数量。这就是容纳这些会议需要的最小房间数。

```python
# O(NlogN), O(N) 
# Very detailed explanation on complexity:
#   https://www.lintcode.com/problem/919/solution/57828?fromId=164&_from=collection
import heapq

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x.start)

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0].end)

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i.start:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i.end)

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)
```
