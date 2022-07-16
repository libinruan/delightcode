SPFA (shortest path fast algorithm)
沿用暴力的思路，先设置起点到每个节点的距离为最大值
初始化距离起点的位置为0，把起点装入队列
从队列拿出节点，然后根据构图先遍历距离为0的节点
再遍历距离为1的节点，如果发现距离比之前的更小，重新装入队列
```python
# version 1
class Solution:
    def modernLudo(self, length, connections):
        from collections import deque
        graph = self.build_graph(length, connections)
        
        queue = deque([1])
        distance = {
            i: float('inf')
            for i in range(1, length + 1)
        }
        distance[1] = 0
        while queue:
            node = queue.popleft()
            for next_node in graph[node]:
                if distance[next_node] > distance[node]:
                    distance[next_node] = distance[node]
                    queue.append(next_node)
            for next_node in range(node + 1, min(node + 7, length + 1)):
                if distance[next_node] > distance[node] + 1:
                    distance[next_node] = distance[node] + 1
                    queue.append(next_node)
        return distance[length]

    def build_graph(self, length, connections):
        graph = {
            i: set()
            for i in range(1, length + 1)
        }
        for a, b in connections:
            graph[a].add(b)
        return graph
# version 2 堆优化
class Solution:
    def modernLudo(self, length, connections):
        import heapq

        graph = self.build_graph(length, connections)
        queue = [(0, 1)]
        distance = {
            i: float('inf')
            for i in range(1, length + 1)
        }
        distance[1] = 0
        while queue:
            dist, node = heapq.heappop(queue)
            for next_node in graph[node]:
                if distance[next_node] > dist:
                    distance[next_node] = dist
                    heapq.heappush(queue, (dist, next_node))
            for next_node in range(node + 1, min(node + 7, length + 1)):
                if distance[next_node] > dist + 1:
                    distance[next_node] = dist + 1
                    heapq.heappush(queue, (dist + 1, next_node))
        return distance[length]

    def build_graph(self, length, connections):
        graph = {
            i: set()
            for i in range(1, length + 1)
        }
        for a, b in connections:
            graph[a].add(b)
        return graph
```

两个队列交替
```python
class Solution:
    def modernLudo(self, length, connections):
        graph = self.build_graph(length, connections)
        
        queue = [1]
        distance = {1: 0}
        while queue:
            next_queue = []
            for node in queue:
                for direct_node in graph[node]:
                    if direct_node in distance:
                        continue
                    distance[direct_node] = distance[node]
                    queue.append(direct_node)
            for node in queue:
                for next_node in range(node + 1, min(node + 7, length + 1)):
                    if next_node in distance:
                        continue
                    distance[next_node] = distance[node] + 1
                    next_queue.append(next_node)
            queue = next_queue
                
        return distance[length]

    def build_graph(self, length, connections):
        graph = {
            i: set()
            for i in range(1, length + 1)
        }
        for a, b in connections:
            graph[a].add(b)
        return graph
```

BFS+BFS解法。外层 BFS 做最短路径，内层 BFS 找连通块。
```python
class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modernLudo(self, length, connections):
        from collections import deque
        
        graph = self.build_graph(length, connections)
        
        queue = deque([1])
        distance = {1: 0}
        while queue:
            node = queue.popleft()
            for neighbor in range(node + 1, min(node + 7, length + 1)):
                connected_nodes = self.get_unvisited_nodes(graph, distance, neighbor)
                for connected_node in connected_nodes:
                    distance[connected_node] = distance[node] + 1
                    queue.append(connected_node)
        return distance[length]

    def build_graph(self, length, connections):
        graph = {
            i: set()
            for i in range(1, length + 1)
        }
        for a, b in connections:
            graph[a].add(b)
        return graph
        
    def get_unvisited_nodes(self, graph, distance, node):
        from collections import deque
        queue = deque([node])
        unvisited_nodes = set()
        while queue:
            node = queue.popleft()
            if node in distance:
                continue
            unvisited_nodes.add(node)
            for neighbor in graph[node]:
                if neighbor not in distance:
                    queue.append(neighbor)
                    unvisited_nodes.add(neighbor)
        return unvisited_nodes
```

DP:
坑有点多，因为存在connections的两地s -> t的目的地t对应的s可能是多个的
而且，多个s中不能使用贪心算法直接取最小的s来得到最短步数（换句话说，就是你跳跃的越远不见得能减少步数）
所以这里用一个dic来存t对应的s值，有多个s值的就放在list里面。

转移方程：

没有connections时：
dp[i] = min(dp[i], dp[i-j] + 1)
其中i - j > 0, j为1-6的骰子点数

有connections时：
dp[i] = min(dp[i], dp[k])
k -> i对应的连接起始点的位置，有多个时，遍历取min(dp[k])
```python
class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modernLudo(self, length, connections):
        # Write your code here
        if length == 1:
            return 0
        dic = {}
        for s, t in connections:
            if t in dic:
                dic[t].append(s)
                continue
            dic[t] = [s]
        dp = [sys.maxsize]*(length+1)
        dp[0] = dp[1] = 0
        
        for i in range(2, length+1):
            if i in dic:
                for j in dic[i]:
                    dp[i] = min(dp[i], dp[j])
            for j in range(1, 7):
                if i - j > 0:
                    dp[i] = min(dp[i], dp[i-j] + 1)
        return dp[-1]
```