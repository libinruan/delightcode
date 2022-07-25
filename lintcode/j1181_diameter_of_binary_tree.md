from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

DSF: https://www.lintcode.com/problem/1181/solution/56987?fromId=164&_from=collection O(n) O(height)        
"""

class Solution:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        self.ans = 1
        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1


"""
方法一 https://www.lintcode.com/problem/1181/solution/19616?fromId=164&_from=collection
"""        
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
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


"""
方法二 https://www.lintcode.com/problem/1181/solution/19616?fromId=164&_from=collection
"""        
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

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
        
        longest[None] = 0
        diameter[None] = 0
        
        # 逆序遍历BFS序，并更新节点最长链和直径
        for i in range(len(bfs_order) - 1, -1, -1):
            node = bfs_order[i]
            
            left_longest, left_diameter = longest[node.left], diameter[node.left]
            right_longest, right_diameter = longest[node.right], diameter[node.right]
            
            longest[node] = max(left_longest, right_longest) + 1
            diameter[node] = max(left_diameter,
                                 right_diameter,
                                 left_longest + right_longest)
        
        return diameter[root]