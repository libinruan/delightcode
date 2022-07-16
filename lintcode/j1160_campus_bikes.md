算法一
将所有的自行车和工人两两配对，求出距离后按照三关键字进行sort排序

第一关键字是距离大小
第二关键字是工人编号
第三关键字是自行车编号

排序完成后遍历数组，如果扫到的工人和自行车都还没分配，就把当前的自行车分配给当前工人，否则就继续扫下一个

算法二
将所有的自行车和工人两两配对，求出距离后 按距离存到桶里

如果我们工人和自行车配对时候，先按工人从小到大枚举，再按自行车编号从小到大

那么先进桶的配对方案满足下面的三关键字排序

第一关键字是距离大小
第二关键字是工人编号
第三关键字是自行车编号

排序完成后遍历桶排序数组，如果扫到的工人和自行车都还没分配，就把当前的自行车分配给当前工人，否则就继续扫下一个

复杂度分析
算法一
时间复杂度
配对后有NM个元素，sort快排带一个loglog 所以总时间复杂度是**O(NMlog(NM))O(NMlog(NM))**

空间复杂度
存放所有配对的元素 空间复杂度**O(NM)O(NM)**

算法二
时间复杂度
配对后有NM个元素，用的桶排序 所以总时间复杂度是**O(NM)O(NM)**

空间复杂度
存放所有配对的元素 空间复杂度**O(NM)O(NM)**

```c
//Method I
class Solution {
  public:
    /**
     * @param workers: workers' location
     * @param bikes: bikes' location
     * @return: assign bikes
     */
    vector<int> assignBikes(vector<vector<int>> &workers, vector<vector<int>> &bikes) {
        // write your code here
        
        //工人数量 
        int n = workers.size();
        //自行车数量 
		int m = bikes.size();
        //工人与自行车两两配对，计算距离，并存到sol里
		
		//pair<int, pair<int, int> > 存放距离 工人编号 自行车编号 
		vector<pair<int, pair<int, int> > > sol;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
            	//计算距离 
                int cost = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]);
                //压入sol 
				sol.push_back(make_pair(cost, make_pair(i, j)));
            }
        }
        //对sol排序 
        sort(sol.begin(), sol.end());
        //标记工人是否分配了车子 
        vector<bool> visisted_worker(n, false);
        //标记车子是否被分配 
		vector<bool> visisted_bike(m, false);
        vector<int>ans(n, 0);
        //按距离从小到大依次处理 
        for(int i = 0; i < n * m; i++) {
            int cost = sol[i].first;
            int workerIdx = sol[i].second.first;
            int bikeIdx = sol[i].second.second;
            //如果工人 和 车子都还没分配 就分配，并记录答案 
            if(visisted_worker[workerIdx] == false && visisted_bike[bikeIdx] == false) {
                visisted_worker[workerIdx] = visisted_bike[bikeIdx] = true;
                ans[workerIdx] = bikeIdx;
            }
        }
        return  ans;
    }
};
```

```python
class Solution:
    """
    @param workers: workers' location
    @param bikes: bikes' location
    @return: assign bikes
    """

    def assignBikes(self, workers, bikes):
        # write your code here

        # 工人和车子数量
        n = len(workers)
        m = len(bikes)
        # 排序数组，存放距离 工人编号 车子编号
        sol = [0 for i in range(n * m)]
        for i in range(n):
            for j in range(m):
                # 计算距离
                cost = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                # 压入sol
                sol[i * m + j] = [cost, i, j]

        # 对按照距离 工人编号 车子编号 三关键字排序
        sol.sort()

        # 标记工人有没有分配车子
        visisted_worker = [False]*n
        # 标记车子有没有被分配
        visisted_bike = [False]*m

        # 答案数组
        ans = [0 for i in range(n)]
        for i in range(len(sol)):
            # 人和车的编号
            cost,workersIdx,bikeIdx = sol[i]
            # 车和人都还没有分配
            if visisted_worker[workersIdx] == False and visisted_bike[bikeIdx] == False:
                visisted_worker[workersIdx] = visisted_bike[bikeIdx] = True
                ans[workersIdx] = bikeIdx
        return ans
```

```python
class Solution:
    """
    @param workers: workers' location
    @param bikes: bikes' location
    @return: assign bikes
    """

    def assignBikes(self, workers, bikes):
        # write your code here

        # 工人和车子数量
        n = len(workers)
        m = len(bikes)
        # 桶排序 按照距离存放
        Bucket = [[] for i in  range(2002)]
        for i in range(n):
            for j in range(m):
                # 计算距离
                cost = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                # 压入Bucket
                Bucket[cost].append([i, j])

        # 标记工人有没有分配车子
        visisted_worker = [False]*n
        # 标记车子有没有被分配
        visisted_bike = [False]*m

        # 答案数组
        ans = [0]*n
        for i in range(2001):
            for j in range(len(Bucket[i])):
                # 人和车的编号
                workersIdx,bikeIdx = Bucket[i][j]
                # 车和人都还没有分配
                if visisted_worker[workersIdx] == False and visisted_bike[bikeIdx] == False:
                    visisted_worker[workersIdx] = visisted_bike[bikeIdx] = True
                    ans[workersIdx] = bikeIdx
        return ans
```



暴力算距离 + 桶排序版本在同一个桶子里面不需要再排序， 因为放进来的时候， 本来就
是先放的小的worker index， 所以到这里的时候， 肯定是按照worker index排序的， 放
心吧。
```python
class Solution:
    """
    @param workers: workers' location
    @param bikes: bikes' location
    @return: assign bikes
    """
    def assignBikes(self, workers, bikes):
        distances_to_indexes = [[] for _ in range(2001)]
        allocated_bikes = set()
        for i in range(len(workers)):
            for j in range(len(bikes)):
                distance = self.calculate_distance(i, workers[i], j, bikes[j])
                distances_to_indexes[distance[0]].append((distance[1], distance[2]))
        results = [-1] * len(workers)
        for d in range(len(distances_to_indexes)):
            worker_bikes = distances_to_indexes[d]
            for worker_bike in worker_bikes:
                if results[worker_bike[0]] == -1 and worker_bike[1] not in allocated_bikes:
                    allocated_bikes.add(worker_bike[1])
                    results[worker_bike[0]] = worker_bike[1]
                
        return results
    
    def calculate_distance(self, worker_index, worker, bike_index, bike):
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]), worker_index, bike_index
```




三种解法：

1. 桶排續
2. 全排續
3. 堆排序

时间复杂度：1 都是 O(m*n)，2 和 3 是 O(mnlogmn)。

```python
class Solution_bucket_sort:
    
    def assignBikes(self, workers, bikes):
        m, n = len(workers), len(bikes) 
        
        def manhattan(a, b):
            (x1, y1), (x2, y2) = a, b
            return abs(x1-x2) + abs(y1-y2)
            
        buckets = [[] for _ in range(2001)]
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                buckets[manhattan(worker, bike)] += (i, j),
        
        bikes, taken = [n] * m, set()
        for bucket in buckets:
            if len(taken) == m:
                break
            for i, j in bucket:
                if bikes[i] == n and j not in taken:
                    bikes[i] = j 
                    taken.add(j)
        return bikes
            
class Solution_pure_sort:
    
    def assignBikes(self, workers, bikes):
        m, n = len(workers), len(bikes) 
        
        def manhattan(a, b):
            (x1, y1), (x2, y2) = a, b
            return abs(x1-x2) + abs(y1-y2)
        
        def sort_key(pair):
            i, j = pair
            return (manhattan(workers[i], bikes[j]), i, j)
            
        output, taken = [n] * m, set()
        for i, j in sorted(((i, j) for i in range(m) for j in range(n)), key = sort_key):
            if len(taken) == m:
                break
            if output[i] == n and j not in taken:
                output[i] = j
                taken.add(j)
        return output

from heapq import heapify, heappop
class Solution_heap
    
    def assignBikes(self, workers, bikes):
        m, n = len(workers), len(bikes) 
        
        def manhattan(a, b):
            (x1, y1), (x2, y2) = a, b
            return abs(x1-x2) + abs(y1-y2)
            
        h = [(manhattan(worker, bike), i, j)
                for i, worker in enumerate(workers)
                for j, bike in enumerate(bikes)]
        heapify(h)
        
        output, taken = [n] * m, set()
        while len(taken) != m:
            _, i, j = heappop(h)
            if output[i] == n and j not in taken:
                output[i] = j
                taken.add(j)
        return output
```