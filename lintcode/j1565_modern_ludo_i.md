![](https://i.postimg.cc/cJBkgxVZ/2022-08-30-at-21-52-15.png)

有方向性（比如从数组最左侧跳到最右侧，只能向右跳），则适合用动态规划。
但是如果没有只能向右跳的条件，则不适合用动态规划。
如果问最少跳几步，这种最短路径的问题，则可以用bfs。

何谓简单图？何谓复杂图？变成简单图才能用bfs。 

将直通关系看作图中的边。比如所有和2连通的点都是可以通过2同一层一步跳到的点。

# SPFA 
**SPFA 是 BFS 的一种拓展，差别在于SPFA的node可以重复进入对列。可以处理复杂图**
![BFS disadvantage](https://i.postimg.cc/cLvDt3pZ/2022-08-30-at-23-07-27.png)
![SPFA advantage](https://i.postimg.cc/dQGHHbFz/2022-08-31-at-00-26-02.png)

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
                if distance[next_node] > distance[node]:  # SPFA special.
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

# (2) 
两个队列交替
```python
class Solution:
    def modernLudo(self, length, connections):
        graph = self.build_graph(length, connections)
        
        queue = [1]
        distance = {1: 0}
        while queue:
            next_queue = []
            for node in queue:  # BFS 将距离为零的点都找出来。比如将距离原始节点为2的点都找出来放在同一层。
                for direct_node in graph[node]: # 将距离为零的点都找出来。还包括孙节点，曾孙节点，etc.
                    if direct_node in distance:
                        continue
                    distance[direct_node] = distance[node] # 连通者要放到同一层，所以距离不加一。
                    queue.append(direct_node) # 所以 for loop 的 queue 是动态增长的。
            for node in queue:  # 对所有在距离为2的点，都开始投骰子，去拓展下一层。
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
# (1) two-layer BFS
BFS+BFS解法。外层 BFS 做最短路径，内层 BFS 找连通块。
将直通关系connections构图，以邻街表(adjacency list)的形式来表示，
具体就是用 Python: dict{node: set(neighbors)} or Java: HashMap<Node, HashSet<Node>>
本意是用 list 储存 neighbors，但是实战中用 set() 的数据结构可以去重，以及O(1) 查询a, b两点是否有连边。比用adjacent matrix好，因为adjacent matrix是O(n^2), 而adjacent list只有O(n)。

```python
class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modernLudo(self, length, connections):
        from collections import deque
        # build graph 丢给子函数去处理，不要写在主函数中。
        graph = self.build_graph(length, connections) # 注意此为连通块的graph, 不是最短路径的graph。
        
        queue = deque([1])  # BFS template. The starting point here is node 1, not zero based.
        distance = {1: 0}  # BFS template as well. The distance from the starting point to the starting point is zero.
        while queue:  # 此为外层求最短路经的BFS
            node = queue.popleft()
            for neighbor in range(node + 1, min(node + 7, length + 1)):  # 掷六面骰子，此处就是BFS找邻居。
                connected_nodes = self.get_unvisited_nodes(graph, distance, neighbor)  # 找出有效的邻居，此处有效的定义是有连通。比如1 -> 2 （1的当前邻居）-> 4 -> 10, 就是 1, 2, 4, 10 是连通的。另外，此处传入distance这个dict有助于效率，避免重复计算。比如，掷出从1跳三步到4，1->4->10, 这样的路径在1->2->4->10就有走过了。此处做了这样的优化，保证每个点只被走过一次。所以我们的complexity 两个BFS是 O(2(n+m)) 而不是 O((n+m)^2)。
                for connected_node in connected_nodes:
                    distance[connected_node] = distance[node] + 1
                    queue.append(connected_node)
        return distance[length] 

    def build_graph(self, length, connections):  # 有length个点
        graph = {
            i: set()
            for i in range(1, length + 1)
        }
        for a, b in connections:  # 我们的边(connections)是有向边, a walk to b。
            graph[a].add(b)  # 将 b 加入到 a 所能走到的所有的点里面。Not vice versa.
        return graph
        
    def get_unvisited_nodes(self, graph, distance, node):
        from collections import deque
        queue = deque([node])
        unvisited_nodes = set()  # BFS template, 此外, 此处求取连通性只需用到set(), 不需要用到dict()。
        while queue:  # 此为内层求连通块的BFS
            node = queue.popleft()
            if node in distance: #如果知道此node的最短距离，那么我们就不算，以避免重复。
                continue
            unvisited_nodes.add(node)
            for neighbor in graph[node]: #探索此node的邻居
                if neighbor not in distance and neighbor not in unvisited_nodes: #Lipin: the 2nd condition 是video老师加上的，我怀疑不需要。
                    queue.append(neighbor)  # BFS template
                    unvisited_nodes.add(neighbor)  # used for return
        return unvisited_nodes
```

# DP
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