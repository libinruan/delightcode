<!-- ------------------------------- Amicus -------------------------------- -->
我觉得这道题最重要的一步就是发现：
if len(edges) != n - 1:
return False
很明显的道理，如果有5个节点，那如果是没有cycle的情况下，中间最多只会连四段，就是那个edges的那个数组只有4 小块。我之前花了很多时间在traverse那个整个树的同时去尝试处理cycle的detection，其实到头来非常的简单，开头的两行就搞定了。

剩下的步骤就是套用那个 courseSchedule的那个directed graph的模板。这个题真的比那个courseSchedule简单太多了。有一个caveat就是题目只给了一个undirected graph，所以在整理那个graph的数组时需要都加，就非常巧妙

```python
from collections import deque
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False

        graph = {i:[] for i in range(n)}
        for (i, j) in edges:
            graph[i].append(j)
            graph[j].append(i)
            

        queue = deque()
        visit = set()
        
        visit.add(0)
        queue.append(0)
        
                       
        while queue:
            node = queue.popleft()
            for x in graph[node]:
                if x not in visit:
                    queue.append(x)
                    visit.add(x)

        return len(visit) == n 
                    
                    
        
        

        
                     



```


<!-- ------------------------------- di.cao -------------------------------- -->
BFS解法，简单易懂，没有使用python的‘省代码行数’的技巧。
dictionary 建立邻接表，queue做BFS用，visited为hashset，快速查找。
先判断边数是否为节点数-1，再判断是否所有点可以访问到。两个条件可以看是否无环。

另附超简短写法BFS，参考用，不用visited；queue改stack并改变pop，可转变成DFS，思路一样。

```python
class Solution:
    """
    @param: n: An integer
    @param: edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n == 0:
            return False
        if len(edges) != n-1:
            return False
        g = {}
        for e in edges:
            g[e[0]] = g.get(e[0], []) + [e[1]]
            g[e[1]] = g.get(e[1], []) + [e[0]]
        q = [0]
        visited = set([0])
        while q:
            node = q.pop(0)
            for i in g.get(node, []):
                if i in visited:
                    continue
                q.append(i)
                visited.add(i)
        return len(visited) == n
    
    # 精简解法
	def validTree(self, n, edges):
        # write your code here
        if n == 0:
            return False
        if len(edges) != n-1:
            return False
        g = {}
        for e in edges:
            g[e[0]] = g.get(e[0], []) + [e[1]]
            g[e[1]] = g.get(e[1], []) + [e[0]]
        q = [0]
        while q:
            q += g.pop(q.pop(0), [])
        return not g
```


直接用的Union Find最基本的模版做的。这道题就是两步走：
1.判断edges数目必须等于n-1
2.连通图总集合数为1。这样就保证了图中所有点连通且无环。

```c
class UnionFind{
    private int[] father;
    private int count;
    public UnionFind(int n) {
        father = new int[n];
        count = n;
        for(int i = 0; i < n; i++) {
            father[i] = i;
        }
    }
    
    public int getCount() {
        return count;
    }
    
    public int find(int x) {
        if(father[x]==x) {
            return x;
        }
        return father[x] = find(father[x]);
    }
    
    public void connect(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        if(rootA!=rootB) {
            father[rootA] = rootB;
            count--;
        }
    }
}

public class Solution {
    /*
     * @param n: An integer
     * @param edges: a list of undirected edges
     * @return: true if it's a valid tree, or false
     */
    public boolean validTree(int n, int[][] edges) {
        // write your code here
        if(n<=0 || edges==null) {
            return false;
        }
        if(edges.length!=n-1) {
            return false;
        }
        UnionFind uf = new UnionFind(n);
        for(int[] edge : edges) {
            int num1 = edge[0];
            int num2 = edge[1];
            uf.connect(num1, num2);
        }
        return uf.getCount()==1;
    }
}
```

<!-- ----------------------------- Jarjarbinks ----------------------------- -->
三种解法

1. BFS
2. DFS
3. UnionFind
这里给出BFS和DFS的解法
思路：
判断一个图是否是树有三个条件：

1. 联通性
2. 边数 = 节点数 - 1
3. 是否有环
另外根据图论：以上三条满足任意两条即可

1. 可以采用BFS或者DFS都不难，只要通过一个点可以遍历到所有点
2. 肯定选，白送的
3. 采用并查集，对于任意一个边，只要发现这条边的两个节点已经联通了，再加上当前边就构成闭环

```java
public class Solution {
    /**
     * @param n an integer
     * @param edges a list of undirected edges
     * @return true if it's a valid tree, or false
     */
    public boolean validTree(int n, int[][] edges) {
        if (n == 0) return false;
        if (edges.length != n - 1) return false;
        Map<Integer, Set<Integer>> graph = initializeGraph(n, edges);
        Set<Integer> hash = new HashSet<>();
        //bfs(0, graph, hash);
        dfs(0, graph, hash);
        return (hash.size() == n);
    }
    
    private void bfs(int x, Map<Integer, Set<Integer>> graph, Set<Integer> hash) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(x);
        hash.add(x);
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (Integer neighbor : graph.get(node)) {
                if (hash.contains(neighbor)) continue;
                queue.offer(neighbor);
                hash.add(neighbor);
            }
        }
    }
    
    private void dfs(int x, Map<Integer, Set<Integer>> graph, Set<Integer> hash) {
        hash.add(x);
        for (Integer neighbor : graph.get(x)) {
            if (hash.contains(neighbor)) continue;
            dfs(neighbor, graph, hash);
        }
    }
    
    private Map<Integer, Set<Integer>> initializeGraph(int n, int[][] edges) {
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new HashSet<Integer>());
        }
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        return graph;
    }
}
```