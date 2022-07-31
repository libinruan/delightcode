# TinLittle
O(mLogN)。这道题的面试标准答案。面试时，你能写出这样，就是Hire，follow-up问题能答好，就是Strong Hire。

要点是：

不要用系统max函数，因为你即需要最值也需要最值下标。
要lo<=hi，不要lo+1<hi。下标移动要快，lo+1<hi有维和感。
follow-up，当然可以说，m > n 时，可以写成 O(nLogM)

追求那个O(m+n)的解法，对于准备面试是纯粹浪费时间。Erik Demaine是14岁大学毕业的神童，20岁当上麻省理工的教授，他是第一个在课堂上讲这个
O(m+n)解的。Erik自己要是没想过这题，面试30分钟，也不一定能写完O(m+n)解。难道面试官指望招得到比Erik Demaine还聪明的人？

```python
class Solution:
    
    def findPeakII(self, matrix) -> tuple:
        
        m, n, = len(matrix), len(matrix[0])
        
        lo, hi = 1, n-2
        while lo <= hi:
            mid = (lo+hi) // 2
            col_max, row_index = matrix[0][mid], 0
            for i in range(1, m-1):
                if matrix[i][mid] > col_max:
                    col_max = matrix[i][mid]
                    row_index = i 
            if matrix[row_index][mid] < matrix[row_index][mid-1]:
                hi = mid - 1
            elif matrix[row_index][mid] < matrix[row_index][mid+1]:
                lo = mid + 1
            else:
                return (row_index, mid)
```

# Dramy butterfly
二分版
这个题目有2个解法。 这里写一下简单一些的那个。 首先我们二分行而不是列。 找到一个mid以后， 我们从这一行里面， 找到最大的那个数。 那么可以确认的数， 这个数肯定比左右两边大。 然后比较一下这个数跟上下两边比。 如果比上下两边都大， 说明这个数直接就是peak， 直接return就好。 如果他比上面小， 就说明上面更大， 那么我们可以确定上面有我们要的答案， 下面可能也有， 但是不重要了， 咱们就把end变成mid。 下面同理即可。

然后就到了激动人心的幸福二选一环节了。 我这个比较暴力， 直接把这2行里面2个最大值找出来比一下， 大的那个， 肯定是答案。 原因呢？首先， 每一行的最大值， 肯定是比左右两边大的， 这个不用说。 另外说到上下， 那么大的那个， 都比另外一行最大的大了， 可能会比其他的小吗？不可能对不对。 然后我们二分的时候， 就确定了在这个start-end区间里面， 肯定是有答案的， 那么这2个数之一， 就一定有答案。 放心return吧

```python
class Solution:
    """
    @param A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            max_col = self.find_max_col(A[mid])
            if A[mid][max_col] > A[mid - 1][max_col] and A[mid][max_col] > A[mid + 1][max_col]:
                return mid, max_col
            
            if A[mid][max_col] < A[mid - 1][max_col]:
                end = mid
            else:
                start = mid
        max_col_start = self.find_max_col(A[start])
        max_col_end = self.find_max_col(A[end])

        return max_col_start if max_col_start > max_col_end else max_col_end

    def find_max_col(self, nums):
        max_num = -float('inf')
        max_index = -1
        for i in range(len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
                max_index = i
        return max_index
```
四分之一分版
随便画个十字， 其实就是长宽都取中点的那个十字就好， 然后看十字的横着和竖着的最大值在哪里， 他们2个共同定义的那个象限， 一定有peak。 举例， 如果十字中心点最大， 直接return。 如果横的最大值在坐标， 输的在上面， 那么就继续递归找左上。

# solution 2
方法1(O(nlogm)). 遍歷 1 < row < A.length - 1，用二分法找出每個row其peak的col值，再檢查是否 A[row][col] > A[row - 1][col] && A[row][col] < A[row + 1][col];
方法2(O(m + n)). 從任一個角落開始，我是用左上。接下來比較其右邊跟下邊的值，哪邊大往哪邊走。如果兩邊的值都小於當前值表示找到解。

```java
//方法1(O(nlogm))
public class Solution {
    /*
     * @param A: An integer matrix
     * @return: The index of the peak
     */
    public List<Integer> findPeakII(int[][] A) {
        if (A == null || A.length < 3 || A[0].length < 3) {
            return new ArrayList<>();
        }
        
        List<Integer> result = new ArrayList<>();
        // Scan horizontally
        for (int i = 1; i < A.length - 1; i++) {
            int j = findPeakH(A[i]);
            if (isPeakV(A, i , j)) {            // Check vertically
                result.add(i);
                result.add(j);
                break;
            }
        }
        return result;
    }
    
    private int findPeakH(int[] heights) {
        int start = 0;
        int end = heights.length - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (heights[mid] > heights[mid - 1]) {
                start = mid;
            } else {
                end = mid;
            }
        }
        return start;
    }
    
    private boolean isPeakV(int[][] A, int i, int j) {
        return A[i][j] > A[i - 1][j] && A[i][j] > A[i + 1][j];
    }
}


//方法2(O(m + n))
public class Solution {
    /*
     * @param A: An integer matrix
     * @return: The index of the peak
     */
    public List<Integer> findPeakII(int[][] A) {
        if (A == null || A.length < 3 || A[0].length < 3) {
            return new ArrayList<>();
        }
        
        int n = A.length;
        int m = A[0].length;
        // start from top - left
        int x = 1, y = 1;
        List<Integer> result = new ArrayList<>();
        while (x < n - 1 && y < m - 1) {
            if (A[x][y] > A[x + 1][y] && A[x][y] > A[x][y + 1]) {
                result.add(x);
                result.add(y);
                break;
            }
            
            if (A[x + 1][y] >= A[x][y + 1]) {
                x++;
            } else {
                y++;
            }
        }
        return result;
    }
}
```



# solution 3
递归方法解决，划十字，找出最大值，然后排除3/4的矩阵，向计算出来的方向进行搜索。O(m + n)
```python
DIRECTIONS = ((0, 1), (0, -1), (-1, 0), (1, 0))


class Solution:

    def findPeakII(self, A):
        return self.dfs(A, 1, len(A) - 2, 1, len(A[0]) - 2)

    def dfs(self, A, up, down, left, right):
        mid_x, mid_y = (up + down) // 2, (left + right) // 2
        x, y = mid_x, mid_y
        highest = A[x][y]

        for i in range(up, down + 1):
            if A[i][mid_y] > highest:
                highest = A[i][mid_y]
                x, y = i, mid_y
        for i in range(left, right + 1):
            if A[mid_x][i] > highest:
                highest = A[mid_x][i]
                x, y = mid_x, i

        is_peak = True
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if A[nx][ny] > A[x][y]:
                is_peak = False
                x, y = nx, ny
                break
        if is_peak:
            return [x, y]
        # serach in the pointed direction
        if up <= x < mid_x and left <= y < mid_y:
            return self.dfs(A, up, mid_x - 1, left, mid_y - 1)
        if up <= x < mid_x and mid_y < y <= right:
            return self.dfs(A, up, mid_x - 1, mid_y + 1, right)
        if mid_x < x <= down and left <= y < mid_y:
            return self.dfs(A, mid_x + 1, down, left, mid_y - 1)
        if mid_x < x <= down and mid_y < y <= right:
            return self.dfs(A, mid_x + 1, down, mid_y + 1, right)

        return []
```



# solution 4
解题思路
O(m+n) Time complexity
```python
class Solution:
    """
    @param A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        # write your code here
        m,n = len(A), len(A[0])
        nowx,nowy = m//2, n//2

        while True:

            if nowx + 1 < m and A[nowx+1][nowy] > A[nowx][nowy]:
                nowx += 1
            elif nowx - 1 >= 0 and A[nowx-1][nowy] > A[nowx][nowy]:
                nowx -= 1
            elif nowy + 1 < n and A[nowx][nowy+1] > A[nowx][nowy]:
                nowy += 1
            elif nowy - 1 >= 0 and A[nowx][nowy-1] > A[nowx][nowy]:
                nowy -= 1
            else:
                return [nowx, nowy]
```

# idea
![](https://i.postimg.cc/wT9GtfKK/Jiuzhang-vip-30days.png)
![](https://i.postimg.cc/Vvg4B8xx/Jiuzhang-vip-30days.png)
```java
public class Solution {
    /*
     * @param A: An integer matrix
     * @return: The index of the peak
     */
    public List<Integer> findPeakII(int[][] A) {
        // write your code here
        List<Integer> result = new ArrayList<>();
        if (A == null || A.length == 0 || A[0].length == 0){
            return result;
        }
        
        int startRow = 1, endRow = A.length - 2;
        while (startRow + 1 < endRow){
            int midRow = startRow + (endRow - startRow) / 2;
            int maxCol = findMaxCol(A[midRow]);
            if (A[midRow][maxCol] > A[midRow - 1][maxCol] && A[midRow][maxCol] > A[midRow + 1][maxCol]){
                result.add(midRow);
                result.add(maxCol);
                return result;
            }
            if (A[midRow - 1][maxCol] > A[midRow + 1][maxCol]){
                endRow = midRow - 1;
            } else {
                startRow = midRow + 1;
            }
        }
        
        int maxCol = findMaxCol(A[startRow]);
        if (A[startRow][maxCol] > A[startRow - 1][maxCol] && A[startRow][maxCol] > A[startRow + 1][maxCol]){
            result.add(startRow);
            result.add(maxCol);
            return result;
        }
        maxCol = findMaxCol(A[endRow]);
        result.add(endRow);
        result.add(maxCol);
        return result;
    }
    
    private int findMaxCol(int[] arr){
        int result = 0;
        
        for (int i = 1; i < arr.length; i++){
            if (arr[i] > arr[result]){
                result = i;
            }
        }
        
        return result;
    }
}
```