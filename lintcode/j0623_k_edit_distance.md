# Trie 
1.给了两种解法
a.第一种是直接算target和每个单词的edit distance, 这种会超时，因为每个单词要重新build一个二维数组。

b.另一种思路是将words build成trie，然后在trie上dfs，每次到一个节点就和word的每一个字符比较一下，这个比较的结果放在dp里供下层使用。
这样在代码里就省去了为每一个新单词build一个新的2D array，非常巧妙。

```python
'''class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """
    # using dp, will get the TLE
    def edit_distance(self, word1, word2):
        M, N = len(word1), len(word2)
        f = [[0]*(N + 1) for i in range(M + 1)]

        for i in range(M + 1):
            for j in range(N + 1):
                if i == 0:
                    f[i][j] = j
                    continue
                if j == 0:
                    f[i][j] = i
                    continue
                
                f[i][j] = min(f[i-1][j], f[i][j-1]) + 1
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = min(f[i][j], f[i-1][j-1])
        return f[M][N]
        
    def kDistance(self, words, target, k):
        # write your code here
        ans = []
        for word in words:
            dist = self.edit_distance(word, target)
            if dist <= k:
                ans.append(word)
        return ans'''
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        if word is None:
            return
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word
        
class Solution:
    def kDistance(self, words, target, k):
        # using dynamic programming
        # the idea is for each dp array
        # it records the edit distance between
        # current prefix and the target
        # it's like one row in the original dp array
        if not words or target is None:
            return []
        # initialize the empty dp
        # empty string vs "target"
        N = len(target)
        # 
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        dp = [j for j in range(N + 1)]
        results = []
        self.dfs(target, k, N, trie.root, dp, results)
        return results
        
    def dfs(self, target, k, N, node, dp, results):
        if node.is_word and dp[N] <= k:
            results.append(node.word)

        # new dp array
        new = [0 for _ in range(N + 1)]
        new[0] = dp[0] + 1 # from the previous row 
        
        # try all branches of node
        for next_char, next_node in node.children.items():
            for j in range(1, N + 1):
                if next_char == target[j - 1]:
                    new[j] = min(dp[j - 1], dp[j] + 1, new[j - 1] + 1)
                else:
                    new[j] = min(dp[j - 1] + 1, dp[j] + 1, new[j - 1] + 1)
            self.dfs(target, k, N, next_node, new, results)
```

# Trie + DP + Rolling Array
```python
class Solution:
    def buildTrie(self, words):
        trie = {}
        for word in words:
            root = trie
            for char in word:
                root = root.setdefault(char, {})
            root["#"] = word
        return trie

    def dfs(self, root, depth, pre, result, target, k):
        n = len(target)

        for char in root:
            if char == "#":
                continue

            dp = [depth] + [0] * n
            for j in range(1, n + 1):
                dp[j] = min(
                    pre[j] + 1, dp[j - 1] + 1,
                    pre[j - 1] + (char != target[j - 1])
                )

            if "#" in root[char] and dp[-1] <= k:
                result.append(root[char]["#"])

            self.dfs(root[char], depth + 1, dp, result, target, k)

    def kDistance(self, words, target, k):
        if not words:
            return []

        if not target:
            return list(filter(lambda x: len(x) <= k, words))

        if not k:
            return list(filter(lambda x: x == target, words))

        result = []
        self.dfs(
            self.buildTrie(words), 1, list(range(len(target) + 1)), result,
            target, k
        )
        return result
```

# Trie + DP + DFS
字典树+DFS+DP版
这个题目， 一个题目考了3个算法。 真的是题目中的王者。 除了难， 我想不到用其他词形容。 下面来说说看怎么做吧。

首先， 最暴力的做法， 就是对于每一个字典里面的单词， 跟target去跑一遍LCS。 如果小于等于K加到结果里面。 这种做法相信学过DP的都做得出来。

那么如何优化呢？我们发现DP的过程中， 同一个前缀其实我们算了很多次， 如果可以结果可以不重复算， 那么就可以大大降低复杂度。 怎么做呢？首先建个字典树。 然后对于每一个前缀都跟target去做一下LCS的DP。 那么这里每跑出来的那个DP数组相当于普通LCS的一行。 然后用DFS的方式， 把整棵树跑完就可以了。

具体做法， 高频班字典树那一个直播课讲了。

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
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode(word[i])
            curr = curr.children[word[i]]
        curr.is_word = True
        curr.word = word

class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """
    def kDistance(self, words, target, k):
        trie = Trie()
        for word in words:
            trie.add(word)
        results = []
        dp = [0 for i in range(len(target) + 1)]
        self.dfs(trie.root, "", target, k, dp, results)
        return results
        
    def dfs(self, trie_node, word, target, K, dp, results):
        new_dp = [0] * len(dp)
        if len(word) > 0:
            new_dp[0] = dp[0] + 1
        for i in range(1, len(new_dp)):
            if len(word) > 0:
                new_dp[i] = min(dp[i], new_dp[i - 1]) + 1
                new_dp[i] = min(new_dp[i], dp[i - 1] + (0 if target[i - 1] == word[-1] else 1))
            else:
                new_dp[i] = new_dp[i - 1] + 1

        if trie_node.is_word:
            if new_dp[len(target)] <= K:
                results.append(trie_node.word)

        for child in trie_node.children:
            self.dfs(trie_node.children[child], word + child, target, K, new_dp, results)
```