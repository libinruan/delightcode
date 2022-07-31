# DFS version 1
这里贡献一个答案，注意不要 self.visited.remove(value) 因为这里不是求路径，只是判断是否存在即可。还有说一下九章的答案代码实在太丑了。。。。。

Use DFS to find a feasible solution;
Add visited to keep track of previous node to avoid inifite loop

```python
class Solution:
    def __init__(self):
        self.visited = set()
    """
    @param: graph: A list of Directed graph node
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """

    def hasRoute(self, graph, s, t):
        if s == t:
            return True

        for next_node in s.neighbors:
            if next_node in self.visited:
                continue

            self.visited.add(s)

            if self.hasRoute(graph, next_node, t):
                return True
        return False
```

# DFS version 2

Use DFS to find a feasible solution;
Add visited to keep track of previous node to avoid inifite loop


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
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """
    def hasRoute(self, graph, s, t):
        # write your code here
        visited = set()
        return self.dfs(graph, s, t, s, visited)
        
    def dfs(self, graph, s, t, cur, visited):
        if cur in visited:
            return False
        if cur == t:
            return True
        visited.add(cur)
        for nei in graph[cur.label].neighbors:
            if self.dfs(graph, s, t, nei, visited):
                return True
        return False
```

# BFS version 1
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
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """

    def hasRoute(self, graph, s, t):
        # write your code here
        if s == t: 
          return True 
        
        queue = collections.deque([s])
        visited = set([s])

        while queue: 
          node = queue.popleft()
          for neighbor in node.neighbors: 
            if neighbor in visited: 
              continue 
            visited.add(neighbor) 
            queue.append(neighbor) 
        
        return t in visited
```


## BFS version 2
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
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """

    def hasRoute(self, graph, s, t):
        queue = collections.deque([s])
        visited = set()
        visited.add(s)
        
        while queue:
            node = queue.popleft()
            if node == t:
                return True
            for neighbor in node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return False
```
