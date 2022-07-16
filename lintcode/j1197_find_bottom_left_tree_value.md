
这题有2个做法，一是宽度优先搜索，用每层的第一个节点来更新答案。二是深度优先搜
索，当遇到一个节点的深度大于目前维护的最大深度时用这个节点来更新答案。

1. 使用宽度优先搜索bfs，用每层的第一个节点更新Ans。时间复杂度O(n)
2. 使用深度优先搜索dfs，当我们第一次访问一个深度为depth的节点x（之前只访问过深度小于depth的节点）时，x一定是depth深度的最左节点，用这个节点更新Ans。即我们维护一个最大深度，当遍历到一个点的深度大于最大深度时，用这个节点来更新答案，并更新最大深度即可。时间复杂度O(n)。

```python
class Solution:
    """
    @param root: a root of tree
    @return: return a integer
    """
    def findBottomLeftValue(self, root):
        # write your code here
        self.max_level = 0
        self.val = None
        self.helper(root, 1)
        return self.val
        
    def helper(self, root, level):
        if not root: return
        if level > self.max_level:
            self.max_level = level
            self.val = root.val
        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)
```        

```python
class Solution:
    """
    @param root: a root of tree
    @return: return a integer

    bfs 分层遍历法
    """
    def findBottomLeftValue(self, root):
        # write your code here
        queue = [root] 
        while queue: 
          next_queue = [] 
          for i in range(len(queue)): 
            node = queue[i] 
            if node.left is not None: 
              next_queue.append(node.left) 
            if node.right is not None: 
              next_queue.append(node.right) 
          if not next_queue: 
            return queue[0].val 
          queue = next_queue
        return -1 
```