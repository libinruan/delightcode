原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/81126995

描述
给一个 01 矩阵，求不同的岛屿的个数。
0 代表海，1 代表岛，如果两个 1 相邻，那么这两个 1 属于同一个岛。我们只考虑上下左右为相邻。


我们对每个有“1"的位置进行dfs，把和它四联通的位置全部变成“0”，这样就能把一个点推广到一个岛。
所以，我们总的进行了dfs的次数，就是总过有多少个岛的数目。
注意理解dfs函数的意义：已知当前是1，把它周围相邻的所有1全部转成0.

# VERSION 1. DFS

[MTV sister DFS](https://www.youtube.com/watch?v=Ft0AmONMYyM)

```python
# 2020-4-13; 2020-5-16
""" cartesian (x, y) = python (j, i)
     up
     (-1, 0)    
left       right
(0, -1)    (0, 1)
     down
     (1, 0)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
# 1 TREAT EVERY CELL AS THE ROOT AND START FROM THE [0][0] ONE.
        if not grid or len(grid) == 0 or len(grid[0]) == 0: return 0
        m, n = map(len, [grid, grid[0]])
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
#   WE ONLY COUNT VALID ROOTS THAT LEADS A COMPLETE EXPLORATION OF AN ISLAND                
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(m, n, grid, i, j)
# 3 END OF THE PROGRAM
        return res
    
    def dfs(self, m, n, grid, i, j):
        diList, djList = [-1, 0, 1, 0], [0, 1, 0, -1]
        grid[i][j] = '0' # don't forget to keep the program from going back.
        # Method 1. Use double lists and a single for-loop.
        for di, dj in zip(diList, djList):
# 2 WE ONLY EXTEND OUR EXPLORATION ON VALID LAND CELLS            
            if 0 <= i + di < m and 0 <= j + dj < n and grid[i + di][j + dj] == '1':
                self.dfs(m, n, grid, i + di, j + dj)
```            
                    
```python
# 36% Lipin 2020.1.14
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for r in range(len(grid)): # (r X c) DFS trees. Not just one.
            for c in range(len(grid[0])):
                if grid[r][c] == "1": # 
                    self.dfs(grid, r, c) # <---DFS template
                    res += 1
        return res

    # Method A. grid is an augument of dfs()    
    def dfs(self, grid, i, j):
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        grid[i][j] = "0" 
        # Method 2. Use a list of 2-tuple and a single for-loop.
        for dir in dirs:
            nr, nc = i + dir[0], j + dir[1]
            if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]):
                if grid[nr][nc] == "1":
                    self.dfs(grid, nr, nc)
```


```python
# 36% Lipin 2020.1.14
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        res = 0
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)] # Python(i, j) left, right, up, down
        m, n = len(grid), len(grid[0])
        
        # Method B. grid is NOT an augument of dfs()
        def dfs(i, j):
            if grid[i][j] == "0": return
            grid[i][j] = "0"
            for d in dirs:
                if 0 <= i + d[0] < m and 0 <= j + d[1] < n:
                    dfs(i + d[0], j + d[1])
                    
        # Method 3. use double for-loops to explore neighboring cells.
        for i in range(m):
            for j in range(n):
                    if grid[i][j] == "0":
                        continue    
                    dfs(i, j)    
                    res += 1
        return res
```
# Comparison: DFS vs BFS
```python
class Solution:
    def numIslands_DFS(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        res = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Python(i, j) up, down, left, right
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if grid[i][j] == '0': return
            grid[i][j] = '0'  # [0] DFS 归零操作在此发生。Preorder traversal。
            for d in dirs:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n:  # [2] DFS此处不判断等不等于一。下面也不做归零。
                    dfs(ni, nj)  # [3] DFS move onto child node.

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)  # [4]
                    res += 1
        
        return res

    def numIslands_BFS(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        res = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Python(i, j) up, down, left, right
        m, n = len(grid), len(grid[0])
        que = []  # [5] BFS queue

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'  # [6]
                    res += 1

                    que.append((i, j))  # [7] BFS add into queue
                    while que:
                        r, c = que.pop()  # [8] BFS be sure to make it different from (i, j)
                        for d in dirs:
                            nr, nc = r + d[0], c + d[1]
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                que.append((nr, nc))
        return res
```

# VERSION 2. BFS

这个题同样可以使用BFS解决。当遇到一个小岛的时候，做个BFS搜索，把它周围的小岛全部转成0即可。速度比DFS稍微慢了一点点。

在写dfs的时候可以把代码包装成一个函数，需要注意的是，由于BFS会把周围的1全部改成0，所以在出队列 (queue) 的时候，做一个判断，如果当前围着孩子已经被改了，那么就不用下面的搜索了。


# JZ 并查集 (to be continued)
In-degree and out-degree ([page](https://www.log2base2.com/data-structures/graph/degree-of-each-vertex-in-the-graph.html))

The vertex that can serve at an initial node has in-degree zero.

If the graph has a cycle, a topological orde cannot exist.  

DFS (BFS) is typically implemented with LIFO (FIFO) (a stack (queue) if you will) - last (first) in first out.
```python
from typing import (
    List,
)


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    self.parent[i * n + j] = i * n + j
                    self.count += 1
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1
    
    def getCount(self):
        return self.count

class Solution:
    def num_islands(self, grid: List[List[bool]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        uf = UnionFind(grid)
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]:
                    grid[r][c] = False
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y]:
                            uf.union(r * nc + c, x * nc + y)
        
        return uf.getCount()
```
![compliexity](https://i.postimg.cc/ydz6H0yh/2022-08-27-at-14-55-48.png)
# JZ BFS
```python
from typing import (
    List,
)

class Solution:
    def num_islands(self, grid: List[List[bool]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]:
                    num_islands += 1
                    grid[r][c] = False
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y]:
                                neighbors.append((x, y))
                                grid[x][y] = False
        
        return num_islands
```
![](https://i.postimg.cc/26zpGGxt/2022-08-27-at-14-58-12.png)

# JZ DFS
```python
from typing import (
    List,
)

class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = False
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y]:
                self.dfs(grid, x, y)

    def num_islands(self, grid: List[List[bool]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]:
                    num_islands += 1
                    self.dfs(grid, r, c)
        
        return num_islands
```
![](https://i.postimg.cc/L83F1GtP/2022-08-27-at-14-59-37.png)