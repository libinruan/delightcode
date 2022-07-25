"""
DP - https://www.lintcode.com/problem/4/solution/56274?fromId=164&_from=collection
O(n), O(n)
"""
class Solution:
    def nth_ugly_number(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        
        return dp[n]


"""
min heap - https://www.lintcode.com/problem/4/solution/56263?fromId=164&_from=collection
O(nlogn), O(n)
"""        
class Solution:
    def nth_ugly_number(self, n: int) -> int:
        import heapq
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)