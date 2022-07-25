# answer 1
# https://www.lintcode.com/problem/122/solution/17179
# https://www.lintcode.com/problem/122/solution/17287
class Solution:
    
    def largestRectangleArea(self, heights) -> int:
        
        heights = [0] + heights + [0]  #  因為假設一個左邊界和一個右邊界方便stack計算。
        stack, max_area = [], 0
        
        for hi_index, height in enumerate(heights):
            
            while stack and height < heights[stack[-1]]:
                
                popped_index = stack.pop()
                lo_index = stack[-1] + 1 

                area = heights[popped_index] * (hi_index - lo_index)
                max_area = max(max_area, area)
            
            stack.append(hi_index)
        
        return max_area