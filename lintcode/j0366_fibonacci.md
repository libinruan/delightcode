class Solution:
    def fibonacci(self, n):
        """
        time and space: O(n)
        """
        fib = [0, 0, 1]
        for i in range(3, n + 1, 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]


"""
这道题并不需要存储那么多的fibonacci数，因为是返回第n项，并且第n项只和前面的两个
数字有关，所以利用一个长度为2的空间记录前两个数字即可。
此时时间复杂度不变，但是空间复杂度降为O(1)。

这种节省空间的方法其实就是动态规划的滚动数组思想。
"""
class Solution:
    def fibonacci(self, n):
        fib = [0, 1]
        for i in range(2, n + 1, 1):
            fib[i % 2] = fib[0] + fib[1]
        return fib[(n + 1) % 2]


"""
这么做的时间复杂度难以接受，因为有很多被重复计算的数字，比如我们在求解fib(10)的
时候，会找到fib(9)和fib(8)共两个，然后下一层会是fib(8)和fib(7)，fib(7)和fib(6)共
四个。这是一个呈指数增长的曲线，其底数为2，是稳定超时的代码。

时间复杂度为O(2^n)，空间复杂度为O(n)（不考虑递归的栈空间占用则为O(1)）。
"""
class Solution:
    def dfs(self, n):
        if n <= 2:
            return n - 1
        return self.dfs(n - 1) + self.dfs(n - 2)
    
    def fibonacci(self, n):
        return self.dfs(n)        


"""
这时候就要用到一种经常被用来以空间换时间的优化算法——记忆化搜索。

顾名思义，它将计算出的结果存储下来，在计算到指定值的时候，先判断这个值是否已经计
算过，若没有，才进行计算，否则读取已经存储下来的值。这样就把一个指数级复杂度变成
了线性复杂度，代价是空间复杂度从常数级上升至线性级。

时间复杂度为O(n)，空间复杂度为O(n)。
"""        
class Solution:
    def dfs(self, n, fib):
        if fib[n] != -1:
            return fib[n]
        if n <= 2:
            fib[n] = n - 1
            return fib[n]
        fib[n] = self.dfs(n - 1, fib) + self.dfs(n - 2, fib)
        return fib[n]
    
    def fibonacci(self, n):
        result = [-1] * (n + 1)
        self.dfs(n, result)
        return result[n]


"""
矩陣快速冪 - https://www.lintcode.com/problem/366/solution/18282?fromId=164&_from=collection
"""        
class Solution:
    def quickPow(self, a, n):
        base = a
        resultMatrix = Matrix(2, 2)
        resultMatrix.numbers[0][0] = 1
        resultMatrix.numbers[1][1] = 1
        while n > 0:
            if n % 2 == 1:
                resultMatrix = resultMatrix.multiply(base)
            base = base.multiply(base)
            n //= 2
        return resultMatrix
    
    def fibonacci(self, n):
        if n == 1:
            return 0
        
        startMatrix = Matrix(2, 1)
        rollingMatrix = Matrix(2, 2)
        
        startMatrix.numbers[0][0] = 1
        startMatrix.numbers[1][0] = 0
        rollingMatrix.numbers[0][0] = 1
        rollingMatrix.numbers[0][1] = 1
        rollingMatrix.numbers[1][0] = 1
        rollingMatrix.numbers[1][1] = 0
        rollingMatrix = self.quickPow(rollingMatrix, n - 2)
        startMatrix = rollingMatrix.multiply(startMatrix)
        return startMatrix.numbers[0][0]

class Matrix:
    def __init__(self, row, column):
        self.row = row;
        self.column = column;
        self.numbers = []
        for i in range(0, row, 1):
            self.numbers.append([0] * column)
        
    def multiply(self, a):
        newMatrix = Matrix(self.row, a.column)
        for i in range(0, newMatrix.row, 1):
            for j in range(0, newMatrix.column, 1):
                for k in range(0, newMatrix.column, 1):
                    newMatrix.numbers[i][j] = newMatrix.numbers[i][j] + self.numbers[i][k] * a.numbers[k][j]
        return newMatrix