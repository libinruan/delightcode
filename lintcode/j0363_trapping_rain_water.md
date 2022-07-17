<!-- -------------------------------- 动态规划f -------------------------------- -->
O(N), O(N)
```python
from typing import (
    List,
)

class Solution:
    def trap_rain_water(self, heights: List[int]) -> int:
        if not heights: return 0
        sum = 0
        max_left = [0 for _ in heights]
        max_right = [0 for _ in heights]
        for i in range(1, len(heights) - 1):
            max_left[i] = max(max_left[i - 1], heights[i - 1])
        for i in range(len(heights) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], heights[i + 1])
        for i in range(1, len(heights) - 1):
            _min = min(max_left[i], max_right[i])
            if (_min > heights[i]): sum += _min - heights[i]
        return sum
```

<!-- ---------------------------------- 栈 ---------------------------------- -->
O(N), O(N)

```python
from typing import (
    List,
)

class Solution:
    def trap_rain_water(self, heights: List[int]) -> int:
        _sum = 0
        _stack = []
        current = 0
        while current < len(heights):
            while len(_stack) and heights[current] > heights[_stack[-1]]:
                h = heights[_stack.pop()]
                if not len(_stack): break
                distance = current - _stack[-1] - 1
                _min = min(heights[_stack[-1]], heights[current])
                _sum += distance * (_min - h)
            _stack.append(current)
            current += 1
        return _sum
```

<!-- --------------------------------- 双指针 --------------------------------- -->
O(N), O(1)
```python
from typing import (
    List,
)

class Solution:
    def trap_rain_water(self, heights: List[int]) -> int:
        if not heights: return 0
        _sum = 0
        max_left = 0
        max_right = [0 for _ in heights]
        for i in range(len(heights) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], heights[i + 1])
        for i in range(1, len(heights) - 1):
            max_left = max(max_left, heights[i - 1])
            _min = min(max_left, max_right[i])
            if (_min > heights[i]): _sum += _min - heights[i]
        return _sum
```    