解题思路
差分（扫描线） + 前缀和差分 / 

扫描线：确定每一时刻需要多少会议室。同时如果#需要的会议室 < rooms，那么置为0，表
明还有剩余的会议室可供安排；反之则置为1

前缀和：如果时刻为[start, end)的一个ask可以被安排上，则说明对于[start, end)这一
段区间内的每一时刻，它们都应该有空会议室剩余，即time_arr[i] == 0 (start ≤ i <
end)。那么这一段区间的总和sum(time_arr[start : end]) == 0。可以用「前缀和」处
理。

```python
class Solution:
    def meeting_room_i_i_i(self, intervals: List[List[int]], rooms: int, asks: List[List[int]]) -> List[bool]:
        def check(start, end) -> bool:  # [start,end]区间内的每一时刻的状态都该是0，因此这段区间的区间和=0
            return preSum[end + 1] - preSum[start] == 0
        
        arr = []
        max_time = max(ask[1] for ask in asks)
        for start, end in intervals:
            arr.append((start, 1))
            arr.append((end, -1))
            max_time = max(max_time, end)
        time_arr = [0 for _ in range(max_time + 1)]
        for time, score in arr:
            time_arr[time] += score
        cur_rooms = 0
        for i in range(len(time_arr)):
            cur_rooms += time_arr[i]
            time_arr[i] = 0 if cur_rooms < rooms else 1  # 0：还有空房；1：没有空房
        preSum = [0]  # 前缀和
        for state in time_arr:
            preSum.append(preSum[-1] + state)
        return [check(ask[0], ask[1] - 1) for ask in asks]
```


我们先放置已有的区间，去看那些时间点是空的。若在某个时间点为空，那么设置这一位为
0，否则设置为1。然后对这个数组求一个前缀和。通过前缀和数组我们可以发现，我们查找
的[l,r]区间要求sum[l],sum[l+1],sum[l+2]一直到sum[r-1]都为0，所以在前缀和中的表达
为sum[l-1]==sum[r-1]。这样我们通过预处理，就能O(1)的处理每一个询问了。

```python
class Solution:
    """
    @param intervals: the intervals
    @param rooms: the sum of rooms
    @param ask: the ask
    @return: true or false of each meeting
    """
    def meetingRoomIII(self, intervals, rooms, ask):
        # Write your code here.
        sum = [0 for i in range(50050)];
        vis = [0 for i in range(50050)];
        length = len(ask);
        ans = [False for i in range(length)];
        sum[0] = 0;
        maxn = 0;
        for i in range(0, len(intervals)):
            vis[intervals[i][0]] += 1;
            vis[intervals[i][1]] -= 1;
            maxn = max(maxn, intervals[i][1]);
        tmp = 0;
        for i in range(0, length):
            maxn = max(maxn, ask[i][1]);
        for i in range(1, maxn + 1):
            tmp += vis[i];
            if tmp < rooms:
                sum[i] = 0;
            else:
                sum[i] = 1;
        for i in range(1, maxn + 1):
            sum[i] += sum[i - 1];
        for i in range(0, length):
            if sum[ask[i][0] - 1] == sum[ask[i][1] - 1]:
                ans[i] = True;
            else:
                ans[i] = False;
        return ans;
```