[PRELIMINARY KNOWLEDGE](https://www.lintcode.com/problem/1179/solution/17493)

    - BFS

    - DFS

    - Union Find


# BFS, DFS, Union Find
```python
# BFS
import collections

class Solution:
    def beginbfs(self, M):
        # 人数
        n = len(M)
        # 答案
        ans = 0
        # 标记是否访问过
        visisted = {}
        for i in range(n):
            visisted[i] = False
        # 遍历每个人，如果这个人还没访问过 就从这个人开始做一遍bfs
        for i in range(n):
            if (visisted[i] == False):
                ans += 1
                q = collections.deque()
                # 标记起点并压入队列
                visisted[i] = True
                q.append(i)
                while (len(q) != 0):
                    # 取出队首
                    now = q.popleft()
                    # 从队首找朋友
                    for j in range(n):
                        # 找到新朋友（之前没访问过的朋友）就标记访问并压入队列
                        if (M[now][j] == 1 and visisted[j] == False):
                            visisted[j] = True
                            q.append(j)
        return ans
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here
        ansbfs = self.beginbfs(M)
        return ansbfs
```

```python
# DFS
class Solution:
    def dfs(self, x, M, visisted):
        for i in range(len(M)):
            if (M[x][i] == 1 and visisted[i] == False):
                visisted[i] = True
                self.dfs(i, M, visisted)
    def begindfs(self, M):
        # 人数
        n = len(M)
        # 答案
        ans = 0
        # 标记是否访问过
        visisted = {}
        for i in range(n):
            visisted[i] = False
        # 遍历每个人，如果这个人还没访问过 就从这个人开始做一遍dfs
        for i in range(n):
            if (visisted[i] == False):
                ans += 1
                visisted[i] = True
                self.dfs(i, M, visisted)
        return ans
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here
        ansdfs = self.begindfs(M)
        return ansdfs
```

```python
# Union Find
class Solution:
    def find(self, x, fa):
        if x == fa[x]:
            return x
        else:
            fa[x] = self.find(fa[x], fa)
            return fa[x]
    def beginset(self, M):
        # 人数
        n = len(M)
        # 答案
        ans = n
        # fa数组
        fa = {}
        for i in range(n):
            fa[i] = i
        # 遍历每个人，进行并查集合并
        for i in range(n):
            for j in range(n):
                if (i != j and M[i][j] == 1):
                    # 这两个朋友在不同的集合里 就把这两个集合合并
                    # 合并两个集合，集合数量减少1个
                    if (self.find(i, fa) != self.find(j, fa)):
                        ans -= 1
                        fa[self.find(i, fa)] = self.find(j, fa)
        return ans
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here
        ansset = self.beginset(M)
        return ansset
```



# Union Find
sol: https://www.lintcode.com/problem/1179/solution/56973
```python
class Solution:
    def find_circle_num(self, m: List[List[int]]) -> int:
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        
        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)
        
        cities = len(m)
        parent = list(range(cities))
        
        for i in range(cities):
            for j in range(i + 1, cities):
                if m[i][j] == 1:
                    union(i, j)
        
        provinces = sum(parent[i] == i for i in range(cities))
        return provinces
```



# DFS
sol: https://www.lintcode.com/problem/1179/solution/56970
```pytohn
from typing import (
    List,
)

class Solution:
    def find_circle_num(self, m: List[List[int]]) -> int:
        def dfs(i: int):
            for j in range(cities):
                if m[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        cities = len(m)
        visited = set()
        provinces = 0

        for i in range(cities):
            if i not in visited:
                dfs(i)
                provinces += 1
        
        return provinces
```



# BFS
sol: https://www.lintcode.com/problem/1179/solution/56971
```python
class Solution:
    def find_circle_num(self, m: List[List[int]]) -> int:
        cities = len(m)
        visited = set()
        provinces = 0
        
        for i in range(cities):
            if i not in visited:
                Q = collections.deque([i])
                while Q:
                    j = Q.popleft()
                    visited.add(j)
                    for k in range(cities):
                        if m[j][k] == 1 and k not in visited:
                            Q.append(k)
                provinces += 1
        
        return provinces
```