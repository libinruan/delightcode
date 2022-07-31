# BFS
Sliding Puzzles: LintCode 794, 941, 950, LeetCode 773
这几道题就一个模板

用tuple做state， LintCode 3 x 3求步数那个会MLE

可以直接用tuple matrix做状态

slicing tuple得到的还是tuple

deque里面如果是 deque((1, 2, 3))会自动变成 deque([1, 2, 3])， 必须用deque([(1, 2, 3)])

divmod(13, 5) return 2, 3 即 （商，余数）

```python
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, board, board2):
        # Write your code here
        start = ''.join(str(board[i][j]) for i in range(3) for j in range(3))
        end = ''.join(str(board2[i][j]) for i in range(3) for j in range(3))
        
        if start == end:
            return 0
        
        queue = collections.deque([start])
        distances = {start : 0}
        
        while queue:
            state = queue.popleft()
            
            for next_state in self.getNext(state, distances):
                if next_state in distances:
                    continue

                distances[next_state] = distances[state] + 1
                if next_state == end:
                    return distances[next_state]
                
                queue.append(next_state)
        
        return -1
    
    
    def getNext(self, B, distances):
        
        next_states = []
        
        idx = B.find('0')
        row, col = divmod(idx, 3)
        
        for dr, dc in DIRECTIONS:
            next_row, next_col = row + dr, col + dc
            
            if not (0 <= next_row < 3 and 0 <= next_col < 3):
                continue
            
            C = list(B)
            next_idx = next_row * 3 + next_col
            C[idx], C[next_idx] = C[next_idx], C[idx]
            
            D = ''.join(C)
            if D not in distances:
                next_states.append(D)
        
        return next_states
```


# BFS
https://www.lintcode.com/problem/950/solution/26118
采用bfs或者dfs均可，这里需要可以采用压位的方法记录已经搜过的状态。
```python
import Queue
import copy
class Solution:
    """
    @param matrix: The 3*3 matrix
    @return: The answer
    """
    def hash(self, tmp):
        t = 0
        for i in tmp:
            t = t * 10 + i
        return t
    def bfs(self, mat, ans):
        if mat == ans :
            return "YES"
        hashans = self.hash(ans)
        visit = {}
        move = [[0,1],[0,-1],[1,0],[-1,0]]
        g = [[] for i in range(9) ]
        for i in range(3):
            for j in range(3):
                for k in range(4):
                    ti = i + move[k][0]
                    tj = j + move[k][1]
                    if (ti >= 0 and ti < 3 and tj >= 0 and tj < 3):
                        g[i * 3 + j].append(ti * 3 + tj)
        q = Queue.Queue()
        q.put(self.hash(mat))
        visit[self.hash(mat)] = 1
        while not q.empty():
            Front = q.get()
            tmp = []
            while(Front):
                tmp.append(Front % 10)
                Front = Front // 10
            if(len(tmp) == 8):
                tmp.append(0)
            tmp = tmp[::-1]

            for pos in range(9):
                if(tmp[pos] == 0):
                    break
            for i in g[pos]:
                tmp[pos], tmp[i] = tmp[i], tmp[pos]
                hashvalue = self.hash(tmp)
                if hashvalue == hashans:
                    return "YES"
                if hashvalue not in visit:
                    visit[hashvalue] = 1
                    q.put(hashvalue)
                tmp[pos], tmp[i] = tmp[i], tmp[pos]
                    
        return "NO"
                    
    def  jigsawPuzzle(self, matrix):
        # Write your code here
        ansmat = [[1,2,3],[4,5,6],[7,8,0]]
        ans , mat = [], []
        for i in ansmat:
            for j in i:
                ans.append(j)
        for i in matrix:
            for j in i:
                mat.append(j)
        return self.bfs(mat, ans)
```

# BFS II
复杂度供参考。

因为有visited，可以保证棋盘的每种情况只出现一次，也就是9个数字的组合，最多 O(9!) 次bfs迭代，每次迭代消耗 O(9) 的时间来处理字符串。

空间，保存了 9! 种棋盘状态，O(9!) * 每个状态的存储空间。

FYI：
0每次可以移动4个方向，按照这种考虑的话时间复杂度是 O(9*4^9)。

time: O(9*9!)
space: O(Space*9!)
```python
class Solution:
    """
    @param matrix: The 3*3 matrix
    @return: The answer
    """
    def  jigsawPuzzle(self, matrix):
        # Write your code here
        
        """
        time: O(9*9!)
        space: O(9!)
        """
        
        # found zero point
        # do bfs
        from collections import deque
        q = deque([''.join([''.join([str(v) for v in r]) for r in matrix])])
        visited = set()
        while q:
            mat_str = q.pop()
            if mat_str == '123456780':
                return 'YES'
            
            zero = mat_str.find('0')
            for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                row, col = zero // 3 + dr, zero % 3 + dc

                if 0<=row<3 and 0<=col<3:
                    mat_new = list(mat_str)
                    mat_new[zero], mat_new[3*row+col] = mat_new[3*row+col], mat_new[zero]
                    mat_new = ''.join(mat_new)

                    if mat_new not in visited:
                        visited.add(mat_new)
                        q.appendleft(mat_new)
        return 'NO'
```        
