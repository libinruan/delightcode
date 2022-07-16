记忆化深搜版
其实本题就是算所以节点取根的最大耗费是多少。 深搜就完事了。 然后用记忆化搜索优化了一下
```python
class Solution:
    """
    @param father: the father of every node
    @param time: the time from father[i] to node i
    @return: time to flower tree
    """
    def timeToFlowerTree(self, father, time):
        max_time = 0
        memo = {}
        for i in range(1, len(father)):
            time_spent = self.dfs(father, time, memo, i)
            max_time = max(max_time, time_spent)
        return max_time
    
    def dfs(self, father, time, memo, root):
        if root == 0:
            return 0

        if root in memo:
            return memo[root]
        
        memo[root] = time[root] + self.dfs(father, time, memo, father[root])
        return memo[root]
```

BFS解法 I：先处理一下father，变成map，这样查找起来O（1）。 然后用BFS层层遍历，更新
全局最大值。
```python
from typing import (
    List,
)
from collections import deque
class Solution:
    """
    @param father: the father of every node
    @param time: the time from father[i] to node i
    @return: time to flower tree
    """
   
    def time_to_flower_tree(self, father: List[int], time: List[int]) -> int:
        # write your code here
        if not father: return -1

        fatherMap = {}
        for node in range(len(father)):
          key = father[node]
          if key not in fatherMap:
            fatherMap[key] = set()
          fatherMap.get(key).add(node)

        # bfs
        queue = deque()
        max_value = -1
        queue.append((0, 0))  # root

        while queue:
          node, value = queue.popleft()
          max_value = max(value, max_value)
          if node in fatherMap:
            # not leaf node
            children = fatherMap.get(node)
            for child in children:
              queue.append((child, value + time[child]))
        
        return max_value
```

BFS解法 II：
```python
from collections import deque
class Solution:
    """
    @param father: the father of every node
    @param time: the time from father[i] to node i
    @return: time to flower tree
    """
    def timeToFlowerTree(self, father, time):
        # write your code here
        child = {i: [] for i in range(len(father))}

        for node, parent in enumerate(father):
            if node != 0:
                child[parent].append(node)

        longest_path_length = -float('inf')
        queue = deque()
        queue.append((0, 0))

        while queue:
            node, length = queue.popleft()
            if len(child[node]) == 0:
                longest_path_length = max(longest_path_length, length)
            else:
                for next_node in child[node]:
                    queue.append((next_node, length + time[next_node]))

        return longest_path_length
```


本题可以用拓扑排序的解法来做，不过节点的入度（indegree）均为零，故可以省掉
get_indegrees步骤，其余跟经典拓扑排序做法一样。如果用经典拓扑排序来做，是这样的
（indegree部分其实可以去掉）

```python
class Solution:
    """
    @param father: the father of every node
    @param time: the time from father[i] to node i
    @return: time to flower tree
    """
    def timeToFlowerTree(self, father, time):
        # write your code here
        if not father or not father[0]:
            return 0

        graph = self.build_grap(father)
        indegrees = self.get_indegrees(graph)

        queue = collections.deque([(0, 0)])
        total_cost = 0
        while queue:
            cur_node, cur_time = queue.popleft()
            total_cost = max(total_cost, cur_time)
            
            # 精简后的拓扑排序
             for i in range(len(graph[cur_node])):
                node = graph[cur_node][i]
                queue.append((node, cur_time + time[node]))
            
            # 经典的拓扑排序实现方式 ；实际上因为入度都是1，
            # 没有必要用这种方式。纯演示作用。
            #for neighbor in graph[cur_node]:
            #   indegrees[neighbor] -= 1
            #   if indegrees[neighbor] == 0:
            #        queue.append((neighbor, cur_time + time[neighbor]))
                
        
        return total_cost
    
    def build_grap(self, father):
        n = len(father)
        graph = collections.defaultdict(list)
        for i in range(1, len(father)):
            graph[father[i]].append(i)
        
        return graph
    
    def get_indegrees(self, nodes):
        indegrees = collections.defaultdict(int)
        for node in nodes:
            for neighbor in nodes[node]:
                indegrees[neighbor] += 1

        return indegrees
```


