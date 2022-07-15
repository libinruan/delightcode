from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = -sys.maxsize - 1
        self.localMaxSum(root)
        return self.maxSum
    
# 0 ACCOUTING FOR POSSIBLE MAX VALUES FOUND IN LOCAL PAHTS EXCLUDING THE INPUT ROOT    
    def localMaxSum(self, node):
        if not node: return 0
# 1 WE IGNORE BRANCHES THAT CONTRIBURES NEGATIVE VALUES.
        l = max(0, self.localMaxSum(node.left))
        r = max(0, self.localMaxSum(node.right))     
# 2 THIS ARRANGEMENT CAN RETURN ONLY A SINGLE NODE IF BOTH THE BRANCHES CONTRIBURES NEGATIVE VALUES (WHICH MEET THE REQUEST OF QUESTION).        
        localSum = l + node.val + r
# 3 UPDATE THE GLOBAL SUM 
        self.maxSum = max(self.maxSum, localSum)
# 4 WHEN COMMUNICATING WITH PARENT NODE, ONLY RETURN THE BEST RESULT FROM "ONE" BRANCH ONLY    
        return max(l, r) + node.val

#%%
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.maxPath = float('-inf')
        
        def largest_path_ends_at(node):
            if node is None:
                return float('-inf')
            
            e_l = largest_path_ends_at(node.left)
            e_r = largest_path_ends_at(node.right)
            
            self.maxPath = max(self.maxPath, node.val + max(0, e_l) + max(0, e_r), e_l, e_r)
            
            return node.val + max(e_l, e_r, 0)
        
        largest_path_ends_at(root)
        return self.maxPath        

#%%
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        maxPath = [float('-inf')]
        
        def largest_path_ends_at(node, maxPath): # Li: list is a mutable object (even though its elemens are float which is immutable.)
            if node is None:
                return float('-inf')
            
            e_l = largest_path_ends_at(node.left, maxPath)
            e_r = largest_path_ends_at(node.right, maxPath)
            
            maxPath[0] = max(maxPath[0], node.val + max(0, e_l) + max(0, e_r), e_l, e_r)
            
            return node.val + max(e_l, e_r, 0)
        
        largest_path_ends_at(root, maxPath)
        return maxPath[0]   
