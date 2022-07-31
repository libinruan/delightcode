# BFS
https://www.lintcode.com/problem/431/solution/19874
```python
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors []

from collections import deque
class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        result = []
        visited = set()
        
        for node in nodes:
            if node not in visited:
                subgraph = []
                self.bfs(node, visited, subgraph)
                result.append(sorted(subgraph))
        return result


    def bfs(self, node, visited, subgraph):
        queue = deque()
        queue.append(node)
        visited.add(node)
        
        while queue:
            node = queue.popleft()
            subgraph.append(node.label)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
```

# DFS, BFS*
https://www.lintcode.com/problem/431/solution/18067
```python
class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        self.visited = {}
        
        for node in nodes:
            self.visited[node] = False
        
        res = []
        for node in nodes:
            if not self.visited[node]:
                tmp = []
                self.bfs(tmp, node)
                res.append(sorted(tmp))
        return res
    
    def dfs(self, tmp, node):
        self.visited[node] = True
        tmp.append(node.label)
        for neighbor in node.neighbors:
            if not self.visited[neighbor]:
                self.dfs(tmp, neighbor)

    def bfs(self, tmp, node):
        q = collections.deque([node])
        tmp.append(node.label)
        self.visited[node] = True
        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if not self.visited[neighbor]:
                    q.append(neighbor)
                    tmp.append(neighbor.label)
                    self.visited[neighbor] = True
```

# 无向图连通块, 可以使用BFS或者并查集union find求解 (Official)

```python
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def dfs(self, x, tmp):
        self.v[x.label] = True
        tmp.append(x.label)
        for node in x.neighbors:
            if not self.v[node.label]:
                self.dfs(node, tmp)
            
    def connectedSet(self, nodes):
        # Write your code here
        self.v = {}
        for node in nodes:
            self.v[node.label] = False

        ret = []
        for node in nodes:
            if not self.v[node.label]:
                tmp = []
                self.dfs(node, tmp)
                ret.append(sorted(tmp))
        return ret
            
```