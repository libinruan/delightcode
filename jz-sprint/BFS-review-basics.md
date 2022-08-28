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

# Topological Sorting
[webpage](https://www.jiuzhang.com/problem/topological-sorting/#tag-lang-python)

You can do topological sorting using BFS. Actually I remembered once my teacher told me that if the problem can be solved by BFS, never choose to solve it by DFS. Because the logic for BFS is simpler than DFS, most of the time you will always want a straightforward solution to a problem.

[source](https://stackoverflow.com/questions/25229624/using-bfs-for-topological-sort#answer-44986459)
You need to start with nodes of which the indegree is 0, meaning no other nodes direct to them. Be sure to add these nodes to your result first.You can use a HashMap to map every node with its indegree, and a queue which is very commonly seen in BFS to assist your traversal. When you poll a node from the queue, the indegree of its neighbors need to be decreased by 1, this is like delete the node from the graph and delete the edge between the node and its neighbors. Every time you come across nodes with 0 indegree, offer them to the queue for checking their neighbors later and add them to the result.

![](https://i.postimg.cc/D02hYWWy/2022-08-28-at-01-56-44.png)
![](https://i.postimg.cc/5NmTnpBL/2022-08-28-at-10-22-50.png)

```python
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        topu = []
        # in记录节点的入度
        in_degree = {}
        que = collections.deque()
        for e in graph:
            for i in e.neighbors:
                # 记录每个点的入度
                if i in in_degree:
                    in_degree[i] += 1 
                else:
                    in_degree[i] = 1
        for e in graph:
            #  入度为0的点作为起始点
            if e not in in_degree:
                que.append(e)
        while len(que) > 0:
            now = que.popleft()
            topu.append(now)
            for e in now.neighbors:
                in_degree[e] -= 1 
                if in_degree[e] == 0:
                    que.append(e)
        return topu;
```

```java
/**
 * Definition for Directed graph.
 * struct DirectedGraphNode {
 *     int label;
 *     vector<DirectedGraphNode *> neighbors;
 *     DirectedGraphNode(int x) : label(x) {};
 * };
 */

public class Solution {
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        ArrayList<DirectedGraphNode> res = new ArrayList();
        Map<DirectedGraphNode, Integer> indegree = new HashMap();
        for(DirectedGraphNode node : graph){
            for(DirectedGraphNode nei : node.neighbors) {
                indegree.putIfAbsent(node, 0); // note: need to add node itself to start
                indegree.put(nei, indegree.getOrDefault(nei, 0) + 1);
            }
        }

        Queue<DirectedGraphNode> q = new LinkedList();
        for(DirectedGraphNode key : indegree.keySet()) {
            if(indegree.get(key) == 0) q.add(key);
        }

        while(q.size() > 0) {
            DirectedGraphNode node = q.poll();
            res.add(node);
            for(DirectedGraphNode nei : node.neighbors) {
                indegree.put(nei, indegree.get(nei) - 1);
                if(indegree.get(nei) == 0) q.add(nei);
            }
        }
        return res;
    }
}
```
