广度优先遍历
source: https://www.lintcode.com/problem/137/solution/56841?fromId=164&_from=collection
```python
from lintcode import (
    UndirectedGraphNode,
)
from collections import deque
class Solution:
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        if not node:
            return node
        visited = {}
        # 将题目给定的节点添加到队列
        queue = deque([node])
        # 克隆第一个节点并存储到哈希表中
        visited[node] = UndirectedGraphNode(node.label)
        # 广度优先搜索
        while queue:
            # 取出队列的头节点
            n = queue.popleft()
            # 遍历该节点的邻居
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # 如果没有被访问过，就克隆并存储在哈希表中
                    visited[neighbor] = UndirectedGraphNode(neighbor.label)
                    # 将邻居节点加入队列中
                    queue.append(neighbor)
                # 更新当前节点的邻居列表
                visited[n].neighbors.append(visited[neighbor])

        return visited[node]
```

深度优先搜索
solution: https://www.lintcode.com/problem/137/solution/56836?fromId=164&_from=collection
```python
from lintcode import (
    UndirectedGraphNode,
)

class Solution:
    def __init__(self):
        self.visited = {}

    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        if not node:
            return node
        # 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
        if node in self.visited:
            return self.visited[node]
        # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
        clone_node = UndirectedGraphNode(node.label)
        # 哈希表存储
        self.visited[node] = clone_node
        # 遍历该节点的邻居并更新克隆节点的邻居列表
        if node.neighbors:
            clone_node.neighbors = [self.clone_graph(n) for n in node.neighbors]
        return clone_node
```