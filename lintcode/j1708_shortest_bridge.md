搜索
分析

我们使用的方法非常直接：首先找到这两座岛，随后选择一座，将它不断向外延伸一圈，直到到达了另一座岛。

在寻找这两座岛时，我们使用深度优先搜索。在向外延伸时，我们使用广度优先搜索。

算法

我们通过对数组 A 中的 1 进行深度优先搜索，可以得到两座岛的位置集合，分别为
source 和 target。随后我们从 source 中的所有位置开始进行广度优先搜索，当它们到达
了 target 中的任意一个位置时，搜索的层数就是答案。

```python
from typing import (
    List,
)
class Solution:
    def shortest_bridge(self, a: List[List[int]]) -> int:
        R, C = len(a), len(a[0])

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():
            done = set()
            components = []
            for r, row in enumerate(a):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        # Start dfs
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if a[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        done |= seen
                        components.append(seen)
            return components

        source, target = get_components()
        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target: return d-1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d+1))
                    done.add(nei)
```           

BFS两遍不改变input版本
```python
DIRECTIONS = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0),
]

class Solution:
    def ShortestBridge(self, A):
        first_land = self.find_first_land(A)
        first_island_points = self.find_first_island(A, first_land[0], first_land[1])

        step = 0
        queue = collections.deque(first_island_points)
        visited = set(first_island_points)
        while queue:
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                if step != 0 and A[x][y] == 1:
                    return step - 1
                for delta_x, delta_y in DIRECTIONS:
                    new_x = x + delta_x
                    new_y = y + delta_y
                    if new_x < 0 or new_x >= len(A) or new_y < 0 or new_y >= len(A[0]):
                        continue
                
                    if (new_x, new_y) in visited:
                        continue
                    
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
            step += 1
        return step        
    
    def find_first_land(self, A):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    return (i, j)
        
    def find_first_island(self, A, start_x, start_y):
        queue = collections.deque([(start_x, start_y)])
        visited = set([(start_x, start_y)])
        results = []
        while queue:
            x, y = queue.popleft()
            if A[x][y]:
                results.append((x, y))
            for delta_x, delta_y in DIRECTIONS:
                new_x = x + delta_x
                new_y = y + delta_y
                if new_x < 0 or new_x >= len(A) or new_y < 0 or new_y >= len(A[0]):
                    continue
            
                if (new_x, new_y) in visited:
                    continue
                
                if A[new_x][new_y] != 1:
                    continue
                
                results.append((new_x, new_y))
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
        return results
            
```