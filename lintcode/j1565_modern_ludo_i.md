![](https://i.postimg.cc/cJBkgxVZ/2022-08-30-at-21-52-15.png)

**必须熟悉either DP or SPFA 的解法，择一面试。DP的代码最短，最简单**。

有方向性（比如从数组最左侧跳到最右侧，只能向右跳），则适合用动态规划。
但是如果没有只能向右跳的条件，则不适合用动态规划。
如果问最少跳几步，这种最短路径的问题，则可以用bfs。

将直通关系看作图中的边。比如所有和2连通的点都是可以通过2同一层一步跳到的点。


# (4) DP  

![](https://i.postimg.cc/6QVgBdHw/2022-08-31-at-20-46-55.png)
要素：状态，转移方程，初始化，

## 从底向上（从右至左）的解法
![](https://i.postimg.cc/JhRKcSqV/2022-08-31-at-20-48-02.png)
转移方程右手边何时加一何时加零，取决于由i到j是直通过去的，还是掷骰子决定步数过去的。由i要选择哪个j，取决于被选择的j到达终点的步数最少（再次提醒，若是依据掷骰子决定距离才跳到的，就要加上跳跃的这一步，所以要加一）。  
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

        dp = [float('inf')] * (length + 1)
        dp[length] = 0  # Jumping from itself to itself takes zero step.
        for i in range(length - 1, 0, -1):  # j 比 i 更靠近终点（右端）。
            # 内部两个for循环顺序先后无所谓。
            for j in range(i + 1, min(i + 7, length + 1)):  # 要跳跃一次才到达的邻居 
                dp[i] = min(dp[i], dp[j] + 1)
            for j in graph[i}: # 连通集的邻居
                dp[i] = min(dp[i], dp[j])
        return dp[1]
```


## 从顶到底（从左至右）的解法
坑有点多，因为存在connections的两地s -> t的目的地t对应的s可能是多个的
而且多个s中不能使用贪心算法直接取最小的s来得到最短步数（换句话说，就是你跳跃的越远不见得能减少步数），所以这里用一个dic来存t对应的s值，有多个s值的就放在list里面。

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

        dic = {} # 生成图
        for s, t in connections:
            if t in dic:
                dic[t].append(s)
                continue
            dic[t] = [s]
        
        dp = [sys.maxsize]*(length+1)
        dp[0] = dp[1] = 0
        
        for i in range(2, length+1):
            if i in dic:  # 如果当前位置有连通的邻居。
                for j in dic[i]:
                    dp[i] = min(dp[i], dp[j])
            for j in range(1, 7):  # 不管有没有连通的邻居，我们都可以掷骰子决定下一步的位置。
                if i - j > 0:
                    dp[i] = min(dp[i], dp[i-j] + 1)
        return dp[-1]
```

# (3) SPFA 
**SPFA 是 BFS 的一种拓展，差别在于SPFA的node可以重复进入对列。可以处理复杂图**

何谓简单图？答案：所有的边长都是一的图。

何谓复杂图？答案：边长可以是任意数（0, 1, 2, ...）。

复杂图要变成简单图才能用bfs。 
![BFS disadvantage](https://i.postimg.cc/cLvDt3pZ/2022-08-30-at-23-07-27.png)

(1h1m00s)
SPFA (shortest path fast algorithm)
沿用暴力的思路，先设置起点到每个节点的距离为最大值
初始化距离起点的位置为0，把起点装入队列
从队列拿出节点，然后根据构图先遍历距离为0的节点
再遍历距离为1的节点，**如果发现距离比之前的更小，重新装入队列**。
![SPFA advantage](https://i.postimg.cc/dQGHHbFz/2022-08-31-at-00-26-02.png)

```python
# version 1
class Solution:
    def modernLudo(self, length, connections):
        from collections import deque
        graph = self.build_graph(length, connections)
        
        queue = deque([1])
        distance = {
            i: float('inf')
            for i in range(1, length + 1)  # 初始化所有的点到所有的点的距离。
        }
        distance[1] = 0
        while queue:
            node = queue.popleft()
            for next_node in graph[node]: # 寻找与1的直通点。
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

# version 2 堆优化，就是使用 priority queue 来代替 queue。主要就改两行。
# 面试就被这个，老师建议。
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
        while queue: # 此处两个for循环调换顺序是无所谓的。
            dist, node = heapq.heappop(queue)
            for next_node in graph[node]:  # 处理零的边
                if distance[next_node] > dist:
                    distance[next_node] = dist
                    heapq.heappush(queue, (dist, next_node))
            for next_node in range(node + 1, min(node + 7, length + 1)):  # 处理一的边
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

# (2) 两个队列交替

第一个for循环，同层连通的拓展。

第二个for循环，是最短路径的拓展。

这个解法的两个for循环不可以对调，一定是先同层拓展结束之后，才进行下一层最短路的拓展。

```python
class Solution:
    def modernLudo(self, length, connections):
        graph = self.build_graph(length, connections)
        
        queue = [1]
        distance = {1: 0}
        while queue:  # 内部两个for循环的顺序不能调换。只有SPFA内的两大for循环可以调换。为啥呢？两队列交替的解法，必须先走完生成当前同一层的for循环，才能走生成下一层的for循环。57m00s.
            next_queue = []
            for node in queue:  # BFS 将距离为零的点都找出来。比如将距离原始节点为2的点都找出来放在"同一层"。千万注意：queue的成员会动态增加，所以不可以设死。
                for direct_node in graph[node]: # 先把直通的点都拓一遍到同一层。将距离为零的点都找出来。还包括孙节点，曾孙节点，etc.
                    if direct_node in distance:
                        continue
                    distance[direct_node] = distance[node] # 连通者要放到同一层，所以距离不加一。
                    queue.append(direct_node) # 所以 for loop 的 queue 是动态增长的。
            for node in queue:  # 上面两个for循环结束后，才开始丢骰子，建构"下一层"。对所有在距离为2的点，都开始投骰子，去拓展下一层。
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
