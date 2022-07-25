# Two pointers
url: https://www.lintcode.com/problem/610/solution/19925
```python
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        target = abs(target) # 让target为正数
        j = 0
        for i in range(len(nums)):
            j = max(i + 1, j)
            while j < len(nums) and nums[j] - nums[i] < target:
                j += 1 # 指针右移到num[j]>=num[i]
            if j > len(nums):
                break # 防止指针越界
            if nums[j] - nums[i] == target: # 找到答案
                return [nums[i],nums[j]]
        return [-1,-1]
```

url: https://www.lintcode.com/problem/610/solution/32911
```java
public class Solution {
    /**
     * @param nums: an array of Integer
     * @param target: an integer
     * @return: [num1, num2] (num1 < num2)
     */
    public int[] twoSum7(int[] nums, int target) {
        // write your code here
        if (nums == null || nums.length < 2) {
            return new int[]{};
        }
        int[] res = new int[2];
        int i = 0;
        int j = 1;
        target = Math.abs(target);
        while (i < j && j < nums.length) {
            int diff = nums[j] - nums[i];
            if (diff == target) {
                res[0] = nums[i];
                res[1] = nums[j];
                return res;
            } else if (diff < target) {
                j++;
            } else {
                i++;
                if (i == j) {
                    j++;
                }
            }
        }
        return res;
    }
}
```