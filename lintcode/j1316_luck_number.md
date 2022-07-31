# solution 1
https://www.lintcode.com/problem/1316/solution/21962
单调栈版
一看到这种左边画个龙右边画个彩虹的题目， 就应该想到单调栈。 唯一不同的是， 这里不是找最近的， 而是最小的里面找最大的， 最大的里面找最小的， 于是就不能直接做， 就需要用奇偶跳那一课讲过的排序以后在index上面做单调栈的方式。
本来是， f是在左边找比自己大的里面最小的， g是在右边找比自己小的里面最大的， 换成了index以后， 就变成了f是找右边第一个比自己小的， g是找左边第一个比自己大的。 那么算f的时候， 我们用单调递增栈， 算g的时候用单调递减栈， 就可以了。

```python
class Solution:
    """
    @param arr: the arr
    @return: the sum of the luck number
    """
    def luckNumber(self, nums):
        index_number_pair = []
        for i in range(len(nums)):
            index_number_pair.append((i, nums[i]))
        index_number_pair.sort(key = lambda num:num[1])

        f_index = [-1] * len(nums)
        g_index = [-1] * len(nums)

        stack = []
        for i in range(len(index_number_pair)):
            while stack and stack[-1][0] > index_number_pair[i][0]:
                poped = stack.pop()
                f_index[poped[0]] = index_number_pair[i][0]
            stack.append(index_number_pair[i])
        while stack:
            poped = stack.pop()
            f_index[poped[0]] = -1

        for i in range(len(index_number_pair)):
            while stack and stack[-1][0] < index_number_pair[i][0]:
                poped = stack.pop()
                if stack:
                    g_index[poped[0]] = stack[-1][0]
            stack.append(index_number_pair[i])
        while stack:
            poped = stack.pop()
            if stack:
                g_index[poped[0]] = stack[-1][0]

        count = 0
        for i in range(len(nums)):
            if f_index[i] != -1 and g_index[i] != -1:
                if nums[f_index[i]] % nums[g_index[i]] == 0:
                    count += 1
        return count
        
```

# soltuion 2 sorted

稍微卖弄了点Python技巧，初学者可能要股沟一下才能看懂。不过花10分钟时间弄懂这个应该比花时间看懂衡助教的猛操作更有益
```python
class Solution:
    
    def luckNumber(self, nums):
        
        sorting = sorted(range(len(nums)), key = nums.__getitem__)
        
        f, g = {}, {}
        
        stack = []
        for i in sorting:
            while stack and i < stack[-1] and nums[i] > nums[stack[-1]]:
                f[stack.pop()] = nums[i]
            stack += i,
            
        stack = []
        for j in sorting[::-1]:
            while stack and j > stack[-1] and nums[j] < nums[stack[-1]]:
                g[stack.pop()] = nums[j]
            stack += j,
            
        return sum(f[i]%g[i] == 0 for i in range(len(nums)) if i in f and i in g)
```
既然第一步已经sort了，nums[i] > nums[stack[-1]]， 还有nums[j] < nums[stack[-1]]， 就完全没必要，多此一举

# solution 3
https://www.lintcode.com/problem/1316/solution/32560

目的是实现找到每一个数左边比它大的且最小的数。
我们利用stack来实现。
排序后按照从小到大的顺序进入stack，每次与stack顶部比较。若发现stack顶部的x值（即在数组之中的位置比目前待进入的小），那么该数的值一定是目前的待进入数。然后将该数pop出来，带进入的数继续反复与栈顶比较即可。最后将其push进栈。
找到在该数右边比它大的也可以用一样的方法。
复杂度O(n*logn)O(n∗logn)
同样也可以使用二分划分树的方法。
复杂度为(n*logn*logn)(n∗logn∗logn)

```python
class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def empty(self):
        return len(self.stack) == 0;
    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]
class Solution:
    """
    @param arr: the arr
    @return: the sum of the luck number
    """
    def luckNumber(self, arr):
        # Write your code here.
        n = len(arr);
        right = [0 for i in range(50050)];
        left = [0 for i in range(50050)];
        a = [{'sum':0,'x':0} for i in range(n)];
        ans = 0;
        s = Stack()
        for i in range(0,n):
            a[i]['sum']=arr[i];
            a[i]['x']=i;
        a = sorted(a,key=lambda tmp: tmp['sum']);
        print(len(s.stack))
        for i in range(0,n):
            
            while s.empty() == False:
                
                fir = s.top();
                if a[i]['x'] < fir['x']:
                    left[fir['x']]=a[i]['sum'];
                    s.pop();
                else:
                    break;
            s.push(a[i]);

        while s.empty() == False:
            s.pop();
        for i in range(n - 1, -1, -1):
            while s.empty() == False:
                fir=s.top();
                if a[i]['x']>fir['x']:
                    right[fir['x']]=a[i]['sum'];
                    s.pop();
                else:
                    break;
            s.push(a[i]);
        for i in range(0, n):
            if left[i] * right[i] != 0 and left[i] % right[i] == 0:
                ans+=1;
        return ans;
```        

