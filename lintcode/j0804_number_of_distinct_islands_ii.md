# answe 1
# https://www.lintcode.com/problem/804/solution/29636
class Solution(object):
    def num_distinct_islands2(self, grid: List[List[int]]) -> int:
        seen = set()
        def explore(r, c):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                    grid[r][c] and (r, c) not in seen):
                seen.add((r, c))
                shape.add(complex(r, c))
                explore(r+1, c)
                explore(r-1, c)
                explore(r, c+1)
                explore(r, c-1)

        def canonical(shape):
            def translate(shape):
                w = complex(min(z.real for z in shape),
                            min(z.imag for z in shape))
                return sorted(str(z-w) for z in shape)

            ans = []
            for k in range(4):
                ans = max(ans, translate([z * (1j)**k for z in shape]))
                ans = max(ans,  translate([complex(z.imag, z.real) * (1j)**k
                                           for z in shape]))
            return tuple(ans)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                explore(r, c)
                if shape:
                    shapes.add(canonical(shape))

        return len(shapes)



# answer 2
# https://www.lintcode.com/problem/804/solution/19757

# 右边和下边加零，利用Python越界卷边的特性，避免繁琐的越界判定

# 先求出4个旋转，再每个x,y翻转4变8

# 直接改原图，无需另开visisted, seen数组

# 简练才能真懂，简练才能复现
class Solution:
    
    def numDistinctIslands2(self, grid):
        
        grid += [0] * len(grid[0]),
        for row in grid:
            row += 0,
        
        def canonical(shape):
            
            def encode(shape):
                x, y = shape[0]
                return "".join(str(i-x)+':'+str(j-y) for i, j in shape)
            
            shapes = [[(a*i, b*j) for i, j in shape] for a, b in ((1,1),(1,-1),(-1,1),(-1,-1))]
            shapes += [[(j, i) for i, j in shape] for shape in shapes]
            
            return min(encode(sorted(shape)) for shape in shapes)
            
        def dfs(i, j):
            if not grid[i][j]: return []
            
            grid[i][j] = 0
            shape = [(i, j)]
            for di, dj in ((0,-1),(0,1),(-1,0),(1,0)):
                shape += dfs(i+di, j+dj)
            return shape
        
        islands = set()
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == 1:
                    islands.add(canonical(dfs(i, j)))
        return len(islands)        



# answer 3
# https://www.lintcode.com/problem/804/solution/19957
from collections import deque

DIRECTIONS = [
    (0, 1), (1, 0), (-1, 0), (0, -1)
]

TRANS = [
    (1, 1), (-1, 1), (-1, -1), (1, -1)
]

class Solution:
    """
    @param grid: the 2D grid
    @return: the number of distinct islands
    """
    def numDistinctIslands2(self, grid):
        # write your code here
        
        if not grid or not grid[0]:
            
            return 0 
            
        m, n = len(grid), len(grid[0])
        islands = set()
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    
                    # Solution 1: DFS to find all islands
                    island = [] 
                    self.dfs(grid, i, j, island)
                    
                    # Solution 2: BFS to find all islands
                    # island = self.bfs(grid, i, j)
                    
                    islands.add(self.getUnique(island))
                    
        return len(islands)
        
    def dfs(self, grid, x, y, island):
        
        m, n = len(grid), len(grid[0])
        
        island.append((x, y))
        
        grid[x][y] = 0 
        
        for dx, dy in DIRECTIONS:
            
            nx, ny = x + dx, y + dy 
            
            if not self.is_valid(grid, nx, ny):
                
                continue 
            
            self.dfs(grid, nx, ny, island)
            
    def bfs(self, grid, x, y):
        
        queue = deque()
        seen = set()
        
        queue.append((x, y))
        seen.add((x, y))
        grid[x][y] = 0 
        
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                
                cx, cy = queue.popleft()
                
                for dx, dy in DIRECTIONS:
                    
                    nx, ny = cx + dx, cy + dy 
                    
                    if not self.is_valid(grid, nx, ny):
                        continue 
                    
                    if (nx, ny) in seen:
                        continue 
                    
                    queue.append((nx, ny))
                    seen.add((nx, ny))
                    grid[nx][ny] = 0
        
        return list(seen)
        
    def is_valid(self, grid, x, y):
        
        m, n = len(grid), len(grid[0])
        
        if x < 0 or x >= m or y < 0 or y >= n:
            return False 
            
        if grid[x][y] == 0:
            return False 
            
        return True 
    
    def getUnique(self, island):
        
        sameIslands = [] 
        
        for t0, t1 in TRANS:
            
            island1, island2 = [], [] 
            
            for x, y in island:
                
                island1.append((x * t0, y * t1))
                island2.append((y * t0, x * t1))
                
            sameIslands.append(self.getStr(island1))
            sameIslands.append(self.getStr(island2))
                
        sameIslands = sorted(sameIslands)
        
        return sameIslands[0]
        
    def getStr(self, island):
        
        island = sorted(island, key = lambda pos:(pos[0], pos[1]))
        dx, dy = island[0]
        string = ""
        
        for point in island:
            
            x, y = point[0] - dx, point[1] - dy 
            string = string + str(x) + " " + str(y) + " "
            
        return string