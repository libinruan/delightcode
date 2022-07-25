"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

Recursive solution is trivial, could you do it iteratively?
"""

class Solution:
    """
    @param root: the tree
    @return: pre order of the tree
    """
    def preorder(self, root):
        # write your code here
        if root is None:
            return []
        
        stack, output = [root, ], []            
        while stack:
            root = stack.pop()
            output.append(root.label)
            stack.extend(root.neighbors[::-1])
                
        return output

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

DDBear: https://www.lintcode.com/problem/1526/solution/19302?fromId=164&_from=collection         
"""

# 方法一
class Solution1:
    """
    @param root: the tree
    @return: pre order of the tree
    """
    def preorder(self, root: UndirectedGraphNode) -> List[int]:
        if root is None:
            return []

        result = [root.label]
        
        for subtree in root.neighbors:
            for x in self.preorder(subtree):
                result.append(x)
        
        return result

# 方法二
class Solution:
    """
    @param root: the tree
    @return: pre order of the tree
    """
    def preorder(self, root: UndirectedGraphNode) -> List[int]:
        if root is None:
            return []

        stack = [root]
        result = []
        
        while stack:
            # 取出栈顶元素
            node = stack.pop()
            result.append(node.label)
            # 将所有子节点逆序加入栈中
            stack.extend(node.neighbors[::-1])
        
        return result
