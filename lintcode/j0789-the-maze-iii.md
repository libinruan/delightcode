![22-34]()
![22-39]()
![22-39]()
![22-40]()
![22-41]()
![22-44]()

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
            # 如果(new_x, new_y)距离始点的距离以量测过，并且新点的距离与路径没有比现有的更短。
            if (new_x, new_y) in distance and distance(new_x, new_y) <= (new_dist, new_path):
                continue

            queue.append((new_x, new_y))
            distance[(new_x, new_y)] = (new_dist, new_path)

def kick_ball(self, x, y, direction, maze, hole):
    # kick ball through direction from x, y and return the stopped position
    dx, dy = DIRECTION_HASH[direction]
    while (x, y) != hole and not self.is_wall(x, y, maze):
        x += dx
        y += dy

    if (x, y) == hole:
        return x, y
    
    return x - dx, y - dy

def is_wall(self, x, y, maze):
    if not (0 <= x < len(maze) and 0 <= y < len(maze[0])):
        return True
    return maze[x][y] == MazeGridType.WALL
```