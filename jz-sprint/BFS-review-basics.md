# Basic (1)
```python
queue = collections.deque()
visited = set()

queue.append(0)
visited.add(0)

while queue:
    now = queue.popleft()
    for next_point in self.find_next(now):
        if not self.is_valid(now):
            continue
        queue.append(next_point)
        visited.add(next_point)
```
```java
Queue<Integer> queue = new LinkedList<>();
HashSet<Integer> visited = new HashSet<>();

queue.offer(0);
visited.add(0);

while (!queue.isEmpty()) {
    int now = queue.poll();
    for (int next_point : findNext(now)) {
        if !isValid(next_point) {
            continue;
        }
        queue.offer(next_point);
        visited.add(next_point);
    }
}
```
# Stratification (2)
```python
queue = collections.deque()
visited = set()

queue.append(0)
visited.add(0)

while queue:
    for i in range(len(queue)):  # Added!
        now = queue.popleft()    # Added!
        for next_point in self.find_next(now):
            if not self.is_valid(now):
                continue
            queue.append(next_point)
            visited.add(next_point)
```
```java
Queue<Integer> queue = new LinkedList<>();
HashSet<Integer> visited = new HashSet<>();

queue.offer(0);
visited.add(0);

while (!queue.isEmpty()) {
    int queueSize = queue.size()
    for (int i = 0; i < queueSize; i++) {
        int now = queue.poll();
        for (int next_point : findNext(now)) {
            if (!isValid(next_point)) {
                continue;
            }
            queue.offer(next_point);
            visited.add(next_point);
        }
    }
}
```
# Dictionary to measure distance (3)
```python
queue = collections.deque()
distance = {}

queue.append(0)
distance[0] = 0

while queue:
    now = queue.popleft()
    for next_point in self.find_next(now):
        if not self.is_valid(now):
            continue
        queue.append(next_point)
        distance[next_point] = distance[now] + 1
```
Difference between Java `pop` and `poll` [link](https://www.baeldung.com/java-linkedlist#:~:text=The%20difference%20between%20poll(),list%2C%20whereas%20poll%20returns%20null.)
```java
Queue<Integer> queue = new LinkedList<>();
HashMapt<Integer, Integer> distance = new HashMap<>();

queue.offer(0);
distance.put(0, 0);

while (!queue.isEmpty()) {
    int now = queue.poll();
    for (int next_point : findNext(now)) {
        continue;
    }
    queue.offer(next_point);
    visited.put(next_point, distance.get(now) + 1)
}
```

# How to do 2D BFS with Python
Answer: Use Tuple. For Java, traslate (x, y) to x * m + y

# Questions
[JZ 433. 岛屿的个数](https://github.com/libinruan/delightcode/blob/main/lintcode/j0433_number_of_islands.md)