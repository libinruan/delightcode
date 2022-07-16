"""
二分法，时间复杂度貌似可以降到O(log(min(m,n))) 相当于在数组A和B中各切一刀，比如分别记为aCut和bCut，
两把刀左边的数总共保持为(m+n)//2，A中的刀有m个位置，B中的刀有n个位置，但考虑到A和B的长度不一样，
所以有min(m,n)个位置，然后再二分，看刀的位置对不对，不对再调整

https://www.lintcode.com/problem/65/solution/18276?fromId=164&_from=collection
"""
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        self.totalLength = len(A) + len(B)
        if len(A) <= len(B):
            start = 0
            end = len(A)
        else:
            start = self.totalLength // 2 - len(B)
            end = self.totalLength // 2
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.compareOne(A, B, mid) and self.compareTwo(A, B, mid):
                return self.outputMedian(A, B, mid)
            if not self.compareOne(A, B, mid):
                end = mid
            else:
                start = mid
        if self.compareOne(A, B, start) and self.compareTwo(A, B, start):
            return self.outputMedian(A, B, start)
        return self.outputMedian(A, B, end)
        
    def compareOne(self, A, B, aCut):
        bCut = self.totalLength // 2 - aCut
        if aCut == 0 or bCut == len(B):
            return True
        if A[aCut - 1] <= B[bCut]:
            return True
        return False
        
    def compareTwo(self, A, B, aCut):
        bCut = self.totalLength // 2 - aCut
        if aCut == len(A) or bCut == 0:
            return True
        if A[aCut] >= B[bCut - 1]:
            return True
        return False
        
    def outputMedian(self, A, B, aCut):
        if self.totalLength % 2 == 1:
            return self.selectRight(A, B, aCut)
        return (self.selectRight(A, B, aCut) + self.selectLeft(A, B, aCut)) / 2
        
    def selectRight(self, A, B, aCut):
        bCut = self.totalLength // 2 - aCut
        if aCut == len(A):
            return B[bCut]
        if bCut == len(B):
            return A[aCut]
        return min(A[aCut], B[bCut])
        
    def selectLeft(self, A, B, aCut):
        bCut = self.totalLength // 2 - aCut
        if aCut == 0:
            return B[bCut - 1]
        if bCut == 0:
            return A[aCut - 1]
        return max(A[aCut - 1], B[bCut - 1])