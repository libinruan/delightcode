# trie + DFS
tire + dfs。
字典树用于前缀查找。
dfs用于搜索，
找到单词时搜索下一个单词
没有搜索到单词时，四方向遍历（回溯 + 标记）
```python
class TrieNode(object):
    def __init__(self, value=0):
        self.value = value
        self.isWord = False
        self.children = collections.OrderedDict()
    #建树
    @classmethod
    def insert(cls, root, word):
        p = root
        for c in word:
            child = p.children.get(c)
            if not child:
                child = TrieNode(c)
                p.children[c] = child
            p = child

        p.isWord = True


class Solution:
    # @param {char[][]} board a list of lists of char
    # @param {str[]} words a list of string
    # @return {int} an integer
    def boggleGame(self, board, words):
        # Write your code here
        self.board = board
        self.words = words
        self.m = len(board)
        self.n = len(board[0])
        self.results = []
        self.temp = []
        self.visited = [[False for _ in xrange(self.n)] for _ in xrange(self.m)]
        
        self.root = TrieNode()
        for word in words:
            TrieNode.insert(self.root, word)
        
        self.dfs(0, 0, self.root)
                
        return len(self.results)
    #dfs查找单词
    def dfs(self, x, y, root):
        for i in xrange(x, self.m):
            for j in xrange(y, self.n):
                paths = []
                temp = []
                self.getAllPaths(i, j, paths, temp, root)
                for path in paths:
                    word = ''
                    for px, py in path:
                        word += self.board[px][py]
                        self.visited[px][py] = True
                    self.temp.append(word)
                    
                    if len(self.temp) > len(self.results):
                        self.results = self.temp[:]
                        
                    self.dfs(i, j, root)
                    self.temp.pop()
                    for px, py in path:
                        self.visited[px][py] = False
            y = 0
    
    def getAllPaths(self, i, j, paths, temp, root):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or \
            self.board[i][j] not in root.children or \
            self.visited[i][j] == True:
            return
        
        root = root.children[self.board[i][j]]
        if root.isWord:
            temp.append((i,j))
            paths.append(temp[:])
            temp.pop()
            return
        #四方向查找
        self.visited[i][j] = True
        deltas = [(0,1), (0,-1), (1,0), (-1, 0)]
        for dx, dy in deltas:
            newx = i + dx
            newy = j + dy
            temp.append((i,j))
            self.getAllPaths(newx, newy, paths, temp, root)
            temp.pop()
        self.visited[i][j] = False
```


# double DFS
![](https://i.postimg.cc/gkQxTRkJ/Jiuzhang-vip-30days.png)
还是两个dfs嵌套的思想。唯一不同的是外层的dfs直接返回结果。读起来可能更容易一点。。。。
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Solution:
    """
    @param: board: a list of lists of character
    @param: words: a list of string
    @return: an integer
    """
    def boggleGame(self, board, words):
        # write your code here

        # build trie tree
        root = TrieNode()
        for w in words:
            cur = root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isWord = True
            
        # two dfs
        # 1st dfs to determine: given a word, what other words can be found. This is to eliminate the overlapping.
        # 2nd dfs to determine: starting from a position, what words can be found. This is to find words
        self.m, self.n = len(board), len(board[0])
        self.board = board
        self.seen = [[0] * self.n for _ in xrange(self.m)]
        
        return self.dfs(0, 0, root, 0)
        
    def dfs(self, i, j, node, cnt):
        res = cnt
        for x in xrange(i, self.m):
            for y in xrange(j, self.n):
                if self.seen[x][y]:
                    continue
                
                path = []
                visited = []
                
                self.getNxtWords(x, y, path, visited, node)
                for p in path:
                    for px, py in p:
                        self.seen[px][py] = 1
                    
                    res = max(res, self.dfs(x, y + 1, node, cnt + 1))
                    
                    for px, py in p:
                        self.seen[px][py] = 0
            j = 0
        return res
            
    def getNxtWords(self, i, j, path, visited, node):
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        if self.seen[i][j]:
            return
        
        c = self.board[i][j]
        if c not in node.children:
            return
        
        node = node.children[c]
        if node.isWord:
            visited.append((i, j))
            path.append(list(visited))
            visited.pop()
            
            return
        
        self.seen[i][j] = 1
        for dx, dy in direct:
            nx, ny = i + dx, j + dy
            if 0 <= nx < self.m and 0 <= ny < self.n:
                visited.append((i, j))
                self.getNxtWords(nx, ny, path, visited, node)
                visited.pop()
        self.seen[i][j] = 0
```

# double loop
Find the paths of all possible words on the board.
Using two loops to find different configurations of non-overlapped words.
```python
## Problem 635 Boggle Game
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.prefix = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        prefix = ''
        for c in word:
            prefix += c
            node.children[c] = node.children.get(c,TrieNode())
            node = node.children[c]
            node.prefix = prefix
        node.is_word = True

    def find(self,word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node
    
DIRECTIONS = [(0,-1),(0,1),(-1,0),(1,0)]

class Solution:
    """
    @param: board: a list of lists of character
    @param: words: a list of string
    @return: an integer
    """
    def boggleGame(self, board, words):
        # write your code here
        if not board or not board[0]:
            return 0
        
        trie = Trie()
        for word in words:
            trie.insert(word)

        self.paths = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i,j,board,set([(i,j)]),trie.find(board[i][j]))

        ## In outer loop,traverse all words
        ## In inner loop, starting from each word, traverse all words and merge
        ## the paths of non-overlapped words, counting the non-overlapped words
        ## in the meantime.
        res = 0
        for path in self.paths:
            coords = path.copy()
            count = 1
            for neighbor in self.paths:
                if neighbor.isdisjoint(coords):
                    coords.update(neighbor.copy())
                    count += 1
            res = max(res,count)

        return res
            

## calcualte the paths for all words on the board
    def dfs(self,i,j,board,path,node):
        if node is None:
            return
        if node.is_word:
            self.paths.append(path.copy())

        for dx, dy in DIRECTIONS:
            x, y = i + dx, j + dy
            if not self.is_valid(x,y,board):
                continue
            if (x,y) in path:
                continue

            path.add((x,y))
            self.dfs(x,y,board,path,node.children.get(board[x][y]))
            path.remove((x,y))

    def is_valid(self,i,j,board):
        return 0 <= i < len(board) and 0 <= j < len(board[0])
```


# single loop

```python
class TrieNode:
    def __init__(self, label):
        self.label = label
        self.children = {}
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def add(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode(word[i])
            node = node.children[word[i]]
        node.is_word = True
        node.word = word

DIR = [-1, 0, 1, 0, -1]
class Solution:
    """
    @param: board: a list of lists of character
    @param: words: a list of string
    @return: an integer
    """
    def boggleGame(self, board, words):
        trie = Trie()
        for word in words:
            trie.add(word)
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        results = []
        self.dfs(board, 0, 0, 0, 0, trie.root, trie.root, visited, 0, [], results)
        return max([len(result) for result in results]) if results else 0

    def dfs(self, board, x, y, xx, yy, root, node, visited, num_visited, result, results):
        curr_node = None
        if node.is_word:
            result.append(node.word)
            curr_node = root
            results.append(list(result))

        if node == root or curr_node == root:
            for i in range(xx, len(board)):
                start_y = yy if i == xx else 0
                for j in range(start_y, len(board[0])):
                    if visited[i][j]:
                        continue
                    if board[i][j] not in root.children:
                        continue
                    visited[i][j] = True
                    self.dfs(board, i, j, i, j, root, root.children[board[i][j]], visited, num_visited + 1, result, results)
                    visited[i][j] = False
        else:
            for d in range(len(DIR) - 1):
                new_x, new_y = x + DIR[d], y + DIR[d + 1]
                if not 0 <= new_x < len(board) or not 0 <= new_y < len(board[0]):
                    continue
                if visited[new_x][new_y]:
                    continue
                if board[new_x][new_y] not in node.children:
                    continue
                visited[new_x][new_y] = True
                self.dfs(board, new_x, new_y, xx, yy, root, node.children[board[new_x][new_y]], visited, num_visited + 1, result, results)
                visited[new_x][new_y] = False

        if node.is_word:
            result.pop()
```