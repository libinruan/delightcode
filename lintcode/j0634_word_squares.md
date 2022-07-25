# answer 1*
# https://www.lintcode.com/problem/634/solution/16732
# 根据九章算法强化班写的，主要是增加了很多注释来帮助大家理解

# 去掉了不必要的代码，比如Trie里面的contains
# 增加了很多注释，更好的理解代码

# define data structure
class TrieNode :
    def __init__(self) :
        self.children = {}
        self.is_word = False
        self.word_list = []
        
class Trie :
    def __init__(self) :
        self.root = TrieNode()
    
    def add(self, word) :
        node = self.root
        for c in word :
            if c not in node.children :
                node.children[c] = TrieNode()
            node = node.children[c]
            node.word_list.append(word)
        node.is_word = True
    
    def find(self, word) :
        node = self.root 
        for c in word :
            node = node.children.get(c)
            if node is None :
                return None
        return node
        
    def words_prefix(self, prefix) :
        node = self.find(prefix)
        return [] if node is None else node.word_list


class Solution:

    def wordSquares(self, words):
        # 初始化trie，加入单词
        trie = Trie()
        for word in words :
            trie.add(word)
        # 检测是否可以加入，sqaure为list
        squares = []
        for word in words :
            self.search(trie, [word], squares)
            
        return squares
        
    def search(self, trie, square, squares) :
        # eg. ['wall', 'area'] n: 单词长度 4, pos: 单词数目 2
        n, pos = len(square[0]), len(square)
        # 递归出口 - 需要deep copy 
        if n == pos :
            squares.append(list(square))
            return 
        
        # 剪枝 - 以后面为前缀的是否存在
        for col in range(pos, n) :
            prefix = ''.join(square[i][col] for i in range(pos))
            if trie.find(prefix) is None :
                return 
    
        # ['wall',
        #  'area']  prefix = 'le'，下一个应该以le开头，每行的pos - 2
        prefix = ''.join(square[i][pos] for i in range(pos))
        for word in trie.words_prefix(prefix) :
            # 尝试将word加入
            square.append(word)
            self.search(trie, square, squares)
            square.pop()



# answer 2
# https://www.lintcode.com/problem/634/solution/18015
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_list = []


class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.word_list.append(word)
        node.is_word = True

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node
        
    def get_words_with_prefix(self, prefix):
        node = self.find(prefix)
        return [] if node is None else node.word_list
        
    def contains(self, word):
        node = self.find(word)
        return node is not None and node.is_word
        
        
class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        trie = Trie()
        for word in words:
            trie.add(word)
            
        squares = []
        for word in words:
            self.search(trie, [word], squares)
        
        return squares
        
    def search(self, trie, square, squares):
        n = len(square[0])
        curt_index = len(square)
        if curt_index == n:
            squares.append(list(square))
            return
        
        # Pruning, it's ok to remove it, but will be slower
        for row_index in range(curt_index, n):
            prefix = ''.join([square[i][row_index] for i in range(curt_index)])
            if trie.find(prefix) is None:
                return
        
        prefix = ''.join([square[i][curt_index] for i in range(curt_index)])
        for word in trie.get_words_with_prefix(prefix):
            square.append(word)
            self.search(trie, square, squares)
            square.pop() # remove the last word



# answer 3*
# https://www.lintcode.com/problem/634/solution/17866
class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        from collections import defaultdict
        if len(words) == 0:
            return [];
        res = []
        prefix = defaultdict(list)
        squares = []
        #预处理得到prefix
        def initprefix(words):
            for word in words:
                prefix[""].append(word)
                pre = ""
                for i in range(len(word)):
                    pre += word[i]
                    prefix[pre].append(word)
        def checkprefix(index,Next):
            for i in range(index+1,wordlen):
                pre = ""
                for j in range(index):
                    pre += squares[j][i]
                pre += Next[i]
                if pre not in prefix:
                    return False
            return True
        def dfs(index):
            if index == wordlen:
                res.append(squares[:])
                return
            pre = ""
            for i in range(index):
                pre += squares[i][index]
            matchedword = prefix[pre][:]
            m = len(matchedword)
            for i in range(m):
                #找到pre前缀
                if checkprefix(index,matchedword[i]) == False:
                    continue
                squares.append(matchedword[i])
                dfs(index + 1)
                squares.pop()
                
        initprefix(words);
        wordlen = len(words[0])
        dfs(0)
        return res;             