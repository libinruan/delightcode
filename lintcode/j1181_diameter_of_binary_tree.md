# DFS
- WHY USES GLOBAL VARIABLES? The reason is that a nested function can access the variable without specifying it as one of the function's arguments. 
```python
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
```

DSF: https://www.lintcode.com/problem/1181/solution/56987?fromId=164&_from=collection 

O(n) O(height)        

```python
class Solution:
    def diameter_of_binary_tree_1(self, root: TreeNode) -> int:
        # Method 1. class attribute
        self.ans = 0
        def depth(node):  # the DFS helper function: the depth of node (the input).
            if not node:
                return 0
            max_height_left = depth(node.left)
            max_height_right = depth(node.right)
            self.ans = max(self.ans, max_height_left + max_height_right)
            return max(max_height_left, max_height_right) + 1

        depth(root)
        return self.ans

    def diameter_of_binary_tree_2(self, root: TreeNode) -> int:
        # Method 2. global variable
        ans = [0]
        def depth(node):  # the DFS helper function
            if not node:
                return 0
            max_height_left = depth(node.left)
            max_height_right = depth(node.right)
            ans[0] = max(ans[0], max_height_left + max_height_right)
            return max(max_height_left, max_height_right) + 1

        depth(root)
        return ans[0]       
```

Example: Use of global variables.
```python
class solution:
    def foo(self, input: int):
        global_variable = [0]
        def boo(some_variable):  # we don't need to explicitly pass the global variable into the nested function.
            return some_variable + global_variable[0]
        return boo(input)
```


```python
class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameter_of_binary_tree_3(self, root):
        _, diameter = self.helper(root)
        return diameter
    
    # 返回最长的单链的长度和子树的直径
    def helper(self, root):
        if root is None:
            return 0, 0
        
        left_longest, left_diameter = self.helper(root.left)
        right_longest, right_diameter = self.helper(root.right)
        
        longest = max(left_longest, right_longest) + 1
        diameter = max(left_diameter, 
                       right_diameter,
                       left_longest + right_longest)
        
        return longest, diameter
```

# BFS 
Official clean version
```
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        longest = {}
        diameter = {}
        queue = collections.deque()
        
        queue.append(root)
        
        bfs_order = []
        
        # 宽度优先搜索，获得BFS序
        while queue:
            node = queue.popleft()
            if node is None:
                continue
            bfs_order.append(node)
            queue.append(node.left)
            queue.append(node.right)
        
        longest[None] = 0   # [1] trick
        diameter[None] = 0  # [1] trick
        
        # 逆序遍历BFS序，并更新节点最长链和直径
        for i in range(len( ) - 1, -1, -1):
            node = bfs_order[i]
            
            left_longest, left_diameter = longest[node.left], diameter[node.left]
            right_longest, right_diameter = longest[node.right], diameter[node.right]
            
            longest[node] = max(left_longest, right_longest) + 1
            diameter[node] = max(left_diameter,asr
                                 right_diameter,
                                 left_longest + right_longest)
        
        return diameter[root]
```