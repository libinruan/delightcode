from typing import List
from collections import namedtuple

class Solution:
		
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        # approach 1. hashmap
        # t(n) = O(n)
        # s(n) = O(n)
        
        num_to_index = dict()
        for i in range(len(numbers)):
                if target - numbers[i] in num_to_index:
                        return (num_to_index[target - numbers[i]], i)
                num_to_index[numbers[i]] = i
        return []

        # loop over the input array; the loop counter takes on a value in each iteration.
        # if the difference after subtracting the loop counter value from the target in the dictionary already,
        # then we found and return the Solution.
        # else we put the loop counter value in the dictionary.Arith  

    def two_sum_v2(self, numbers: List[int], target: int) -> List[int]:
        # approach 2. two pointers
        # t(n) = O(n logn)
        # s(n) = O(n)

        num = sorted([(val, idx) for (idx, val) in enumerate(numbers)])
        start, end = 0, len(numbers) - 1
        while start < end:
            if num[start][0] + num[end][0] == target:
                return sorted([num[start][1], num[end][1]])
            if num[start][0] + num[end][0] > target:
                end -= 1
            else:
                start += 1
        return []


        # sort the input array by value in [(val1, idx1), (val2, idx2), ...]
        # left and right pointers
        # walking toward each other
        # (1) if sum < target, move left pointer to right by one Step
        # (2) if ... > ......, .... right ... ... ..left .........
        # until left pointer meets right pointers
        # if no answer is found, return emtpy list.