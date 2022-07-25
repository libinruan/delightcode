# answer 1
# https://www.lintcode.com/problem/510/solution/17494
# 采用算法强化班中讲到的单调栈。
# 要做这个题之前先做直方图最大矩阵（Largest Rectangle in Histogram） 这个题。
# 这个题其实就是包了一层皮而已。一行一行的计算以当前行为矩阵的下边界时，最大矩阵是什么。
# 计算某一行为下边界时的情况，就可以转换为直方图最大矩阵问题了。
class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
            
        max_rectangle = 0
        heights = [0] * len(matrix[0])
        for row in matrix:
            for index, num in enumerate(row):
                heights[index] = heights[index] + 1 if num else 0
            max_rectangle = max(
                max_rectangle,
                self.find_max_rectangle(heights),
            )

        return max_rectangle

    def find_max_rectangle(self, heights):
        indices_stack = []
        max_rectangle = 0
        for index, height in enumerate(heights + [-1]):
            while indices_stack and heights[indices_stack[-1]] >= height:
                popped = indices_stack.pop(-1)
                left_bound = indices_stack[-1] if indices_stack else -1
                max_rectangle = max(
                    max_rectangle,
                    (index - left_bound - 1) * heights[popped],
                )
            indices_stack.append(index)
            print(indices_stack)
        
        return max_rectangle

# ansewr 2
# https://www.lintcode.com/problem/510/solution/19624
class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        n,m = len(matrix),len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):#每个位置上方有多少连续的1
            for j in range(m):
                if i == 0 and matrix[i][j]:
                    dp[i][j] = 1
                    continue
                if matrix[i][j]:
                   dp[i][j] = dp[i-1][j] + 1
        ans = 0
        for i in range(n):#把每一行作为底找最大矩形
            ans = max(ans,self.largestRectangleArea(dp[i][:]));
        return ans;
    def largestRectangleArea(self,height):
        stack = []
        height.append(0)
        Sum = 0
        i = 0
        while i < len(height):
            if stack == [] or height[i] > height[stack[len(stack) - 1]]:
                stack.append(i)
            else:
                tmp = stack.pop()
                if stack == []:
                    Sum = max(Sum,height[tmp] * i)
                else:
                    Sum = max(Sum,height[tmp] * (i - stack[len(stack) - 1] - 1))
                i -= 1#拿着右边界， 寻找左边界；
            i += 1
        return Sum     



# answer 3
# https://www.lintcode.com/problem/510/solution/62618
from typing import (
    List,
)

class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximal_rectangle(self, matrix: List[List[bool]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        def get_max_area(arr):
            arr = [-1] + arr + [-1]
            stack = []
            ans = float('-inf')
            for right, height in enumerate(arr):
                while stack and arr[stack[-1]] > height:
                    curr = stack.pop()
                    left = stack[-1]
                    ans = max(ans, (right - left - 1) * arr[curr])
                stack.append(right)
            arr = arr[1:-1]
            return 0 if ans == float('-inf') else ans
        
        n, m = len(matrix), len(matrix[0])
        arr = [0] * m
        ans = 0
        for row in matrix:
            for i, num in enumerate(row):
                arr[i] = arr[i] + 1 if num else 0
            ans = max(ans, get_max_area(arr))
        return ans