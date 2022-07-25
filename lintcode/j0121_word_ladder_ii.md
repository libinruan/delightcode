# answer 1
# https://www.lintcode.com/problem/121/solution/20402
import collections
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, source, target, wordList):
        # write your code here
        if not source or not target or len(source) != len(target):
            return []
        
        n = len(source)
        
        wordList.add(source)
        wordList.add(target)
        
        self.indexes = self.buildIndexes(n, wordList)
        self.distances = {}
        
        self.bfs(target)
        
        res = []
        if source in self.distances:
            self.dfs(source, target, [source], res)
        return res
    
    ## generate a new word that removed the index-position character
    def getDiff1Word(self, word, index):
        return word[:index] + word[index + 1:]


    ## generate a list of dictionary called indexes
    ## indexes[i] meaning by removing i-th character (0 <= i < n)
    ## for each word in wordList
    ## { shortened-word: [original-word1, original-word2, ...], ... }
    def buildIndexes(self, n, wordList):
        indexes = []
        for i in range(n):
            temp = collections.defaultdict(list)
            for word in wordList:
                shortenWord = self.getDiff1Word(word, i)
                temp[shortenWord].append(word)
            indexes.append(temp)
        return indexes


    ## iterate each position i of word
    ## first generate the shortenWord in position i
    ## if shortenWord can be generating from wordList
    ## by checking `if shortenWord in self.indexes[i]`
    ## return a different word each time
    ## inputWord --> shortenWord --> each possible word in wordList
    ###############################################################
    ## IMPORTANT:                                                ##
    ## all the word generates by this function                   ##
    ## IS TO BE ENSURED IS THE WORD IN WORDLIST                  ##
    ###############################################################
    def getNextWord(self, word):
        for i in range(len(word)):
            shortenWord = self.getDiff1Word(word, i)
            if shortenWord in self.indexes[i]:
                for nextWord in self.indexes[i][shortenWord]:
                    if nextWord != word:
                        yield nextWord
      

    ## BFS function updates distance
    ## OF ALL THE POSSIBLE (REACHABLE) WORD in self.getNextWord
    ## to the target word
    def bfs(self, target):
        self.distances[target] = 0
        q = [target]
        while q:
            curr = q.pop(0)
            for word in self.getNextWord(curr):
                if word not in self.distances:
                    self.distances[word] = self.distances[curr] + 1
                    q.append(word)
        
    
    ## DFS search for all possible paths
    def dfs(self, currentWord, target, currentPath, results):
        if currentWord == target:
            results.append(currentPath[:])
            return
        
        for word in self.getNextWord(currentWord):
            if self.distances.get(word, -2) + 1 == self.distances[currentWord]:
                currentPath.append(word)
                self.dfs(word, target, currentPath, results)
                currentPath.pop()



# answer 2
# https://www.lintcode.com/problem/121/solution/16602
from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        distance = {}
        
        self.bfs(end, distance, dict)
        
        results = []
        self.dfs(start, end, distance, dict, [start], results)
        
        return results

    def bfs(self, start, distance, dict):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, dict):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)
    
    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in dict:
                    words.append(next_word)
        return words
                        
    def dfs(self, curt, target, distance, dict, path, results):
        if curt == target:
            results.append(list(path))
            return
        
        for word in self.get_next_words(curt, dict):
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, dict, path, results)
            path.pop()




# answer 3
# https://www.lintcode.com/problem/121/solution/23747    
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        from collections import defaultdict
        dict = set(dict)
        #将end添加进dict,防止结果为[]
        dict.add(end)
        res = []
        # 记录单词下一步能转到的单词
        next_word_dict = defaultdict(list)
        # 记录到start距离
        distance = {}
        distance[start] = 0
        
        # 暴力匹配,当前字符串修改一个字母后的新字符串存在于dict中
        def next_word(word):
            ans = []
            for i in range(len(word)):
                       #97=ord('a')，123=ord('z')+1  
                for j in range(97, 123):
                    tmp = word[:i] + chr(j) + word[i + 1:]
                    if tmp != word and tmp in dict:
                        ans.append(tmp)
            return ans
        # 求到start的距离
        def bfs():
            q = collections.deque()
            q.append(start)
            step = 0
            flag = False #标记是否找到结果
            while len(q) is not 0:
                step += 1
                n=len(q)
                for i in range(n):
                    word=q[0]
                    q.popleft()
                    for nextword in next_word(word):
                        next_word_dict[word].append(nextword)
                       #当下一跳是end时，就可以结束搜索
                        if nextword == end:
                            flag = True
                        #如果没被添加过，则进行添加
                        if nextword not in distance:
                            distance[nextword] = step
                            q.append(nextword)
                if flag:
                    break
        # 遍历所有从start到end的路径
        def dfs(tmp, step):
            if tmp[-1] == end:
                res.append(tmp)
                return
            for word in next_word_dict[tmp[-1]]:
                if distance[word] == step + 1:
                    dfs(tmp + [word], step + 1)
        #bfs搜start--end的最短路径           
        bfs()
        #dfs输出距离最短的路径
        dfs([start], 0)
        return res        