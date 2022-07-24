# https://www.lintcode.com/problem/901/

# answer 1
# https://www.lintcode.com/problem/901/solution/16651
# 对令狐老师和其他同学的解法小小总结一下, O(h + k)的时间复杂度。h为树的高度，平均为logn。

# 【确认条件】
# （1）沟通BST的定义。
# （2）确认是否需要判断tree和k是否valid。
# （3）确认不会存在两个与target距离相等的值，否则输出list的时候还得判断哪一个放在前面。
# （4）确认k是否小于等于tree中的节点数（虽然解法中遇到这种情况会通过break跳出）。

# 【解题思路】
# （1）通过get_stacks()虚拟寻找target的插入位置，并将一路上经过的点根据值的大小分别放入prev_stack和next_stack。用两个栈的好处是：之后在实现get_next()和get_prev()的时候会相对简单一些，不需要像完整版BST iterator那么复杂。

# （2）实现get_next()，利用next_stack寻找next_value。
# 在一般的BST iterator中，寻找下一节点的算法是：如果当前点存在右子树，那么就是右子树中一直向左走到底的那个点；如果当前点不存在右子树，则对到达当前点的路径进行反向遍历（一直pop stack），寻找第一个（离当前点最近的）左拐的点。
# 然而在本题中，因为已经分离prev_stack和next_stack，所以在当前节点不存在右子树的情况下，当前节点在next_stack中的前一个位置自然就是要找的下一个点。因此代码中只需处理当前节点存在右子树时的情况，即先取当前节点的右子树，再一路向左走到底。

# （3）实现get_prev()，利用prev_stack寻找prev_value。
# 对get_next()的处理方式取反，即先取当前节点的左子树，再一路向右走到底。若不存在左子树，在pop出当前节点后，stack[-1]自然处于下一个prev节点的位置。

# （4）for循环k次，每次比较prev_stack和next_stack栈顶节点的值，把与target距离近的那个放进results中。

# 【实现要点】
# （1）实现get_stacks()的时候，在把节点分入两个栈的时候注意思考一下，别把大小写，左右子树弄反了。另外对于本题，不需要对root.val == target的情况专门处理。
# （2）实现get_next()和get_prev()注意细节（完整版BST iterator其实需要背诵，本题中再对其简化）。
# （3）比较大小的时候引入sys.maxsize作为异常情况处理。

# 【复杂度】
# 时间复杂度：O(h + k)，O(h)来自于对树的搜索，O(k)是获取k个结果。
# 空间复杂度：O(h)

class Solution:
    def closestKValues(self, root, target, k):
        results = []
        if root is None or k == 0:
            return results
        next_stack, prev_stack = self.get_stacks(root, target)
        
        for _ in range(k):
            if len(next_stack) == 0 and len(prev_stack) == 0:
                break
            next_diff = sys.maxsize if len(next_stack) == 0 else abs(next_stack[-1].val - target)
            prev_diff = sys.maxsize if len(prev_stack) == 0 else abs(prev_stack[-1].val - target)
            
            if next_diff < prev_diff:
                results.append(self.get_next(next_stack))
            else:
                results.append(self.get_prev(prev_stack))
                
        return results
    
    def get_stacks(self, root, target):
        next_stack, prev_stack = [], []
        while root:
            if root.val < target:
                prev_stack.append(root)
                root = root.right
            else:
                next_stack.append(root)
                root = root.left
                
        return next_stack, prev_stack
    
    def get_next(self, next_stack):
        value = next_stack[-1].val
        node = next_stack.pop().right 
        while node:
            next_stack.append(node)
            node = node.left
            
        return value
        
    def get_prev(self, prev_stack):
        value = prev_stack[-1].val
        node = prev_stack.pop().left     
        while node:
            prev_stack.append(node)
            node = node.right
            
        return value



# answer 2
# 使用类似于 Find K Closest Elements 的做法。先求得 inorder，然后再二分到一个接近的位置，然后 Two pointers 向两边走。
# 时间复杂度 O(n)
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        if root is None or k == 0:
            return []
            
        nums = self.get_inorder(root)
        left = self.find_lower_index(nums, target)
        right = left + 1
        results = []
        for _ in range(k):
            if self.is_left_closer(nums, left, right, target):
                results.append(nums[left])
                left -= 1
            else:
                results.append(nums[right])
                right += 1
        return results
        
    def get_inorder(self, root):
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        inorder = []
        
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inorder.append(stack[-1].val)

        return inorder
        
    def find_lower_index(self, nums, target):
        """
        find the largest number < target, return the index
        """
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
                
        if nums[end] < target:
            return end
        
        if nums[start] < target:
            return start
            
        return -1
        
    def is_left_closer(self, nums, left, right, target):
        if left < 0:
            return False
        if right >= len(nums):
            return True
        return target - nums[left] < nums[right] - target        



