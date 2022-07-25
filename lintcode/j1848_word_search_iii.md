# JZ: https://www.lintcode.com/problem/1848/

# Official 0
# 算法DFS + Trie （HashMap应该也可）

# 算法思路本题和word search II整体类似，只是最后要求的东西改变了，改为要求同时在
# 整个棋盘上可以圈出的单词数量。我们采用和word search II一致的思路。

# 首先使用trie去预处理dict，用于表示前缀。然后从棋盘的起始点开始dfs，每当我们找
# 到一个单词以后，我们继续在当前棋盘继续进行dfs，直到搜不到单词为止。

# 优化我们可以在棋盘搜索的时候进行优化，当一个单词找到以后，下一个单词我们可以从
# 上一个单词的起点的后面开始搜索。因此我们在dfs的过程中可以记录一下单词的起始
# 点，这样用于下一次开始的枚举。


# Official 1
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: return the maximum nunber
    """
    def wordSearchIII(self, board, words):
        trie = Trie()
        for w in words:
            trie.insert(w)

        return self.dfs(board, trie, set(), 0, -1)

    def dfs(self, board, trie, visited, start_i, start_j):
        n, m = len(board), len(board[0])
        word_count = 0
        for i in range(start_i, n):
            _j = start_j + 1 if i == start_i else 0
            for j in range(_j, m):
                if (i, j) in visited:
                    continue
                c = board[i][j]
                if c not in trie.root.children:
                    continue
                visited.add((i, j))
                word_count = max(
                    word_count,
                    self.search_word(board, i, j, trie, trie.root.children[c], visited, i, j),
                )
                visited.remove((i, j))
        return word_count

    def search_word(self, board, x, y, trie, node, visited, start_i, start_j):
        n, m = len(board), len(board[0])
        word_count = 0
        if node.is_word:
            node.is_word = False
            word_count = self.dfs(board, trie, visited, start_i, start_j) + 1
            node.is_word = True
        for dx, dy in ((1, 0), (0, -1), (-1, 0), (0, 1)):
            i = x + dx
            j = y + dy
            if i < 0 or i >= n or j < 0 or j >= m:
                continue
            if (i, j) in visited:
                continue        
            c = board[i][j]
            if c not in node.children:
                continue
            visited.add((i, j))
            word_count = max(
                word_count,
                self.search_word(board, i, j, trie, node.children[c], visited, start_i, start_j),
            )
            visited.remove((i, j))
        return word_count


# Official 2
class Trie:
    def __init__(self):
        self.children = {}
        self.flag = False
        self.hasWord = False
    
    def put(self, key):
        if key == '':
            self.flag = True
            self.hasWord = True
            return
        
        if key[0] not in self.children:
            self.children[key[0]] = Trie()
        self.children[key[0]].put(key[1:])
        self.hasWord = True
    
    def pop(self, key):
        if key == '':
            self.flag = False
            self.hasWord = False
            return
        if key[0] not in self.children:
            return
        self.children[key[0]].pop(key[1:])
        self.hasWord = any([child.hasWord for child in self.children.values()])
        
    def has(self, key):
        if key == '':
            return self.flag
        
        if not self.hasWord:
            return False
        if key[0] not in self.children:
            return False
        return self.children[key[0]].has(key[1:])


class Solution:
    DIRECT_X = [1, 0, 0, -1]
    DIRECT_Y = [0, 1, -1, 0]
    def wordSearchIII(self, board, words):
        trie = Trie()
        for word in words:
            trie.put(word)
        
        self.results = 0
        self.ans = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.search(trie, trie, board, r, c, r, c)
        return self.ans
                
    def search(self, root, trie, board, x, y, start_x, start_y):
        char = board[x][y]
        if char not in trie.children:
            return
        trie = trie.children[char]
        board[x][y] = '.'
        if trie.flag:
            self.results += 1
            trie.flag = False
            self.ans = max(self.ans, self.results)
            for i in range(start_x, len(board)):
                if i == start_x:
                    range_j = range(start_y + 1, len(board[0]))
                else:
                    range_j = range(len(board[0]))
                for j in range_j:
                    if board[i][j] != '.':
                        self.search(root, root, board, i, j, i, j)
            trie.flag = True
            self.results -= 1
        
        for i in range(4):
            r = x + self.DIRECT_X[i]
            c = y + self.DIRECT_Y[i]
            if r < 0 or r == len(board) or c < 0 or c == len(board[0]):
                continue
            self.search(root, trie, board, r, c, start_x, start_y)
        board[x][y] = char        



# 在 word search II 的DFS模板上直接做了改动。在找到第一个word之后，在剩下的未遍
# 历的元素中继续进行DFS。
class Result:
    def __init__(self):
        self.result = 0
        
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: return the maximum nunber
    """
    def wordSearchIII(self, board, words):
        # write your code here
        if not board:
            return 0
        
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        prefix = set()
        for word in words:
            for i in range(len(word)):
                prefix.add(word[:i + 1])
        words = set(words)
        maxCount = Result()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, i, j, board, prefix, words, set([(i, j)]), board[i][j], 0, maxCount, directions)
        
        return maxCount.result
    
    def dfs(self, i, j, start_x, start_y, board, prefix, words, visited, string, count, maxCount, directions):
        if string not in prefix:
            return
        
        if string in words:
            words.remove(string)
            count += 1
            maxCount.result = max(count, maxCount.result)
            for x in range(start_x, len(board)):
                if x == start_x:
                    range_y = range(start_y + 1, len(board[0]))
                else:
                    range_y = range(len(board[0]))
                for y in range_y:
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    self.dfs(x, y, x, y, board, prefix, words, visited, board[x][y], count, maxCount, directions)
                    visited.remove((x, y))
            count -= 1
            words.add(string)
        
        for (dx, dy) in directions:
            next_x, next_y = i + dx, j + dy
            if not self.isInside(board, next_x, next_y):
                continue
            if (next_x, next_y) in visited:
                continue
            visited.add((next_x, next_y))
            self.dfs(next_x, next_y, start_x, start_y, board, prefix, words, visited, string + board[next_x][next_y], count, maxCount, directions)
            visited.remove((next_x, next_y))
                    
    def isInside(self, board, i, j):
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            return True
        return False
                    
        

# Trie + DFS(two times)
# Trie to build the words prefix tree

# first DFS find the map where key is the word, value is a list of set,each set
# is a way that the word occupied locations in the board

# second DFS just trying to find the combinations we can have most on the board
class Trie:

  def __init__(self):
    self.nei = {}
    self.word = None

  def add(self, root, new_word):
    ptr = root
    for char in new_word:
      if char not in ptr.nei:
        ptr.nei[char] = Trie()
      ptr = ptr.nei[char]
    ptr.word = new_word

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: return the maximum nunber
    """
    def wordSearchIII(self, board, words):
        # write your code here
        if not board or len(board) == 0:
          return []
        root = Trie()
        for word in words:
          root.add(root, word)
        
        rows = len(board)
        cols = len(board[0])
        word_locs = collections.defaultdict(list)

        for row in range(rows):
          for col in range(cols):
            visited = set()
            next_char = board[row][col]
            if next_char not in root.nei:
              continue
            idx = row * cols + col
            visited.add(idx)
            self.DFS(board, row, col, root.nei[next_char], visited, word_locs)
            visited.remove(idx)
        
        res = [0]
        visited.clear()
        self.find_max(word_locs, words, res, 0, visited, 0)
        return res[0]
    

    def DFS(self, board, row, col, trie_node, visited, word_locs):
        if trie_node.word:
          word_locs[trie_node.word].append(set(visited))
        
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for row_acc, col_acc in dirs:

          new_row, new_col = row + row_acc, col + col_acc

          if new_row < 0 or new_row >= len(board) or new_col < 0 or new_col >= len(board[0]):
            continue

          idx = new_row * len(board[0]) + new_col
          if idx in visited:
            continue

          next_char = board[new_row][new_col]
          if next_char not in trie_node.nei:
            continue

          visited.add(idx)
          self.DFS(board, new_row, new_col, trie_node.nei[next_char], visited, word_locs)
          visited.remove(idx)


    def find_max(self, word_locs, words, res, cur_cnt, visited, idx):
      if res[0] == len(words):
        return
      res[0] = max(res[0], cur_cnt)
      if idx == len(words):
        return
      
      for i in range(idx, len(words)):
        next_locs = word_locs[words[i]]
        for next_loc in next_locs:
          if len(next_loc.intersection(visited)) == 0:
            visited.update(next_loc)
            self.find_max(word_locs, words, res, cur_cnt + 1, visited, i + 1)
            visited.difference_update(next_loc)