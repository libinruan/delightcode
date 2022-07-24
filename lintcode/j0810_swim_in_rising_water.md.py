# answer 1 深度优先遍历
# details: https://www.lintcode.com/problem/810/solution/57281
#   including complexity analysis. O(N^2logN) O(N^2)
from typing import (
    List,
)

class Solution:
    def swim_in_water(self, grid: List[List[int]]) -> int:
        N = len(grid)
        left, right = 0, N * N - 1
        while left < right:
            mid = (left + right) // 2
            visited = [[False] * N for _ in range(N)]
            if grid[0][0] <= mid and self.dfs(grid, 0, 0, visited, mid):
                # mid 可以，尝试 mid 小一点是不是也可以呢？下一轮搜索的区间[left, mid]
                right = mid
            else:
                left = mid + 1

        return left

    # 使用深度优先遍历得到从 (x, y) 开始向四个方向的所有小于等于 threshold 且与 (x, y) 连通的结点
    def dfs(self, grid, x, y, visited, threshold):
        visited[x][y] = True
        for diretion in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            dx = x + diretion[0]
            dy = y + diretion[1]

            if self.in_area(dx, dy, grid) and not visited[dx][dy] and grid[dx][dy] <= threshold:
                if dx == len(grid) - 1 and dy == len(grid) - 1:
                    return True

                if self.dfs(grid, dx, dy, visited, threshold):
                    return True
        
        return False

    def in_area(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid)



# answer 2
# 广度优先遍历
from typing import (
    List,
)

import collections
class Solution:
    def swim_in_water(self, grid: List[List[int]]) -> int:
        N = len(grid)
        left, right = 0, N * N - 1
        while left < right:
            mid = (left + right) // 2
            if grid[0][0] <= mid and self.bfs(grid, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def bfs(self, grid, threshold):
        queue = collections.deque()
        queue.append([0, 0])
        N = len(grid)
        visited = [[False] * N for _ in range(N)]
        visited[0][0] = True

        while queue:
            x, y = queue.popleft()
            for direction in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dx = x + direction[0]
                dy = y + direction[1]
                if self.in_area(dx, dy, grid) and not visited[dx][dy] and grid[dx][dy] <= threshold:
                    if dx == N - 1 and dy == N - 1:
                        return True
                    
                    queue.append([dx, dy])
                    visited[dx][dy] = True

        return False

    def in_area(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid)



# answer 3
# details: https://www.lintcode.com/problem/810/solution/57283
from typing import (
    List,
)

class UnionFind:
    def __init__(self, n):
        self.father = {}
        for i in range(n):
            self.father[i] = i

    def find(self, x):
        while x != self.father[x]:
            self.father[x] = self.father[self.father[x]]
            x = self.father[x]

        return x

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        if self.is_connected(x, y):
            return

        self.father[self.find(x)] = self.find(y)

class Solution:
    def swim_in_water(self, grid: List[List[int]]) -> int:
        # Write your code here
        N = len(grid)
        length = N * N
        index = [0] * length
        for i in range(N):
            for j in range(N):
                index[grid[i][j]] = i * N + j

        union_find = UnionFind(length)

        for i in range(length):
            x = index[i] // N
            y = index[i] % N
            for direction in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dx = x + direction[0]
                dy = y + direction[1]
                if (self.in_area(dx, dy, grid) and grid[dx][dy] <= i):
                    union_find.union(index[i], dx * N + dy)

                if union_find.is_connected(0, length - 1):
                    return i

        return -1

    def in_area(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid)



# answer 4
# https://www.lintcode.com/problem/810/solution/30245
import heapq
class Solution:
    """
    @param grid: the grid
    @return: the least time you can reach the bottom right square
    """
    def swimInWater(self, grid):
        N, pq, seen, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        while True:
            T, x, y = heapq.heappop(pq)
            res = max(res, T)
            if x == y == N - 1:
                return res
            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= i < N and 0 <= j < N and (i, j) not in seen:
                    seen.add((i, j))
                    heapq.heappush(pq, (grid[i][j], i, j))        