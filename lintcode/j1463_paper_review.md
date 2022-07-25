# DP + Union Find
sol: https://www.lintcode.com/problem/1463/solution/29206

并查集 + 双序列型动态规划提取信息：pair里面的单词是两两相似，words1和words2可能
长度不一样，而且需要找最长公共相似序列。

基于pair联想到构件图，再bfs进行相似性查找，用最长公共子序列解决最长相似性问题。
但是每次bfs所耗费的时间比较长，最坏可能是全部找一遍。这里可以联想到，还可以用并
查集构建集合，这样能快速查找每个单词的root是否跟另一个相同。

```python
class Node :
    def __init__(self) :
        self.fa=[]
        for i in range(6200) :
             self.fa.append(i)
    def find(self,x) :
        if self.fa[x]==x :
            return x
        else :
            self.fa[x]=self.find(self.fa[x])
            return self.fa[x]
    def unity(self,x,y) :
        x=self.find(x)
        y=self.find(y)
        self.fa[x]=y
class Solution:
    """
    @param words1: the words in paper1
    @param words2: the words in paper2
    @param pairs: the similar words pair
    @return: the similarity of the two papers
    """
    def getSimilarity(self, words1, words2, pairs):
        # Write your code here
        ans=Node()
        cnt=0
        a=[]
        b=[]
        s={}
        a.append(0)
        b.append(0)
        for i in pairs:
            if s.__contains__(i[0])==0 :
                cnt+=1
                s[i[0]]=cnt
            if s.__contains__(i[1])==0 :
                cnt+=1
                s[i[1]]=cnt
            ans.unity(s[i[0]],s[i[1]])
        for i in words1 :
            if s.__contains__(i)==0: 
                cnt+=1
                s[i]=cnt
            a.append(s[i])
        for i in words2 :
            if s.__contains__(i)==0 : 
                cnt+=1
                s[i]=cnt
            b.append(s[i])
        dp=[[0]*1000 for i in range(1000)]
        for i in range(1,len(words1)+1) :
            for j in range(1,len(words2)+1) :
                x=ans.find(a[i])
                y=ans.find(b[j])
                if x==y :
                    dp[i][j]=dp[i-1][j-1]+1
                else :
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        res=dp[len(words1)][len(words2)]*2.0/(len(words1)+len(words2))
        return res
```

# DP + Union Finnd version 2
```python
from typing import (
    List,
)

# Method: Union Find + DP (LCS)
class UnionFind:
    def __init__(self):
        self.parent = dict()

    def find(self, value):
        if value not in self.parent:
            return None
        if self.parent[value] == value:
            return value
        self.parent[value] = self.find(self.parent[value])
        return self.parent[value]
    
    def add(self, value):
        if value not in self.parent:
            self.parent[value] = value

    def in_same_set(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b and root_a is not None

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_a] = root_b

class Solution:
    """
    @param words1: the words in paper1
    @param words2: the words in paper2
    @param pairs: the similar words pair
    @return: the similarity of the two papers
    """
    def get_similarity(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> float:
        
        ## Step_1: Union Find to construct connected graph
        uf = UnionFind()
        for w1, w2 in pairs:
            uf.add(w1)
            uf.add(w2)
            uf.union(w1, w2)
        
        ## Step_2: DP 
        # dp_1: state + dp_2: init 
        longest = 0
        dp = [[0 for _ in range(len(words2) + 1)] for _ in range(len(words1) + 1)]
        
        # dp_3: shift
        for i in range(1, len(words1) + 1):
            dp[i][0] = 0
            for j in range(1, len(words2) + 1):
                if words1[i - 1] == words2[j - 1] or uf.in_same_set(words1[i - 1], words2[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                longest = max(longest, dp[i][j])
        
        # dp_4: answer
        return 2.0 * longest / (len(words1) + len(words2))
```

# DP + Union Finnd version 3*
```python
from typing import (
    List,
)

class Solution:
    """
    @param words1: the words in paper1
    @param words2: the words in paper2
    @param pairs: the similar words pair
    @return: the similarity of the two papers
    """
    def get_similarity(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> float:
        # Write your code here

        father = {}
        def find(node):
            if node not in father:
                father[node] = node
                return node

            if father[node] == node:
                return node
            
            father[node] = find(father[node])
            return father[node]

        
        def union(node1, node2):
            
            father1 = find(node1)
            father2 = find(node2)

            if father1 != father2:
                father[father1] = father2
        
        for each in pairs:
            union(each[0], each[1])


        dp = {}
        for i in range(len(words1)+1):
            for j in range(len(words2)+1):

                if i == 0 or j == 0:
                    dp[(i,j)] = 0
                    continue

                if find(words1[i-1]) == find(words2[j-1]) :
                    dp[(i,j)] = dp[(i-1,j-1)] + 1
                else:
                    dp[(i,j)] = max(dp[(i-1,j)] , dp[(i,j-1)])

        
        return dp[ (len(words1), len(words2)) ]*2/( len(words1) + len(words2) )
```

# DP + Union Finnd version 4*
sol: https://www.lintcode.com/problem/1463/solution/36336

代码思路来自于糖糖https://www.lintcode.com/user/%E7%B3%96%E7%B3%96/
判断相似度我们需要建立并查集，注意相似度的传递性以及对称性：
分以下情况讨论：
若两单词具有相同的root: 我们认为已经在同一集合内，无需更改
若root不同，则归并到同一root下，此处按照str内置排序规则取较小的为root
接下来查重本体过程应用dynamic programming：
若当前位置相同，则当前最大值为上一位+1
若当前位置不同，则错一位取较大值，可以想象成删去或插入一个字母
最终答案按照给定公式计算即可。

```python
class Solution:
    """
    @param words1: the words in paper1
    @param words2: the words in paper2
    @param pairs: the similar words pair
    @return: the similarity of the two papers
    """
    def getSimilarity(self, words1, words2, pairs):
        
        # Initialize and connect the "similar" elements together 
        self.roots = {}
        for w1, w2 in pairs:
            self.union(w1, w2)

        # Use dynamic programming to solve
        l1, l2 = len(words1), len(words2)

        grid = [[0] * (l2+1) for i in (range(l1+1))]

        words1_roots = [self.find_root(word) for word in words1]
        words2_roots = [self.find_root(word) for word in words2]

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if words1_roots[i-1] == words2_roots[j-1]:
                    grid[i][j] = grid[i-1][j-1] + 1 
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1] *2 / (l1+l2)



    # Find the root of the current element
    def find_root(self, element):
        if element not in self.roots:
            self.roots[element] = element
            return element
        
        path = []
        while self.roots[element] != element:
            path.append(element)
            element = self.roots[element]

        for p in path:
            self.roots[p] = element
        return element

    # Combine two element in one root
    def union(self, a,b):
        root_a  = self.find_root(a)
        root_b  = self.find_root(b)
        
        if root_a == root_b:
            return

        rmin, rmax = min(root_a, root_b), max(root_a, root_b)
        self.roots[rmax] = rmin
```

# answer 5
sol:
首先想到dp。和最长公共子序列很相似。

刚开始想到直接建图，但是之后的查询是一个问题。因为要判断两个节点有没有关系。要遍
历整个图才行。一定会超时~所以就知道了并查集这么个东西~但是代码里面并没有用，而是
用set优化了查找图的部分。如果他们有关系，就都存储在一个hashSet中。这样查找的速度
就有提升了。

```java
public class Solution {
    /**
     * @param words1: the words in paper1
     * @param words2: the words in paper2
     * @param pairs: the similar words pair
     * @return: the similarity of the two papers
     */
    public float getSimilarity(List<String> words1, List<String> words2, List<List<String>> pairs) {
        // Write your code here
        float result = 0f;
        if(words1.size() == 0 || words2.size() == 0) {
            return result;
        }
        //当前所有的结合
        List<Set<String>> sets = new ArrayList<>();
        for(List<String> pair : pairs) {
            String key = pair.get(0);
            String value = pair.get(1);
            像集合中添加元素
            addValue(sets,key,value);
        }
        //dp部分
        int[][] dp = new int[words1.size() + 1][words2.size() + 1];
        for(int i = 1; i <= words1.size(); i++) {
            for(int j = 1; j <= words2.size(); j++) {
                if(find(sets,words1.get(i-1),words2.get(j-1)) || words1.get(i-1).equals(words2.get(j-1))) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                }else {
                    dp[i][j] = Math.max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        结果计算
        result = (dp[words1.size()][words2.size()]*2f)/(words1.size()+words2.size());
        return result;
    }
    //查找两个词是否有关系
    private boolean find(List<Set<String>> sets, String word1 ,String word2){
        for(Set<String> set :sets) {
            //如果一个集合包含两个词，表示有关系。如果包含任意一个但不包含另一个。则没有关系
            if(set.contains(word1) && set.contains(word2)) {
                return true;
            }
            if(set.contains(word1) || set.contains(word2)) {
                return false;
            }
        }
        return false;
    }
    //像集合中添加值
    private void addValue(List<Set<String>> sets,String key,String value ) {
        //记录包含词的集合索引
        List<Integer> delSet = new ArrayList<Integer>();
        //当前新集合
        Set<String> allSet  = new HashSet<String>();
        for(int i = 0;i < sets.size(); i++){
            if(sets.get(i).contains(key) || sets.get(i).contains(value)) {
            	delSet.add(i);
                //合并集合
                allSet.addAll(sets.get(i));
            }
        }
        Collections.sort(delSet);
        for(int i = delSet.size() - 1; i >=0 ;i--) {
            sets.remove(delSet.get(i).intValue());
        }
        allSet.add(key);
        allSet.add(value);
        sets.add(allSet);
    }
}
```