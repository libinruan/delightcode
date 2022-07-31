# solution DP + state supression
![](https://i.postimg.cc/DwTCLWkW/Jiuzhang-vip-30days.png)
```python
from typing import (
    List,
)

class Solution:
    def findLastOne(self, n: int):
        ret = 1
        while n % 2 == 0:
            ret += 1
            n >>= 1
        return ret
    def min_cost(self, n: int, roads: List[List[int]]) -> int:
        INT_MAX = 2 ** 31 - 1
        m = len(roads)
        dp = [[(INT_MAX // 2) for i in range(1 << n)] for j in range(n + 1)]
        for mask in range(2, (1 << n), 2):
            # 如果 mask 只包含一个 1，即 mask 是 2 的幂
            if (mask & (mask - 1)) == 0:
                u = self.findLastOne(mask)
                dp[u][mask] = 0;
            else:
                for i in range(m):
                    u = roads[i][0]
                    v = roads[i][1]
                    w = roads[i][2]
                    if u == 1 or v == 1:
                        continue
                    if (mask & (1 << (u - 1))) and (mask & (1 << (v - 1))):
                        dp[v][mask] = min(dp[v][mask], dp[u][mask ^ (1 << (v - 1))] + w)
                        dp[u][mask] = min(dp[u][mask], dp[v][mask ^ (1 << (u - 1))] + w)
        ans = INT_MAX
        for i in range(m):
            u = roads[i][0]
            v = roads[i][1]
            w = roads[i][2]
            if u == 1:
                ans = min(ans, dp[v][(1 << n) - 2] + w)
            elif v == 1:
                ans = min(ans, dp[u][(1 << n) - 2] + w)
        return ans
```
![](https://i.postimg.cc/7YvXrCLB/Jiuzhang-vip-30days.png)

# Prunning + DFS
![](https://i.postimg.cc/Nf78hpSM/Jiuzhang-vip-30days.png)
```python
class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def __init__(self):
        self.result = float('Inf')
    
    def minCost(self, n, roads):
        graph = self.buildGraph(n, roads)
        
        self.dfs(graph, 1, 0, set([1]))
        
        return self.result
        
        
    def dfs(self, graph, start, cmc, visited):
        
        if len(visited) == len(graph):
            self.result = min(self.result, cmc)
            return
        
        for next_city in graph[start]:
            if next_city in visited:
                continue
            
            if cmc > self.result:
                continue
            
            cur_cost = graph[start][next_city]
            if cur_cost > self.result:
                continue

            visited.add(next_city)
            self.dfs(graph, next_city, cmc + cur_cost, visited) 
            visited.remove(next_city)
        
        
    def buildGraph(self, n, roads):
        graph = { i : {} for i in range(1, n + 1)}
        
        for u, v, w in roads:
            if v not in graph[u]:
                graph[u][v] = w
            else:
                graph[u][v] = min(graph[u][v], w)
            
            if u not in graph[v]:
                graph[v][u] = w
            else:
                graph[v][u] = min(graph[v][u], w)
        
        return graph
```

# BFS
最短路径法bfs。
没啥特别的，只要有更短的路就一直进队列，直到访问过所有点。
```python
import heapq
class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def minCost(self, n, roads):
            # Write your code here
            if not roads:
                return 0
            p = self.make_graph(roads)
            q = []
            for i in range(1, n):
                if i + 1 in p[1]:
                    visited = set()
                    visited.add(1)
                    visited.add(i + 1)
                    heapq.heappush(q, [p[1][i + 1], i + 1, visited])
            while q:
                d, cur, visited = heapq.heappop(q)
                if len(visited) == n:
                    return d
                for nei in p[cur]:
                    if nei in visited:
                        continue
                    tmp1 = set()
                    for x in visited:
                        tmp1.add(x)
                    tmp1.add(nei)
                    heapq.heappush(q, [d + p[cur][nei], nei, tmp1])
            return -1
```


# sol 1
如果要保证正确性的最优做法。状态压缩动态规划。

```python
class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def minCost(self, n, roads):
        graph = self.construct_graph(roads, n)
        state_size = 1 << n
        f = [
            [float('inf')] * (n + 1)
            for _ in range(state_size)
        ]
        f[1][1] = 0
        for state in range(state_size):
            for i in range(2, n + 1):
                if state & (1 << (i - 1)) == 0:
                    continue
                prev_state = state ^ (1 << (i - 1))
                for j in range(1, n + 1):
                    if prev_state & (1 << (j - 1)) == 0:
                        continue
                    f[state][i] = min(f[state][i], f[prev_state][j] + graph[j][i])
        return min(f[state_size - 1])
        
    def construct_graph(self, roads, n):
        graph = {
            i: {j: float('inf') for j in range(1, n + 1)}
            for i in range(1, n + 1)
        }
        for a, b, c in roads:
            graph[a][b] = min(graph[a][b], c)
            graph[b][a] = min(graph[b][a], c)
        return graph
```        

# DFS
使用了 pruning 的 DFS
```python
class Result:
    def __init__(self):
        self.min_cost = float('inf')
    
class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def minCost(self, n, roads):
        graph = self.construct_graph(roads, n)
        result = Result()
        self.dfs(1, n, [1], set([1]), 0, graph, result)
        return result.min_cost
        
    def dfs(self, city, n, path, visited, cost, graph, result):
        if len(visited) == n:
            result.min_cost = min(result.min_cost, cost)
            return
    
        for next_city in graph[city]:
            if next_city in visited:
                continue
            if self.has_better_path(graph, path, next_city):
                continue
            visited.add(next_city)
            path.append(next_city)
            self.dfs(
                next_city,
                n,
                path,
                visited,
                cost + graph[city][next_city],
                graph,
                result,
            )
            path.pop()
            visited.remove(next_city)
    
    def construct_graph(self, roads, n):
        graph = {
            i: {j: float('inf') for j in range(1, n + 1)}
            for i in range(1, n + 1)
        }
        for a, b, c in roads:
            graph[a][b] = min(graph[a][b], c)
            graph[b][a] = min(graph[b][a], c)
        return graph
        
    def has_better_path(self, graph, path, city):
        for i in range(1, len(path)):
            if graph[path[i - 1]][path[i]] + graph[path[-1]][city] >\
                    graph[path[i - 1]][path[-1]] + graph[path[i]][city]:
                return True
        return False
```


# randomization
使用随机化算法，不保证正确性，但是可以处理很大的数据，得到近似答案。
调整策略是交换 i, j 两个点的位置，看看是否能得到更优解
测试中如果失败了可以多跑几次。
```python
# increase RANDOM_TIMES or submit your code again 
# if you got wrong answer.
RANDOM_TIMES = 1000

class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def minCost(self, n, roads):
        graph = self.construct_graph(roads, n)
        min_cost = float('inf')
        for _ in range(RANDOM_TIMES):
            path = self.get_random_path(n)
            cost = self.adjust_path(path, graph)
            min_cost = min(min_cost, cost)
        return min_cost
        
    def construct_graph(self, roads, n):
        graph = {
            i: {j: float('inf') for j in range(1, n + 1)}
            for i in range(1, n + 1)
        }
        for a, b, c in roads:
            graph[a][b] = min(graph[a][b], c)
            graph[b][a] = min(graph[b][a], c)
        return graph
    
    def get_random_path(self, n):
        import random
        
        path = [i for i in range(1, n + 1)]
        for i in range(2, n):
            j = random.randint(1, i)
            path[i], path[j] = path[j], path[i]
        return path
        
    def adjust_path(self, path, graph):
        n = len(graph)
        adjusted = True
        while adjusted:
            adjusted = False
            for i in range(1, n):
                for j in range(i + 1, n):
                    if self.can_swap(path, i, j, graph):
                        path[i], path[j] = path[j], path[i]
                        adjusted = True
        cost = 0
        for i in range(1, n):
            cost += graph[path[i - 1]][path[i]]
        return cost
    
    def can_swap(self, path, i, j, graph):
        before = self.adjcent_cost(path, i, path[i], graph)
        before += self.adjcent_cost(path, j, path[j], graph)
        after = self.adjcent_cost(path, i, path[j], graph)
        after += self.adjcent_cost(path, j, path[i], graph)
        return before > after
    
    def adjcent_cost(self, path, i, city, graph):
        cost = graph[path[i - 1]][city]
        if i + 1 < len(path):
            cost += graph[city][path[i + 1]]
        return cost
```


# brute force DFS
暴力 DFS 算法
```python
class Result:
    def __init__(self):
        self.min_cost = float('inf')
    
class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def minCost(self, n, roads):
        graph = self.construct_graph(roads, n)
        result = Result()
        self.dfs(1, n, set([1]), 0, graph, result)
        return result.min_cost
        
    def dfs(self, city, n, visited, cost, graph, result):
        if len(visited) == n:
            result.min_cost = min(result.min_cost, cost)
            return
    
        for next_city in graph[city]:
            if next_city in visited:
                continue
            visited.add(next_city)
            self.dfs(next_city, n, visited, cost + graph[city][next_city], graph, result)
            visited.remove(next_city)
    
    def construct_graph(self, roads, n):
        graph = {i: {} for i in range(1, n + 1)}
        for a, b, c in roads:
            if b not in graph[a]:
                graph[a][b] = c
            else:
                graph[a][b] = min(graph[a][b], c)
            if a not in graph[b]:
                graph[b][a] = c
            else:
                graph[b][a] = min(graph[b][a], c)
        return graph
```        