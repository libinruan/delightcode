[Problem](https://blog.csdn.net/roufoo/article/details/104338009)

# JZ sprint official solution
```python
DIRECTIONS = [(1, 2), (-1, 2), (2, 1), (-2, 1)]  # Python (i, j) ~ (Y-axis, X-axis)
class GridType():
    WALL = 1
    EMPTY = 0
class Solution:
    """
    @program grid: a chessboard include 0 and 1 (obstacles)
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        n, m = len(grid), len(grid[0])
        queue = collections.deque()
        # distance (value) from a point (key) to the original. 
        distance = {(0, 0): 0}

        while queue:
            x , y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                
                if not is_valid(next_x, next_y, grid, distance):
                    continue
                queue.append(next_x, next_y)
                distance[(next_x, next_y)] = distance[(x, y)] + 1

        if (n - 1, m - 1) in distance:
            return distance[(n - 1, m - 1)]

        return -1

    def is_valid(self, x, y, grid, distance):
        # still on chessboard
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        # is an obstacle?
        if grid[x][y] == GridType.WALL:
            return False
        # has visited?
        if (x, y) in distance:
            return False
        return True
             
```
## Complexity (?)

# DP: Rolling Array
## Simple DP
sol: https://www.lintcode.com/problem/630/solution/20146
```python
class Solution:
    # @param {boolean[][]} grid a chessboard included 0 and 1
    # @return {int} the shortest path
    def shortestPath2(self, grid):
        # Write your code here
        n = len(grid)
        if n == 0:
            return -1

        m = len(grid[0])
        if m == 0:
            return -1

        f = [ [sys.maxsize for j in range(m)] for _ in range(n)]

        f[0][0] = 0
        for j in range(m):
            for i in range(n):
                if not grid[i][j]:
                    if i >= 1 and j >= 2 and f[i - 1][j - 2] != sys.maxsize:
                        f[i][j] = min(f[i][j], f[i - 1][j - 2] + 1)
                    if i + 1 < n and j >= 2 and f[i + 1][j - 2] != sys.maxsize:
                        f[i][j] = min(f[i][j], f[i + 1][j - 2] + 1)
                    if i >= 2 and j >= 1 and f[i - 2][j - 1] != sys.maxsize:
                        f[i][j] = min(f[i][j], f[i - 2][j - 1] + 1)
                    if i + 2 < n and j >= 1 and f[i + 2][j - 1] != sys.maxsize:
                        f[i][j] = min(f[i][j], f[i + 2][j - 1] + 1)

        if f[n - 1][m - 1] == sys.maxsize:
            return -1

        return f[n - 1][m - 1]
```


## official version
```python
DIRECTIONS = [
    (-1, -2),
    (1, -2),
    (-2, -1),
    (2, -1),
]

class Solution:
    # @param {boolean[][]} grid a chessboard included 0 and 1
    # @return {int} the shortest path
    def shortestPath2(self, grid):
        if not grid or not grid[0]:
            return -1
        
        n, m = len(grid), len(grid[0])
        
        # state: dp[i][j % 3] 代表从 0,0 跳到 i,j 的最少步数
        dp = [[float('inf')] * 3 for _ in range(n)]

        # initialize: 0,0 是起点
        dp[0][0] = 0
        
        # function
        for j in range(1, m):
            for i in range(n):
                dp[i][j % 3] = float('inf')
                if grid[i][j]:
                    continue
                for delta_x, delta_y in DIRECTIONS:
                    x, y = i + delta_x, j + delta_y
                    if 0 <= x < n and 0 <= y < m:
                        dp[i][j % 3] = min(dp[i][j % 3], dp[x][y % 3] + 1)

        # answer
        if dp[n - 1][(m - 1) % 3] == float('inf'):
            return -1
        return dp[n - 1][(m - 1) % 3]
```

## Non-official version
循环数组的写法，用O(3n)的额外空间
（1）列遍历j必须放在外循环（当然无论是否循环数组都得这样...）
（2）为了使用循环数组，每一次更新时必须把当前step先初始化到maxsize，覆盖旧数值，避免错误
（3）为了不覆盖掉原点，j必须从1开始（当然第一列除了原点也不可能走到）
```python
class Solution:    
    def shortestPath2(self, grid):
        if not grid or not grid[0]:
            return -1
        
        n, m = len(grid), len(grid[0])
        if n == 0 or m == 0:
            return -1
            
        steps = [[sys.maxsize] * 3 for i in range(n)]
        steps[0][0] = 0
        
        for j in range(1, m):  # horizontal axis
            for i in range(n):  # vertical axis
                steps[i][j % 3] = sys.maxsize
                if grid[i][j] == 1:
                    continue
                
                for delta_i, delta_j in [(1, 2), (-1, 2), (2, 1), (-2, 1)]:
                    pre_i, pre_j = i - delta_i, j - delta_j
                        
                    if pre_i < 0 or pre_i >= n or pre_j < 0 or pre_j >= m or steps[pre_i][pre_j % 3] == sys.maxsize:
                        continue
                        
                    steps[i][j % 3] = min(steps[i][j % 3], steps[pre_i][pre_j % 3] + 1)

        if steps[n - 1][(m - 1) % 3] == sys.maxsize:
            return -1
            
        return steps[n - 1][(m - 1) % 3]
```

# Two-way BFS
sol: https://www.lintcode.com/problem/630/solution/19661
```python
FORWARD_DIRECTIONS = (
    (1, 2),
    (-1, 2),
    (2, 1),
    (-2, 1),
)

BACKWARD_DIRECTIONS = (
    (-1, -2),
    (1, -2),
    (-2, -1),
    (2, -1),
)

class Solution:
    def shortestPath2(self, grid):
        if not grid or not grid[0]:
            return -1
            
        n, m = len(grid), len(grid[0])
        if grid[n - 1][m - 1]:
            return -1
        if n * m == 1:
            return 0
            
        forward_queue = collections.deque([(0, 0)])
        forward_set = set([(0, 0)])
        backward_queue = collections.deque([(n - 1, m - 1)])
        backward_set = set([(n - 1, m - 1)])
        
        distance = 0
        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(forward_queue, FORWARD_DIRECTIONS, forward_set, backward_set, grid):
                return distance
                
            distance += 1
            if self.extend_queue(backward_queue, BACKWARD_DIRECTIONS, backward_set, forward_set, grid):
                return distance

        return -1
                
    def extend_queue(self, queue, directions, visited, opposite_visited, grid):
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                new_x, new_y = (x + dx, y + dy)
                if not self.is_valid(new_x, new_y, grid, visited):
                    continue
                if (new_x, new_y) in opposite_visited:
                    return True
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
                
        return False
        
    def is_valid(self, x, y, grid, visited):
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y]:
            return False
        if (x, y) in visited:
            return False
        return True
```

# BFS
sol: https://www.lintcode.com/problem/630/solution/17412

BFS解法，按步搜索， 如果终点值为1，直接返回-1，否则从左向右搜索，已经访问过的点
置为1.和DP解法相比，不需要额外空间。

## version 1

```python
def shortestPath2(self, grid):
        # write your code here
        if not grid or grid[-1][-1] == 1:
            return -1
            
        n = len(grid)
        m = len(grid[0])
 
        delta = [(1,2), (-1,2), (2,1), (-2,1)]
        queue = [(0,0)]
        step = 0
        while queue:
            size = len(queue)
            step += 1
            for i in range(size):
                x, y = queue.pop()
                for delta_x, delta_y in delta:
                    if x + delta_x == n - 1 and y + delta_y == m - 1:
                        return step
                    if n > x + delta_x >= 0 and m > y + delta_y >= 0 and grid[x + delta_x][y + delta_y] != 1:
                        grid[x + delta_x][y + delta_y] = 1
                        queue.insert(0, (x+delta_x, y+delta_y))
        return -1
```

## version 2 similar to official BFS solution
url: https://www.lintcode.com/problem/630/solution/19620
一个BFS的基本解法，十分的传统了。时间复杂度：O（N）N是matrix里点的个数。空间复杂度：O（N）
```python
DIRECTIONS = [[1, 2], [-1, 2], [2, 1], [-2, 1]]

def shortestPath2(self, grid):
    # write your code here
    queue = deque([(0, 0)])
    path = {(0, 0): 0}
    n, m = len(grid), len(grid[0])
    
    while queue:
        loc = queue.popleft()
        for i, j in self.DIRECTIONS:
            x, y = loc[0] + i, loc[1] + j
            if not self.is_valid(x, y, n, m, grid):
                continue
            queue.append((x, y))
            grid[x][y] = 1
            path[(x, y)] = path[loc] + 1

    return path.get((n - 1, m - 1), -1)

def is_valid(self, x, y, n, m, grid):
    if 0 <= x < n and 0 <= y < m:
        return not grid[x][y]
    return False
```
