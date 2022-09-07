![22-34](https://i.postimg.cc/T2kN8NjR/2022-09-05-at-22-34-53.png)
![22-39](https://i.postimg.cc/52RdgNyM/2022-09-05-at-22-39-00.png)
![22-39](https://i.postimg.cc/3rthSHt9/2022-09-05-at-22-39-24.png)
![22-40](https://i.postimg.cc/4NdT9FbM/2022-09-05-at-22-40-39.png)



# Method 1
```python
DIRECTION_HASH = {
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1),
    'u': (-1, 0),
}

class MazeGridType:
    SPACE = 0
    WALL = 1

def findShortestWay(self, maze, ball, hole):
    # corner case check
    if not ball or not hole:
        return 'impossible'
    if not maze or not maze[0]:
        return 'impossible'
    hole = (hole[0], hole[1])

    # (distance, x, y, path)
    queue = collections.deque([(ball[0], ball[1])])  # queue stores the coornidates.
    distance = {(ball[0], ball[1]): (0, '')}  # the starting point's distance is zero and the operation order is empty ('').

    while queue:
        x, y = queue.popleft()
        dist, path = distance[(x, y)]  #  

        for direction in DIRECTION_HASH:
            if path and path[-1] == direction:  # moving in the same direction again is not allowed.
                continue
            
            new_x, new_y = self.kick_ball(x, y, direction, maze, hole)  # 一路到底移动的写法
            new_dist = dist + abs(new_x - x) + abs(new_y - y)  # Manhattan distance
            new_path = path + direction  # log the attempted direction
            # 如果(new_x, new_y)距离始点的距离以量测过，并且新点的距离没有更短。我们就跳过。
            # 此外，Python可以直接对二元组比对大小（见下一行）。
            if (new_x, new_y) in distance and distance(new_x, new_y) <= (new_dist, new_path):
                continue

            queue.append((new_x, new_y))  # 加到对列
            distance[(new_x, new_y)] = (new_dist, new_path)  # 并且更新距离。

    if hole in distance:          # LP: do we need to add these lines as in Method 2?    
        return distance[hole][1]  # LP: do we need to add these lines as in Method 2?          
                                  # LP: do we need to add these lines as in Method 2?      
    return 'impossible'           # LP: do we need to add these lines as in Method 2?

def kick_ball(self, x, y, direction, maze, hole):
    # kick ball through direction from x, y and return the stopped position
    dx, dy = DIRECTION_HASH[direction]
    while (x, y) != hole and not self.is_wall(x, y, maze):
        x += dx
        y += dy

    if (x, y) == hole:
        return x, y
    
    return x - dx, y - dy  # Our movement is stopped at an obstcle, so we need to move one step back to be relocated to an non-obstacle point.

def is_wall(self, x, y, maze):
    if not (0 <= x < len(maze) and 0 <= y < len(maze[0])):
        return True
    return maze[x][y] == MazeGridType.WALL
```

# Method 2 replace queue with heapq :: SPFA
```python
def findShortestWay(self, maze, ball, hoe):
    from heapq import heappush, heappop

    if not ball or not hole:
        return 'impossible'
    if not maze or not maze[0]:
        return 'impossible'
    
    hole = (hole[0], hole[1])  # 当数组为空或是只有一个元素，heapify这个步骤可以省略。
    queue = [(0, '', ball[0], ball[1])]
    distance = {(ball[0], ball[1]): (0, '')}

    while queue:
        dist, path, x, y = heappop(queue)
        for direction in DIRECTION_HASH:
            if path and path[-1] == direction:
                continue

            new_x, new_y = self.kick_ball(x, y, direction, maze, hole)
            new_dist = dist + abs(new_x - x) + abs(new_y - y)
            new_path = path + direction
            if (new_x, new_y) in distance and distance[(new_x, new_y)] <= (new_dist, new_path):
                continue

            heappush(queue, (new_dist, new_path, new_x, new_y))
            distance[(new_x, new_y)] = (new_dist, new_path)

    if hole in distance:
        return distance[hole][1]
    
    return 'impossible'

def kick_ball(...):
    ...

def is_wall(...):
    ...
```