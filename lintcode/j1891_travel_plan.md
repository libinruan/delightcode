因为数据规模比较小，所以我们就直接遍历所有的方案数即可。n!求出所有可行的方案，然
后逐一得求出每个方案所对应的距离和，求出最小值即可
```python
class Solution:
    """
    @param arr: the distance between any two cities
    @return: the minimum distance Alice needs to walk to complete the travel plan
    """
    def __init__(self):
        self.ans = 100000000
        self.travel = [0 for i in range(20)]
        self.vis = [0 for i in range(20)]
    def travelPlan(self, arr):
        # Write your code here.
        n = len(arr)
        self.dfs(1, n, arr)
        return self.ans
    def dfs(self, k, n, arr):
        if k == n:
            self.travel[k] = 0
            tmp = 0
            for i in range(1, k + 1):
                tmp += arr[self.travel[i - 1]][self.travel[i]]
            self.ans = min(tmp,self.ans)
        for i in range(1, n):
            if self.vis[i] == 0:
                self.vis[i] = 1
                self.travel[k] = i
                self.dfs(k + 1, n, arr)
                self.vis[i] = 0
```


穷举， 时间复杂度 n!
```python
class Solution:
    """
    @param arr: the distance between any two cities
    @return: the minimum distance Alice needs to walk to complete the travel plan
    """
    def travelPlan(self, arr):
        self.res = sys.maxsize
        visited = [0]
        self.dfs(0, 0, visited, arr)
        return self.res
    
    def dfs(self, city, dist, visited, arr):
        if len(visited) == len(arr):
            self.res = min(self.res, dist + arr[visited[-1]][0])
            return
        for i in range(len(arr)):
            if i in visited:
                continue
            visited.append(i)
            self.dfs(i, dist+arr[city][i], visited, arr)
            visited.pop()
```

dfs + 最优值剪枝
```python
class Solution:
    """
    @param arr: the distance between any two cities
    @return: the minimum distance Alice needs to walk to complete the travel plan
    """
    def travelPlan(self, arr):
        # Write your code here.
        visited = set([0]) 
        result = [float('inf')] 

        self.dfs(0, visited, 0, arr, result)

        return result[0]
    
    def dfs(self, last, visited, curr_cost, arr, result): 
      n = len(arr)
      if len(visited) == n: 
        result[0] = min(result[0], curr_cost + arr[last][0])
        return 
      if curr_cost > result[0]: 
        return 
      
      for i in range(1, n): 
        if i in visited: 
          continue 
        
        visited.add(i) 
        self.dfs(i, visited, curr_cost + arr[last][i], arr, result)
        visited.remove(i)
```