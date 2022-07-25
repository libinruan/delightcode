# method 1
class Solution:
    def canJump(self, A):
        l = len(A)
        dp = [1] + [0]*(l-1)
        for i in range(l):
            if dp[i] is 0:
                continue
            for j in range(A[i]):
                if i+j+1 < l:
                    dp[i+j+1] = 1
        return dp[-1] == 1

# method 2
'''
贪心方法， 时间复杂度O（N），空间复杂度O（1）如果可以到达某个位置，那么之前的位
置一定都可以到达。初始华最远位置为0，遍历数组更新最远右边界即可。
'''
class Solution:
    def canJump(self, arr):
        res, length = 0, len(arr)
        if length == 0:							  # 剪枝提前判断输出
            return  False
        elif length == 1:
            return True
            
        for index in range(length):
            if index <= res:					   #可以跳到index处，则判断并更新最大值信息
                res = max(res, index + arr[index])
            else:
                return False	                   #说明无法跳到index位置，肯定不能到最后位置，所以直接False
        return res >= length - 1

# method 3
'''
greedy method, beats 100%, use maxJump, if maxJump is greater than len(A), no need to iterate the rest.
'''
class Solution:
    def canJump(self, A):
        if len(A) == 0:
            return 0
        maxJump, i = A[0], 0
        while i < len(A):
            if maxJump >= len(A) - 1:
                return True
            if maxJump == i :
                return False
            if i < maxJump:
                maxJump = max(i+A[i], maxJump)
                i += 1

        return False        