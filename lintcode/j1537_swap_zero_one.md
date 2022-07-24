question: https://www.lintcode.com/problem/1537/

# answer 1
解题思路

只需要从前往后，考虑当前的"0"前面有多少个"1"，比如当前"0"前面有3个"1"，则这个"0"需要至少3次移动到左侧，使得其左侧没有"1"，即最终结果累加3，遍历数组即可。

```java
    public class Solution {
        /**
        * @param nums: an Integer array
        * @return: return the minimum number of swaps.
        */
        public int SwapZeroOne(int[] nums) {
            // Write your code here
            int cnt = 0, res = 0;
            for (int num : nums) {
                if (num == 1) {
                    cnt++;
                } else {
                    res += cnt;
                }
            }
            return res;
        }
    }
```



# answer 2
解题思路
双指针，一个记录当前的0的位置，另外一个扫描下一个0的位置。

```java
class Solution {
public:
    /**
     * @param nums: an Integer array
     * @return: return the minimum number of swaps.
     */
    int SwapZeroOne(vector<int> &nums) {
        // Write your code here

        //从左边和从右边swap的操作数目是一样的，只需要计算一侧的数据即可
        //计算左边0的个数，就能知道当前的1需要移动到的位置，与当前位置的差值，就是swap的次数。累加起来就是答案
        int count = 0;//left side 0's count
        int n = nums.size();
        int ret = 0;

        for (int i = 0; i < n; i++){
            if (nums[i] == 0){
                ret += i-count;
                count++;
            }
        }
        return ret;
    }
};

```



# answer 3
面向双指针
```python
class Solution:
    """
    @param nums: an Integer array
    @return: return the minimum number of swaps.
    """
    def SwapZeroOne(self, nums):
        # Write your code here
        count = 0
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] > nums[right]:
                count += right - left
                right -= 1
                left += 1
            
            if nums[left] == 0:
                left += 1

            if nums[right] == 1:
                right -= 1

        return count
```



# answer 4

```python
class Solution:
    """
    @param nums: an Integer array
    @return: return the minimum number of swaps.
    """
    def SwapZeroOne(self, nums):
        # Write your code here
        if not nums:
            return 0
        
        ans = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] == 0:
                left += 1
            while left <= right and nums[right] == 1:
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                ans += right - left

                left += 1
                right -= 1

        return ans 
```