# ansewr 1
# https://www.lintcode.com/problem/249/solution/44585
import bisect

class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        tmp = []
        ans = []
        for x in A:
            idx = bisect.bisect_left(tmp, x)
            ans.append(idx)
            tmp.insert(idx, x)
        return ans



# answer 2
# https://www.lintcode.com/problem/249/solution/19721
class Solution:
    def countOfSmallerNumberII(self, A):
        for i, item in enumerate(A):
            group_num = item // N
            item_num = item % N
            group_sum, item_sum = 0, 0
            #0~输入数字范围内的group总和
            for j in range(group_num):
                if j in nums_group:
                    group_sum += nums_group[j]
        #输入数字当前group 内，小于输入数字的总和
            for j in range(group_num * N, group_num * N + item_num):
                if j in nums:
                    item_sum += nums[j]
            res.append(group_sum + item_sum)
        #更新hash表
            nums[group_num * N + item_num] = nums.get(group_num * N + item_num, 0) + 1
            nums_group[group_num] = nums_group.get(group_num, 0) + 1

        return res        



# answer 3
# Fenwick Tree (Binary Indexed Tree)
# https://www.lintcode.com/problem/249/solution/21050
class BITree:
    def __init__(self, num_range):
        self.bit = [0] * (num_range + 1)

    def lowbit(self, x):
        return x & (-x)
        
    def update(self, index, val):
        i = index + 1 
        while i < len(self.bit):
            self.bit[i] += val
            i += self.lowbit(i)
    
    def getPresum(self, index):
        presum = 0
        i = index + 1 
        while i > 0:
            presum += self.bit[i]
            i -= self.lowbit(i)
        
        return presum
        
class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        # write your code here
        if not A:
            return []
            
        smallest = sys.maxsize
        largest = -sys.maxsize
        for a in A:
            smallest = min(smallest, a)
            largest = max(largest, a)

        #bit = BITree(10000)
        bit = BITree(largest - smallest + 1)
        
        result = []
        for a in A:
            #result.append(bit.getPresum(a - 1))
            #bit.update(a, 1)
            result.append(bit.getPresum(a - smallest - 1))
            bit.update(a - smallest, 1)
            
        return result        



# answer 4
# https://www.lintcode.com/problem/249/solution/19952
class Block:
    def __init__(self):
        self.total = 0
        self.counter = {}
        
        
class BlockArray:
    def __init__(self, max_value):
        self.blocks = [
            Block()
            for _ in range(max_value // 100 + 1)
        ]
    
    def count_smaller(self, value):
        count = 0
        block_index = value // 100
        for i in range(block_index):
            count += self.blocks[i].total
        
        counter = self.blocks[block_index].counter
        for val in counter:
            if val < value:
                count += counter[val]
        return count
        
    def insert(self, value):
        block_index = value // 100
        block = self.blocks[block_index]
        block.total += 1
        block.counter[value] = block.counter.get(value, 0) + 1


class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        if not A:
            return []

        block_array = BlockArray(10000)
        results = []
        for a in A:
            count = block_array.count_smaller(a)
            results.append(count)
            block_array.insert(a)
        return results        