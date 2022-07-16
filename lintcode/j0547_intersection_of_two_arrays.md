
> source: https://www.lintcode.com/problem/547/solution/19605?fromId=164&_from=collection

方法一：hashset
解题思路
使用两个集合解决这个问题。

首先，将nums1中的元素加入到集合set1中。

依次检查nums2中的元素是否在set1中，如果在，说明属于交集元素，加入到交集集合set2中。

遍历set2，把所有元素加入到数组res中，返回res。

复杂度分析
时间复杂度：O(m + n)，m和n分别表示nums1和nums2的长度。算法中对nums1和nums2分别进行遍历。

空间复杂度: O(max(n, m))，m表示nums1的长度。集合set1的长度最长为m，set2和res的长度不会超过set1。

```python
class Solution:
    def intersection(self, nums1, nums2):
        # 创建nums1的集合set1
        set1 = set(nums1)
        # 创建交集集合set2
        set2 = set()
        for num in nums2:
            if num in set1:
                set2.add(num)
        # 把set2的元素加入到res中
        res = []
        for num in set2:
            res.append(num)
        return res

```

方法二: 双指针
解题思路
首先，将nums1和nums2排序。

定义双指针i和j，分别指向两个数组。从前向后遍历寻找交集元素。

当nums1[i] < nums2[j]，i后移1位
当nums1[i] > nums2[j]，j后移1位
当nums1[i] == nums2[j]，把nums1[i]加入集合intersect，i后移1位，j后移1位
将集合intersect的元素加入res中

复杂度分析
时间复杂度：O(mlog(m)+nlog(n))，其中m和n分别是nums1和nums2长度。排序算法的时间复杂度是O(mlog(m)+nlog(n))，双指针扫描的复杂度是O(m + n)。

空间复杂度：O(1)，常量空间。

```python

class Solution:
    def intersection(self, nums1, nums2):
        res = []
        # 排序
        nums1.sort()
        nums2.sort()
        # 双指针遍历
        i, j = 0, 0
        intersect = set()
        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                intersect.add(nums1[i])
                i += 1
                j += 1
        res = []
        # 把intersect的元素加入到res中
        for num in intersect:
            res.append(num)
        return res
```


方法三：二分查找
解题思路
首先，将nums1排序。

对于nums2中的每个元素，在有序的nums1中进行二分查找，如果找到，加入intersect集合中。

将集合intersect的元素移入res中。

复杂度分析
时间复杂度：O(mlogm + nlogm)，m和n分别为nums1和nums2的长度。对nums1排序的时间复杂度是O(mlogm)，在nums1中搜索nums2所有元素的时间复杂度为O(nlogm)

空间复杂度：O(1)。常量空间。

```python
class Solution:
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """
    def intersection_3(self, nums1, nums2):
        # idea: binary search + hash set
        result = set()
        if len(nums1) > len(nums2):
            s_nums = nums2
            b_nums = nums1
        else:
            s_nums = nums1
            b_nums = nums2

        s_nums.sort()
        for num in b_nums:
            if self.binary_seach(s_nums, num):
                result.add(num)
        return list(result)


    def binary_seach(self, nums, target):
        if not nums or len(nums) == 0:
            return False

        start, end = 0, len(nums) -1
        while start + 1 < end:
            middle = start + (end - start) // 2

            if nums[middle] <= target:
                start = middle
            elif nums[middle] > target:
                end = middle

        if nums[end] == target or nums[start] == target:
            return True
        return False

```

```java
public class Solution {

    /**
     * @param nums1: an integer array
     * @param nums2: an integer array
     * @return: an integer array
     */

    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> intersect = new HashSet<>();
        // nums1排序
        Arrays.sort(nums1);
        // 在nums1中搜索nums2的每位元素，添加到intersect集合中
        for (int i = 0; i < nums2.length; i++) {
            if (intersect.contains(nums2[i])) {
                continue;
            }
            if (binarySearch(nums1, nums2[i])) {
                intersect.add(nums2[i]);
            }
        }
        // 把intersect的元素加入到res中
        int[] result = new int[intersect.size()];
        int index = 0;
        for (Integer num : intersect) {
            result[index++] = num;
        }
        return result;
    }
    private boolean binarySearch(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return false;
        }
        int start = 0, end = nums.length - 1;
        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;
            if (nums[mid] == target) {
                return true;
            }
            if (nums[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }
        if (nums[start] == target) {
            return true;
        }
        if (nums[end] == target) {
            return true;
        }
        return false;
    }
}
```
