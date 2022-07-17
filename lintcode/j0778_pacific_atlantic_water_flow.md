方法：深度优先搜索
雨水的流动方向是从高到低，每个单元格上的雨水只能流到高度小于等于当前单元格的相邻
单元格。从一个单元格开始，通过搜索的方法模拟雨水的流动，则可以判断雨水是否可以从
该单元格流向海洋。

如果直接以每个单元格作为起点模拟雨水的流动，则会重复遍历每个单元格，导致时间复杂
度过高。为了降低时间复杂度，可以从矩阵的边界开始反向搜索寻找雨水流向边界的单元
格，反向搜索时，每次只能移动到高度相同或更大的单元格。

由于矩阵的左边界和上边界是太平洋，矩阵的右边界和下边界是大西洋，因此从矩阵的左边
界和上边界开始反向搜索即可找到雨水流向太平洋的单元格，从矩阵的右边界和下边界开始
反向搜索即可找到雨水流向大西洋的单元格。

可以使用深度优先搜索实现反向搜索，搜索过程中需要记录每个单元格是否可以从太平洋反
向到达以及是否可以从大西洋反向到达。反向搜索结束之后，遍历每个网格，如果一个网格
既可以从太平洋反向到达也可以从大西洋反向到达，则该网格满足太平洋和大西洋都可以到
达，将该网格添加到答案中。

```python
# O(mn), O(mn)
# https://www.lintcode.com/problem/778/solution/58587?fromId=164&_from=collection
class Solution:
    def pacific_atlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        def search(starts: List[tuple[int, int]]) -> set[tuple[int, int]]:
            visited = set()
            def dfs(x: int, y: int):
                if (x, y) in visited:
                    return
                visited.add((x, y))
                for nx, ny in ((x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)):
                    if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] >= matrix[x][y]:
                        dfs(nx, ny)
            for x, y in starts:
                dfs(x, y)
            return visited

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)]
        return list(map(list, search(pacific) & search(atlantic)))
```

方法：广度优先搜索
雨水的流动方向是从高到低，每个单元格上的雨水只能流到高度小于等于当前单元格的相邻
单元格。从一个单元格开始，通过搜索的方法模拟雨水的流动，则可以判断雨水是否可以从
该单元格流向海洋。

如果直接以每个单元格作为起点模拟雨水的流动，则会重复遍历每个单元格，导致时间复杂
度过高。为了降低时间复杂度，可以从矩阵的边界开始反向搜索寻找雨水流向边界的单元
格，反向搜索时，每次只能移动到高度相同或更大的单元格。

由于矩阵的左边界和上边界是太平洋，矩阵的右边界和下边界是大西洋，因此从矩阵的左边
界和上边界开始反向搜索即可找到雨水流向太平洋的单元格，从矩阵的右边界和下边界开始
反向搜索即可找到雨水流向大西洋的单元格。

反向搜索可以使用广度优先搜索实现。搜索过程中同样需要记录每个单元格是否可以从太平
洋反向到达以及是否可以从大西洋反向到达。反向搜索结束之后，遍历每个网格，如果一个
网格既可以从太平洋反向到达也可以从大西洋反向到达，则该网格满足太平洋和大西洋都可
以到达，将该网格添加到答案中。

```python
# O(mn), O(mn)
# https://www.lintcode.com/problem/778/solution/58591?fromId=164&_from=collection
class Solution:
    def pacific_atlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        from collections import deque
        m, n = len(matrix), len(matrix[0])

        def bfs(starts: List[tuple[int, int]]) -> set[tuple[int, int]]:
            q = deque(starts)
            visited = set(starts)
            while q:
                x, y = q.popleft()
                for nx, ny in ((x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)):
                    if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] >= matrix[x][y] and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))
            return visited

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)]
        return list(map(list, bfs(pacific) & bfs(atlantic)))
```