# 描述
# 给定一个已经按绝对值升序排列的数组，找到两个数使他们加起来的和等于特定数。

# 函数应该返回这两个数的下标，index1必须小于index2。注意：数组的下标以0开始。

# 你不能对该数组进行排序。

# 挑战
# \mathcal{O}(n)O(n)的时间复杂度和\mathcal{O}(1)O(1)的额外空间复杂度



# 解题思路：用hashmap/dict做会很简单，传统2sum 加一句 if abs(target - nums[i]) < abs(nums[i]): continue 来避免不必要的查找
class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
    """
    def twoSumVII(self, nums, target):
        # write your code here

        find = {}
        result = []
        for i in range(len(nums)):
            if nums[i] in find:
                result.append([find[nums[i]], i])
            if abs(target - nums[i]) < abs(nums[i]):
                continue
            find[target - nums[i]] = i
        return result



# 那个nextLeft和nextRight是什么鬼？
# 这题是展示Python语言语法简单表达力强大的机会。平常心对待，双指针，左指针从最小值开始，右指针从最大值开始，指针下标相向靠拢。
class Solution:
    
    def twoSumVII(self, nums, target):
        n = len(nums)
        if n < 2: return []
        
        def ascending():
            lo = min(range(n), key = nums.__getitem__)
            for i in range(lo, -1, -1):
                if nums[i] <= 0:
                    yield i
            for i in range(1, n):
                if nums[i] > 0:
                    yield i 
        
        def descending():
            hi = max(range(n), key = nums.__getitem__)
            for j in range(hi, -1, -1):
                if nums[j] >= 0:
                    yield j
            for j in range(1, n):
                if nums[j] < 0:
                    yield j
        
        up, down, output = ascending(), descending(), []
        i, j = next(up), next(down)
        while nums[i] < nums[j]:
            if nums[i] + nums[j] < target:
                i = next(up)
            elif nums[i] + nums[j] > target:
                j = next(down)
            else:
                output.append((min(i, j), max(i, j)))
                i, j = next(up), next(down)
        return output



# Official
class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
    """
    def nextleft(self, left, nums):
        n = len(nums)
        if (nums[left] < 0):
            for i in range(left - 1, -1, -1):
                if (nums[i] < 0):
                    return i
            for i in range(n):
                if (nums[i] >= 0):
                    return i
            return -1
        for i in range(left + 1, n):
            if (nums[i] >= 0):
                return i
        return -1
    def nextright(self, right, nums):
        n = len(nums)
        if (nums[right] > 0):
            for i in range(right - 1, -1, -1):
                if (nums[i] > 0):
                    return i
            for i in range(n):
                if (nums[i] <= 0):
                    return i
            return -1
        for i in range(right + 1, n):
            if (nums[i] <= 0):
                return i
        return -1
    def twoSumVII(self, nums, target):
        # write your code here
        n = len(nums)
        if (n == 0):
            return []
        left = 0
        right = 0
        for i in range(n):
            if (nums[i] > nums[right]):
                right = i
            if (nums[i] < nums[left]):
                left = i
        ans = []
        while (nums[left] < nums[right]):
            if (nums[left] + nums[right] < target):
                left = self.nextleft(left, nums)
                if left == -1:
                    break
            elif (nums[left] + nums[right] > target):
                right = self.nextright(right, nums)
                if right == -1:
                    break
            else:
                tmp = [left, right]
                if left > right:
                    tmp[0], tmp[1] = tmp[1], tmp[0]
                ans.append(tmp)
                left = self.nextleft(left, nums)
                if left == -1:
                    break
        return ans