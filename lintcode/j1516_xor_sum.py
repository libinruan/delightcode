# answer 1-A

# 从（0,0)走到（n-1，n-1）的走法为C（n+m-2）(n)种。所以我们可以发现，如果从(0,0)
# 开始搜索，那么搜索到终点的方案数是要超过int的，会导致TLE。所以本题，应该采用两
# 遍BFS。即划定一条分界线之后，从原点和终点各开始搜索到这条分界线为止。走过的路
# 径的状态存放在map中。

# xor操作是按位异或，在Java或C ++或python中表示为“ ^”对xor有疑问可查询 xor
# 1<=n,m<=20

class Solution:
    """
    @param arr: the arr 
    @param target: the target
    @return: the sum of paths 
    """
    def __init__(self):
        self.mp = [[{} for i in range(25)] for i in range(25)];
        self.goal = 0;
        self.ans = 0;
    def bfs1(self,arr):
        n = len(arr);
        m = len(arr[0]);
        mid = max(n, m) - 2;
        st = {
            'x':0,
            'y':0,
            'sum':arr[0][0]
        };
        queue = [];
        queue.append(st);
        while not len(queue) == 0:
            fir = queue.pop();
            i = fir['x'];
            j = fir['y'];
            k = fir['sum'];
            if i + j == mid:
                if not k in self.mp[i][j]:
                    self.mp[i][j][k] = 1;
                else:
                    self.mp[i][j][k] = self.mp[i][j][k] + 1;
                continue;
            if i + 1 < n:
                sec = {
                    'x':i + 1,
                    'y':j,
                    'sum':k ^ arr[i + 1][j]
                };
                queue.append(sec);
            if j + 1 < m:
                sec = {
                    'x':i,
                    'y':j + 1,
                    'sum':k ^ arr[i][j + 1]
                }
                queue.append(sec);
    def bfs2(self, arr):
        n = len(arr);
        m = len(arr[0]);
        mid = max(n, m) - 2;
        ed = {
            'x':n - 1,
            'y':m - 1,
            'sum':arr[n - 1][m - 1]
        };
        queue = [];
        queue.append(ed);
        
        while not len(queue) == 0:
            fir = queue.pop();
            i = fir['x'];
            j = fir['y'];
            k = fir['sum'];
            if i + j == mid + 1:
                if i - 1 >= 0:
                    if k ^ self.goal in self.mp[i - 1][j]:
                        self.ans += self.mp[i - 1][j][k ^ self.goal];
                if j - 1 >= 0:
                    if k ^ self.goal in self.mp[i][j - 1]:
                        self.ans += self.mp[i][j - 1][k ^ self.goal];
                continue;
            if i - 1 >= 0:
                sec = {
                    'x':i - 1,
                    'y':j,
                    'sum':k ^ arr[i - 1][j]
                };
                queue.append(sec);
            if j - 1 >= 0:
                sec = {
                    'x':i,
                    'y':j - 1,
                    'sum':k ^ arr[i][j - 1]
                }
                queue.append(sec);
    def xor_sum(self, arr: List[List[int]], target: int) -> int:
        # Write your code here.
        
        self.mid = 0;
        self.n = len(arr);
        self.m = len(arr[0]);
        self.mid = max(self.n, self.m) - 2;
        self.goal = target;
        if self.n != 1 or self.m != 1:
            self.ans = 0;
            self.bfs1(arr);
            self.bfs2(arr);
        else:
            if arr[0][0] == self.goal:
                self.ans = 1;
            else:
                self.ans = 0;
        return self.ans;



# answe 1-B.
# 套个双向BFS模板就行，注意碰到visited也要append，因为哪怕xy相
# 同，xorsum也可能不同。
# LI: doesn't work. MLE

from typing import (
    List,
)

class Solution:
    """
    @param arr: the arr 
    @param target: the target
    @return: the sum of paths 
    """
    def xor_sum(self, arr: List[List[int]], target: int) -> int:
        n, m = len(arr), len(arr[0])
        forward_q = collections.deque([(0, 0, arr[0][0])])
        backward_q = collections.deque([(n - 1, m - 1, arr[n - 1][m - 1])])
        forward_visited = set([(0, 0)])
        backward_visited = set([(n - 1, m - 1)])
        forward_dir = ((0, 1), (1, 0))
        backward_dir = ((0, -1), (-1, 0))
        forward_ans = [[{} for _ in range(m)] for _ in range(n)]   
        forward_ans[0][0][arr[0][0]] = 1
        backward_ans = [[{} for _ in range(m)] for _ in range(n)]
        backward_ans[n - 1][m - 1][arr[n - 1][m - 1]] = 1
        
        count = 0
        while forward_q and backward_q:
            resf = self.move(arr, forward_q, forward_dir, forward_visited, backward_visited, forward_ans)
            if resf:
                for xorsum, newx, newy in resf:
                    if (xorsum ^ target) in backward_ans[newx][newy]:
                        count += backward_ans[newx][newy][xorsum ^ target]
                break
            
            resb = self.move(arr, backward_q, backward_dir, backward_visited, forward_visited, backward_ans)
            if resb:
                for xorsum, newx, newy in resb:
                    if (xorsum ^ target) in forward_ans[newx][newy]:
                        count += forward_ans[newx][newy][xorsum ^ target]
                break            
        return count
                    
        
    def move(self, arr, q, dir, visited, oppo_visited, ans):
        n, m = len(arr), len(arr[0])
        res = []
        size = len(q)
        for _ in range(size):
            x, y, xorsum = q.popleft()
            for dx, dy in dir:
                newx, newy = x + dx, y + dy
                if not (0 <= newx < n and 0 <= newy < m):
                    continue
                
                # if (newx, newy) in visited:
                #     continue
                
                newxorsum = xorsum ^ arr[newx][newy]
                ans[newx][newy][newxorsum] = ans[newx][newy].get(newxorsum, 0) + 1
                q.append((newx, newy, newxorsum))
                visited.add((newx, newy))
                if (newx, newy) in oppo_visited:
                    res.append((xorsum, newx, newy))
        return res