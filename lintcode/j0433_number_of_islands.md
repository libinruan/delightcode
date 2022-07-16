
原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/81126995

我们对每个有“1"的位置进行dfs，把和它四联通的位置全部变成“0”，这样就能把一个点推广到一个岛。

所以，我们总的进行了dfs的次数，就是总过有多少个岛的数目。

注意理解dfs函数的意义：已知当前是1，把它周围相邻的所有1全部转成0.

# VERSION 1. DFS

[MTV sister DFS](https://www.youtube.com/watch?v=Ft0AmONMYyM)

```python
# 2020-4-13; 2020-5-16
"""
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
        
    def dfs(self, grid, i, j):
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        grid[i][j] = "0" 
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
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)] # left, right, up, down
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if grid[i][j] == "0": return
            grid[i][j] = "0"
            for d in dirs:
                if 0 <= i + d[0] < m and 0 <= j + d[1] < n:
                    dfs(i + d[0], j + d[1])
                    
        for i in range(m):
            for j in range(n):
                    if grid[i][j] == "0":
                        continue    
                    dfs(i, j)    
                    res += 1
        return res
```

# VERSION 2. BFS

这个题同样可以使用BFS解决。当遇到一个小岛的时候，做个BFS搜索，把它周围的小岛全部转成0即可。速度比DFS稍微慢了一点点。

在写dfs的时候可以把代码包装成一个函数，需要注意的是，由于BFS会把周围的1全部改成0，所以在出队列的时候，做一个判断，如果当前围着孩子已经被改了，那么就不用下面的搜索了。

        UP
        (-1,0)
    LEFT   RIGTH
    (0,-1) (0,1)
        DOWN
        (1,0)

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0: return 0
        m, n = map(len, [grid, grid[0]])
        res = 0
        que = []
        diList, djList = [-1, 0, 1, 0], [0, 1, 0, -1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    res += 1
# 1 THE START OF BFS                
                    que.append((i, j))
                    while que:
                        x, y = que.pop()
                        for dx, dy in zip(diList, djList):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                que.append((nx,ny))
# 2 END OF THE PROGRAM
        return res
                            
```
