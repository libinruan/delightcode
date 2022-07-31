# solution 1
calculate the next array in the kmp algorithm first, then the answer is len(array) - 1 - next[-1]

```python
class Solution:
    """
    @param array: an integer array
    @return: the length of the minimum cycle section
    """
    def minimumCycleSection(self, array):
        # Write your code here
        next = [-1]
        n = len(array)
        for i in range(1, n):
            j = i - 1
            while j >= 0 and array[next[j] + 1] != array[i]: j = next[j]
            next.append(next[j] + 1 if j >= 0 else j)
        return n - 1 - next[-1]
```        

```python
class Solution:
    """
    @param array: The array
    @return: The answer
    """
    def minimumCycleSection(self, array):
        i = 0
        j = -1
        next = [0 for x in range(len(array) + 1)]
        next[0] = -1
        while(i < len(array)):
            if j == -1 or array[i] == array[j]:
                i+=1
                j+=1
                next[i] = j
            else:
                j = next[j]
        return i - next[i]
```