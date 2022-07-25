# https://www.lintcode.com/problem/1742/

# 描述给出了一个由小写字母组成的字符串 S。
# 然后，我们可以进行任意次数的移动。

# 在每次移动中，我们选择前 K 个字母中的一个（从左侧开始），将其从原位置移除，并
# 放置在字符串的末尾。

# 返回我们在任意次数的移动之后可以拥有的按字典顺序排列的最小字符串。



# https://www.lintcode.com/problem/1742/solution/59240
# 数学
# 当 K = 1 时，每次操作只能将第一个字符移动到末尾，因此字符串 S 可以看成一个头尾相连的环。如果 S 的长度为 NN，我们只需要找出这 NN 个位置中字典序最小的字符串即可。

# 当 K = 2 时，可以发现，我们能够交换字符串中任意两个相邻的字母。具体地，设字符串 S 为 S[1], S[2], ..., S[i], S[i + 1], ..., S[N]，我们需要交换 S[i] 和 S[j]。首先我们依次将 S[i] 之前的所有字符依次移到末尾，得到

# S[i], S[i + 1], ..., S[N], S[1], S[2], ..., S[i - 1]

# 随后我们先将 S[i + 1] 移到末尾，再将 S[i] 移到末尾，得到

# S[i + 2], ..., S[N], S[1], S[2], ..., S[i - 1], S[i + 1], S[i]

# 最后将 S[i + 1] 之后的所有字符依次移到末尾，得到

# S[1], S[2], ..., S[i - 1], S[i + 1], S[i], S[i + 2], ..., S[N]

# 这样就交换了 S[i] 和 S[i + 1]，而没有改变其余字符的位置。

# 当我们可以交换任意两个相邻的字母后，就可以使用冒泡排序的方法，仅通过交换相邻两个字母，使得字符串变得有序。因此当 K = 2 时，我们可以将字符串移动得到最小的字典序。

# 当 K > 2 时，我们可以完成 K = 2 时的所有操作。

class Solution(object):
    def orderlyQueue(self, S, K):
        if K == 1:
            return min(S[i:] + S[:i] for i in range(len(S)))
        return "".join(sorted(S))

# 复杂度分析

# 时间复杂度：当 K = 1 时为 O(N^2)

# 否则为 O(NlogN)，其中 N 是字符串 S 的长度。

# 空间复杂度：当 K = 1 时为 O(N^2)，否则为 O(N)。



# answer 2.
# 当K>1，相当于可以任意排列，所以直接返回最小值
# 当K==1，有S.length不同的状态，返回按字典顺序排列的最小字符串。

class Solution:
    """
    @param S: a string
    @param K: int
    @return: the lexicographically smallest string
    """
    def orderlyQueue(self, S, K):
        # Write your code here.
        if K > 1:
            lst = list(S)
            lst.sort()
            return ''.join(lst)
        min_char = min(set(S))
        ans = S
        for i in range(len(S)):
            if S[i] == min_char:
                ans = min(ans, S[i:] + S[:i])
        return ans



# ansewr 3
# 暴力法
# k=0 无法排列
# k=1 只能旋转， 这里就一个个比过去
# k=2 啥都能做， 所以直接排好
# 序return就行。 这里的排序方法就是， 前2个里面， 把小的一直往后循环， 大的保持
# 住， 转很多很多圈之后， 就排好序了

class Solution:
    """
    @param S: a string
    @param K: int
    @return: the lexicographically smallest string
    """
    def orderlyQueue(self, S, K):
        if K == 0:
            return S
        if K > 1:
            return "".join(sorted(list(S)))
        
        min_start = 0
        str_to_cmp = S + S
        for start in range(len(S)):
            for i in range(len(S)):
                if str_to_cmp[start + i] < str_to_cmp[min_start + i]:
                    print(start, min_start, i, str_to_cmp[start + i], str_to_cmp[min_start + i])
                    min_start = start
                    break
                elif str_to_cmp[start + i] > str_to_cmp[min_start + i]:
                    break
                else:
                    continue
        return str_to_cmp[min_start:(min_start + len(S))]        



# answer 4
class Solution:
    """
    @param S: a string
    @param K: int
    @return: the lexicographically smallest string
    """
    def orderlyQueue(self, S, K):
        # Write your code here.
        if K > 1: 
          return ''.join(sorted(list(S)))
        else: 
          min_char = min(list(S)) 

          answer = S 
          for i in range(len(S)): 
            if S[i] == min_char: 
              answer = min(answer, S[i:] + S[:i])
          return answer