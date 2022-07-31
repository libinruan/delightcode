# DFS
![](http://postimg.cc/zHgZYcCY)
```python
class Solution:
    """
    @param n: an integer, denote the number of courses
    @param p: a list of prerequisite pairs
    @return: return an integer,denote the number of topologicalsort
    """

    def topologicalSortNumber(self, n, p):
        # Write your code here

        def dfs(visited, visited_count, graph, indegree, memo):
            if visited_count == len(graph):
                return 1

            if visited in memo:
                return memo[visited]

            ret = 0
            for n in graph:
                if indegree[n] == 0 and visited & (1<<n) == 0:

                    visited |= 1<<n
                    visited_count += 1

                    for sub in graph[n]:
                        indegree[sub] -= 1

                    ret += dfs(visited, visited_count, graph, indegree, memo)

                    for sub in graph[n]:
                        indegree[sub] += 1
                    
                    visited_count -= 1    
                    visited &= ~(1<<n)
            
            memo[visited] = ret
            return ret

        graph = {i: set() for i in range(n)}
        indegree = {i: 0 for i in range(n)}
        visited = 0

        for take, take_first in p:
            # take_first -> take (indegree++)
            # take is dependes on take_first
            graph[take_first].add(take)
            indegree[take] += 1

        return dfs(visited, 0, graph, indegree, {})
```

# DFS ii
```python
    def topologicalSortNumber(self, n, p):
        
        if p == []:
            res = 1
            while n != 1:
                res *= n
                n -= 1
            return res
            
        ##### build graph
        graph = {i: [] for i in range(n)}
        in_degree = {i: 0 for i in range(n)}
        for course, pre in p:
            graph[pre].append(course)
            in_degree[course] += 1
        
        res = [0]
        visited = set()
        for course in graph:
            if in_degree[course] == 0:
                visited.add(course)
                self.dfs(graph, in_degree, course, res, 1, visited)
                visited.remove(course)
        return res[0]
    
    
    def dfs(self, graph, in_degree, course, res, depth, visited):
        
        if len(graph) == depth:
            res[0] += 1
            
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            
        for next_course in graph:
            if in_degree[next_course] == 0 and next_course not in visited:
                visited.add(next_course)
                self.dfs(graph, in_degree, next_course, res, depth + 1, visited)
                visited.remove(next_course)
                
        for next_course in graph[course]:
            in_degree[next_course] += 1   
```

# DFS + memorized search
![](https://i.postimg.cc/yx2bwnbn/Jiuzhang-vip-30days.png)
```python
class Solution:
    """
    @param n: an integer, denote the number of courses
    @param p: a list of prerequisite pairs
    @return: return an integer,denote the number of topologicalsort
    """
    def topologicalSortNumber(self, n, p):
        # Write your code here
        if n == 1:
            return 1

        graph, indegree = self.buildGraph(n, p)
        ret = [0]
        visited = [0 for i in range(n)]
        memo = {}
        return self.dfs(n, graph, indegree, 0, visited, memo)

    def buildGraph(self, n, p):
        graph = {i:set() for i in range(n)}
        indegree = {i:0 for i in range(n)}
        for end, start in p:
            if end not in graph[start]:
                graph[start].add(end)
                indegree[end] += 1
        return graph, indegree

    def dfs(self, n, graph, indegree, count, visited, memo):
        if count == n:
            return 1

        state = tuple(visited)
        if state in memo:
            return memo[state]

        num = 0
        for i in range(n):
            if visited[i] == 0 and indegree[i] == 0:
                visited[i] = 1
                for neighbor in graph[i]:
                    indegree[neighbor] -= 1
                num += self.dfs(n, graph, indegree, count + 1, visited, memo)
                for neighbor in graph[i]:
                    indegree[neighbor] += 1
                visited[i] = 0

        memo[state] = num
        return num
```

# DFS + backtrack
最基础的DFS版本，一定要记得回溯。
```python
class Solution:
    """
    @param n: an integer, denote the number of courses
    @param p: a list of prerequisite pairs
    @return: return an integer,denote the number of topologicalsort
    """
    def topologicalSortNumber(self, n, p):
        # Write your code here
        if n == 1:
            return 1

        graph, indegree = self.buildGraph(n, p)
        ret = [0]
        self.dfs(n, graph, indegree, set(), ret)

        return ret[0]

    def buildGraph(self, n, p):
        graph = {i:set() for i in range(n)}
        indegree = {i:0 for i in range(n)}
        for end, start in p:
            if end not in graph[start]:
                graph[start].add(end)
                indegree[end] += 1
        return graph, indegree

    def dfs(self, n, graph, indegree, visited, ret):
        if len(visited) == n:
            ret[0] += 1
            return

        for i in range(n):
            if i not in visited and indegree[i] == 0:
                visited.add(i)
                for neighbor in graph[i]:
                    indegree[neighbor] -= 1
                self.dfs(n, graph, indegree, visited, ret)
                for neighbor in graph[i]:
                    indegree[neighbor] += 1
                visited.remove(i)
```