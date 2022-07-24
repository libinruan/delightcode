# answer 1
# https://www.lintcode.com/problem/132/solution/16642
# 不用 Trie，直接使用哈希表的方法
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if board is None or len(board) == 0:
            return []
        
        # pre-process
        # 预处理
        word_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
        
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(
                    board,
                    i,
                    j,
                    board[i][j],
                    word_set,
                    prefix_set,
                    set([(i, j)]),
                    result,
                )
                
        return list(result)
        
    def search(self, board, x, y, word, word_set, prefix_set, visited, result):
        if word not in prefix_set:
            return
        
        if word in word_set:
            result.add(word)
        
        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y
            
            if not self.inside(board, x_, y_):
                continue
            if (x_, y_) in visited:
                continue
            
            visited.add((x_, y_))
            self.search(
                board,
                x_,
                y_,
                word + board[x_][y_],
                word_set,
                prefix_set,
                visited,
                result,
            )
            visited.remove((x_, y_))
            
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])



# answer 2. Trie, dfs
# https://www.lintcode.com/problem/132/solution/17284
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class TrieNode:			#定义字典树的节点
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):		#字典树插入单词
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()   #在此节点申请节点
            node = node.children[c]     		#继续遍历
        node.is_word = True
        node.word = word        #存入单词
        
    def find(self, word):	
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
                
        return node
        

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if board is None or len(board) == 0:
            return []
            
        trie = Trie()
        for word in words:			#插入单词
            trie.add(word)

        result = set()
        for i in range(len(board)):				#遍历字母矩阵，将每个字母作为单词首字母开始搜索
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(
                    board,
                    i,
                    j,
                    trie.root.children.get(c),
                    set([(i, j)]),
                    result,
                )
                
        return list(result)
        
    def search(self, board, x, y, node, visited, result):			#在字典树上dfs查找
        if node is None:
            return
        
        if node.is_word:
            result.add(node.word)
        
        for delta_x, delta_y in DIRECTIONS:				#向四个方向查找
            x_ = x + delta_x
            y_ = y + delta_y
            
            if not self.inside(board, x_, y_):
                continue
            if (x_, y_) in visited:
                continue
            
            visited.add((x_, y_))
            self.search(
                board,
                x_,
                y_,
                node.children.get(board[x_][y_]),
                visited,
                result,
            )
            visited.remove((x_, y_))
            
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])



# answer 3 Trie + backtrack
# https://www.lintcode.com/problem/132/solution/57229
from typing import (
    List,
)

from collections import defaultdict

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word

class Solution:
    def word_search_i_i(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(now, i1, j1):
            if board[i1][j1] not in now.children:
                return
            ch = board[i1][j1]
            now = now.children[ch]
            if now.word != "": ans.add(now.word)
            board[i1][j1] = "#"
            for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                if 0 <= i2 < m and 0 <= j2 < n:
                    dfs(now, i2, j2)
            board[i1][j1] = ch

        ans = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)
        return list(ans)



# answer 4. 删除被匹配的单词
# https://www.lintcode.com/problem/132/solution/57231
class Solution {
    int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public List<String> wordSearchII(char[][] board, List<String> words) {
        Trie trie = new Trie();
        for (String word : words) {
            trie.insert(word);
        }

        Set<String> ans = new HashSet<String>();
        for (int i = 0; i < board.length; ++i) {
            for (int j = 0; j < board[0].length; ++j) {
                dfs(board, trie, i, j, ans);
            }
        }

        return new ArrayList<String>(ans);
    }

    public void dfs(char[][] board, Trie now, int i1, int j1, Set<String> ans) {
        if (!now.children.containsKey(board[i1][j1])) {
            return;
        }
        char ch = board[i1][j1];
        Trie nxt = now.children.get(ch);
        if (!"".equals(nxt.word)) {
            ans.add(nxt.word);
            nxt.word = "";
        }

        if (!nxt.children.isEmpty()) {
            board[i1][j1] = '#';
            for (int[] dir : dirs) {
                int i2 = i1 + dir[0], j2 = j1 + dir[1];
                if (i2 >= 0 && i2 < board.length && j2 >= 0 && j2 < board[0].length) {
                    dfs(board, nxt, i2, j2, ans);
                }
            }
            board[i1][j1] = ch;
        }

        if (nxt.children.isEmpty()) {
            now.children.remove(ch);
        }
    }
}

class Trie {
    String word;
    Map<Character, Trie> children;
    boolean isWord;

    public Trie() {
        this.word = "";
        this.children = new HashMap<Character, Trie>();
    }

    public void insert(String word) {
        Trie cur = this;
        for (int i = 0; i < word.length(); ++i) {
            char c = word.charAt(i);
            if (!cur.children.containsKey(c)) {
                cur.children.put(c, new Trie());
            }
            cur = cur.children.get(c);
        }
        cur.word = word;
    }
}