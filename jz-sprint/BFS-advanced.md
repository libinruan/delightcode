Application of BFS:
1. Connected Component
    1. 通过一个点找到图中连通的所有点
    2. 非递归方式找到所有方案（见第20章）
2. Level Order Traversal
    1. 图的层次遍历
    2. Simple Graph Shortest Path
3. Topological Sorting
    1. Arbitrary topological sorting.
    2. Existence of topological sorting.
    3. lexicographical smallest topological sorting.
    4. Uniqueness of topological sorting.

```java
Queue<Node> queue = new ArrayDeque<>();  //LinkedList works as well. Slower due to 非连续数据结构 
HashMap<Node, Integer> distance = new HashMap<>();

queue.offer(node); 
distance.put(node, 0);

while (!queue.isEmpty()) {
    Node node = queue.poll();
    for (Node neighbor : node.getNeighbors()) {
        if (distance.containsKey(neighbor)) {
            continue;
        }
        distance.put(neighbor, distance.get(node) + 1);
        queue.offer(neighbor);
    }
}
```
Extension: Implement queue 对列 by circular array 循环数组. 


```python
# step 1. Initializaion
# Put initial nodes into deque. If multple root nodes, put them all in the deque.
# Mark the distance to the root node as zero, register the distance in dict.
queue = collections.deque([node])
distance = {node : 0}

# step 2. Repeatively walk through the deque
# Use 'while' to do repetition; pop out an object per round.
while queue:
    node = queue.popleft()
    # step 3. expand neighboring nodes
    # add valid neighboring nodes into queue and into distance dict
    for neighbor in node.get_neighbors():
        if neighbor in distance:
            continue
        distance[neighbor] = distance[node] + 1
        queue.append(neighbor)
```

[](