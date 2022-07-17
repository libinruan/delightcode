```python
from typing import (
    List,
)

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def max_profit(self, prices: List[int]) -> int:
        # 數組價格補索引 不可思議填極壞 迴圈指針由一始 最後出清空手回
        
        # at most twice
        m = 2  
        n = len(prices)
        prices = [0] + prices
        dp = [[[0 for _ in range(2)] for _ in range(m + 1)] for _ in range(n + 1)]    
        
        for i in range(m + 1):
            # impossible to have positions at date 0        
            dp[0][i][1] = -float('inf')  
        for i in range(n + 1):
            # impossible to have position with no transaction
            dp[i][0][1] = -float('inf')  
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # sell the stock held yesterday or remains hold nothing as yesterday.
                dp[i][j][0] = max(
                    dp[i - 1][j][0], dp[i - 1][j][1] + prices[i]) 
                # have a new tranction (stock purchasing) today
                dp[i][j][1] = max(
                    dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        # On the last date, the last position should end up with short position.
        return dp[-1][-1][0]
```        