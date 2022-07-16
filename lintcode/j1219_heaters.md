detailed solution: https://www.lintcode.com/problem/1219/solution/57062?fromId=164&_from=collection

方法：排序 + 双指针
```python
from typing import (
    List,
)
import bisect
class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def find_radius(self, houses: List[int], heaters: List[int]) -> int:
        # Write your code here
        ans = 0
        houses.sort()
        heaters.sort()
        j = 0
        for i, house in enumerate(houses):
            curDistance = abs(house - heaters[j])
            while j + 1 < len(heaters) and abs(houses[i] - heaters[j]) >= abs(houses[i] - heaters[j + 1]):
                j += 1
                curDistance = min(curDistance, abs(houses[i] - heaters[j]))
            ans = max(ans, curDistance)
        return ans
```

方法：排序 + 二分查找 I
detailed solution: https://www.lintcode.com/problem/1219/solution/57062?fromId=164&_from=collection
```python
from typing import (
    List,
)

import bisect
class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def find_radius(self, houses: List[int], heaters: List[int]) -> int:
        # Write your code here
        ans = 0
        heaters.sort()
        for house in houses:
            j = bisect.bisect_right(heaters, house)
            i = j - 1
            rightDistance = heaters[j] - house if j < len(heaters) else float('inf')
            leftDistance = house - heaters[i] if i >= 0 else float('inf')
            curDistance = min(leftDistance, rightDistance)
            ans = max(ans, curDistance)
        return ans
```

方法：排序 + 二分查找 II
```python
class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def find_radius(self, houses: List[int], heaters: List[int]) -> int:
        # Write your code here
        heaters.sort()
        heat_radius = 0
        for house in houses:
            radius = self.get_minimum_radius(house, heaters)
            heat_radius = max(heat_radius, radius)
        return heat_radius
    
    def get_minimum_radius(self, house, heaters):
        left, right = 0, len(heaters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if heaters[mid] < house:
                left = mid + 1
            elif heaters[mid] > house:
                right = mid - 1
            elif heaters[mid] == house:
                return 0

        m = max(heaters)
        if left <= len(heaters) - 1:
            left_distance = abs(heaters[left] - house)
            m = min(m, left_distance)
        if right >= 0:
            right_distance = abs(heaters[right] - house)
            m = min(m, right_distance)
        return m
```