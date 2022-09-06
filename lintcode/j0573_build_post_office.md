![](https://i.postimg.cc/dt6Bqj06/2022-09-05-at-20-31-59.png)

![](https://i.postimg.cc/NM2Sq9Lv/2022-09-01-at-23-48-32.png)

![](https://i.postimg.cc/q7W6816V/2022-09-01-at-22-37-42.png)
Assume the number of positions (or space) available for post office to locate is SPACE. -> O(SPACE).
Given a location of post office, there are (n*m) points on the board to calcualte their distances to the post office. -> O(n*m). So the total time complexity is O(SPACE*n*m). The worst case of time complexity is the case where the post office is allowed to locate in any postion on the board, which offer (n*m) choices. So the time complexity of the worst case is O(n^2*m^2).

>  (x, y) = (列, 行) m: 为列数。n: 为行数。

```python
class GridType:  # 定义一个class去储存常数。
    EMPTY = 0
    HOUSE = 1
    WALL = 1

class Solution:
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return 0 
        n, m = len(grid), len(grid[0])
        min_dist = float('inf')

        # loop over all the cells looking for empty space for the post office to reside.
        for i in range(n):
            for j in range(m):
                if grid[i][j] == GridType.EMPTY  # 是空地才能作为新邮局地址。
                    # bfs is used for finding the shortest path.
                    distance = self.bfs(gird, i, j)  # (i, j) 到所有其他点的最短距离。
                    # update the global vairable for finding the minimum distance sum in the end. 记录的是全局的最小值
                    min_dist = min(min_dist, self.get_distance_sum(distance, grid))
        
        return min_dist if min_dist != float('inf') else -1

    def bfs(self, grid, i, j):
        # distance from the starting point (i, j)
        distance = {(i, j): 0}  # the disntace from (i, j) to (i, j) is zero. 初始：(i, j) 到自己的距离为零。
        queue = collections.deque([(i, j)])

        while queue:
            x, y = queue.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                # generate the coordinate of neighbor
                adj_x, adj_y = x + dx, y + dy 
                # check if it falls in valid cells, not beyond the boundary
                if not self.is_valid(adj_x, adj_y, grid):  # (adj_x, adj_y) 必须是没有越界，且不是房子就是空地。
                    continue
                if (adj_x, adj_y) in distance: # (adj_x, adj_y) 到 (i, j) 的距离是否已知。LP: 为何第一次走到的距离是所求?
                    continue
                distance[(adj_x, adj_y)] = distance[(x, y)] + 1
                # 房子的点无法成为道路，所以没有继续拓展的可能。只有空地才行。
                if grid[adj_x][adj_y] != GridType.HOUSE: 
                    queue.append((adj_x, adj_y))
        return distance

    def get_distance_sum(self, distance, grid):
        distance_sum = 0
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val == GridType.HOUSE:
                    if (x, y) not in distance: # 若此房子的距历根本没计算过，就代表这房子根本走不到。
                        return float('inf')
                    distance_sum += distance[(x, y)]
        return distance_sum
    
    def is_valid(self, x, y, grid):  # 有无越界的判断。
        n, m = len(grid), len(grid[0])
        # falls outside the boundary
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return grid[x][y] in [GridType.EMPTY, GridType.HOUSE]  # we cannot walk through wall.
```

# Follow up question: what if the number of space is much larger than the number of houses?
How should we optimize with this information?
![9-5-at-21-14]()
![at-21-17 ]()
```python
def shortestDistance(self, grid):
    if not grid:
        return 0
    n, m = len(grid), len(grid[0])
    distance_sum = {}  # distance from a particular point to all the houses.
    reachable_count = {}  # track how many houses can reach a particular point on the map.

    houses = 0

    # This for loop costs O(Houses)
    for i in range(n):
        for j in range(m):
            # This method focuses on hourses only.
            if grid[i][j] == GridType.HOUSE:
                # through double for-loops, we update distance_sum and reachable_count.
                self.bfs(grid, i, j, distance_sum, reachable_count)  # Each bfs execution costs O(n * m).  
                house += 1
    # therefore, the overall time complexity is O(house * n * m).
            
    min_dist = float('inf')
    for i in range(n):  # loop over every postiion.
        for j in range(m):
            if (i, j) not in reachable_count:  # if (i,j) is not a reachable space from any houses.
                continue
            if reachable_count[(i, j)] != houses:  # if the reachable space can only be reached by part of the houses.
                continue
            min_dist = min(min_dist, distance_sum[(i, j)])  # if both the conditions above are satisfied, update the global variable, distance_sum, i.e., the total distance of (i,j) to every house.
    return min_dist if min_dist != float('inf') else -1

def bfs(self, grid, i, j, distance_sum, reachable_count):
    distance = {(i, j): 0}  # the distance from the current position (i, j) to itself is zero.
    queue = collections.deque([i, j])

    while queue:
        x, y = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            adj_x, adj_y = x + dx, y + dy
            if not self.is_valid(adj_x, adj_y, grid): # 必须不能越界，且必须是空地。
                continue
            if (adj_x, adj_y) not in distance:  # the distance from (i, j) to (adj_x, adj_y) has not been calculated.
                queue.append((adj_x, adj_y))
                distance[(adj_x, adj_y)] = distance[(x, y)] + 1
                # add up into distance_sum & reachable_count
                if (adj_x, adj_y) not in reachable_count:
                    distance_sum([adj_x, adj_y)] = 0
                    reachable_count[(adj_x, adj_y)] = 0
                distance_sum[(adj_x, adj_y)] += distance[(adj_x, adj_y)]
                reachable_count[(adj_x, adj_y)] += 1

def is_valid(self, x, y, grid):
    n, m = len(grid), len(grid[0])
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return grid[x][y] == GridType.EMPTY
```

```