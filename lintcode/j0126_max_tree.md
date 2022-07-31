# monotonic stack
![](https://i.postimg.cc/tJ06wMjB/Jiuzhang-vip-30days.png)
```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
 
class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        n = len(A)
        stack = [0] * n
        cnt = -1
        pNodes = []
        for i in range(0, n):
            node = TreeNode(A[i])
            pNodes.append(node)
            if cnt > -1 and A[stack[cnt]] < A[i]:
                # 如果栈中有元素且元素小于当前元素，则弹出栈内元素
                while cnt > -1 and A[stack[cnt]] < A[i]:
                    cnt -= 1
                # 弹出的最后一个元素就是当前元素的左儿子
                pNodes[i].left = pNodes[stack[cnt + 1]]
            if cnt > -1 and A[stack[cnt]] > A[i]:
                # 如果栈内有元素且栈顶元素大于当前元素
                # 那么当前元素是栈顶元素的右儿子
                pNodes[stack[cnt]].right = pNodes[i]
            # 压入当前元素
            cnt += 1
            stack[cnt] = i
        return pNodes[stack[0]]
```

# monotonic stack
这道题的难点其实不是单调递减栈，我个人觉得是如何理解什么时候node放到左子树，什么时候放到右子树。
用cur表示TreeNode(A[i])
用pre表示stack.pop()的node
pre是cur从栈中踢出的node，这是我们值到 stack[-1].val > pre.val < cur.val.
这是我们要决定如何放置pre，stack[-1].val和cur.val, 谁小谁成为pre的parent
建树的原则就是，

如果cur是最大值，就把已经存在的树作为cur的左孩子
如果cur不是最大值，就把pre作为已经存在的树的右孩子。

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        # write your code here
        if not A:
            return None
        
        stack = []
        for index, num in enumerate(A + [sys.maxsize]):
            cur = TreeNode(num)
            # 单调递减栈
            while stack and stack[-1].val < cur.val:
                pre = stack.pop()
                # stack[-1].val pre.val cur.val
                # if stack[-1].val < cur.val, stack[-1] will be the root of pre
                if stack and stack[-1].val < cur.val:
                    stack[-1].right = pre
                # otherwise, cur will the root of the existed whole tree,
                else:
                    cur.left = pre 
                    
            stack.append(cur)
            
        # the top of stack is sys.maxsize
        return stack[-1].left
```

# monotonic stack
使用九章算法强化班中讲过的单调栈。另外一种比较简洁的写法。

考点：

数据结构设计
树的调整
单调栈
题解：
利用数组实现基本数据结构的调整，当前遍历到的数字比stk中的最后一个大时，将stk中的最后一个数字转变为当前节点的左子树，循环调整至stk为空或者stk中的最后节点值大于新节点的值。如果stk不为空，说明stk中的最后一个节点值大于新节点值，则将新节点设为stk中的最后一个节点的右子树，将新节点存入stk。

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        stack = []
        for num in A:
            node = TreeNode(num)		#新建节点
            while stack and num > stack[-1].val:		#如果stk中的最后一个节点比新节点小
                node.left = stack.pop()					#当前新节点的左子树为stk的最后一个节点
                
            if stack:									#如果stk不为空
                stack[-1].right = node					#将新节点设为stk最后一个节点的右子树
                
            stack.append(node)

        return stack[0]
```

# monotonic stack + BFS?
Python, 單調棧 without if else loop
棧維護從大到小的元素。
題意，array裡大元素(self)，左邊的是self.left，右邊的是self.right。
從而可知棧左邊的self.right是棧右邊的元素，因為題意。遇到更大的incoming node時，為了棧維護的特性，我們知道棧裡更小的元素都是incoming node的self.left（因為更小）。把棧裡的元素整理出來，然後再添加incoming node以滿足棧的特性。
```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    6 4 20
    
    """
    def maxTree(self, A):

        stack = [] # mono decreasing
        for num in A:

            node = TreeNode(num)
            rightNode = None
            while stack and stack[-1].val < num:
                prevNode = stack.pop()
                prevNode.right = rightNode
                rightNode = prevNode
            node.left = rightNode
            stack.append(node)
        
        # remaining mono decrasing order
        while len(stack) > 1:
            node = stack.pop()
            stack[-1].right = node

        return stack[0]
```


# monotonic stack

```python
参考九章-小原的解释，维护一个单调递减栈。

在压入栈的过程中，一个元素作为节点时的左儿子也就是左半边最大的值，是这个元素被压入栈时，栈弹出的最后一个元素；而右儿子也就是右半边最大的值，是这个元素的上面一个元素，因为递减的单调栈是从底部往顶部依次减小的。最后留在栈顶的元素即为root。

具体实现用了一个dict存每个下标对应的node

def maxTree(self, A):
        # write your code here
        n = len(A)
        if n == 0:
            return None
        nodes = {i: TreeNode(A[i]) for i in range(n)}
        stack = []
        for i in range(n):
            left = -1
            while stack and A[stack[-1]] <= A[i]:
                left = stack.pop()
            if left != -1:
                nodes[i].left = nodes[left]
            if stack:
                nodes[stack[-1]].right = nodes[i]
            stack.append(i)
        return nodes[stack[0]]
```