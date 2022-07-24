# 排序，中位数，根据题意，完全可以无视每个点的y坐标
# 所有点到达马路的直线距离为垂直距离，想要让每个点到马路的路程和最小那么马路一定在中位数上
# 如果有奇数个点，则马路处于那个电上，如果有偶数个点，马路在中位数的两个端点之间，
# 复杂度O(nlogn)

# answer 1.
# https://www.lintcode.com/problem/1323/solution/32567
class Solution:
    """
    @param coordinates: a series of coordinates (x, y)
    @return: Given a series of coordinates (x, y),return the shortest sum of distance
    """
    def Fetchsupplies(self,coordinates):
        if len(coordinates) == 0:
            return 0;
        tmp = []
        for coordinate in coordinates:
            tmp.append(coordinate[0])
        tmp = sorted(tmp)
        size = len(tmp)
        mid = 0
        if size % 2 == 0:
            l = int(size / 2 - 1)
            r = l + 1;
            mid = (tmp[l] + tmp[r]) / 2
        else:
            mid = tmp[int((size - 1) / 2)]
        ans = 0
        for i in range(size):
            ans += math.fabs(tmp[i] - mid)
        return int(ans)



# answer 2.
class Solution:
    """
    @param coordinates: a series of coordinates (x, y)
    @return: Given a series of coordinates (x, y),return the shortest sum of distance
    """
    def Fetchsupplies(self, coordinates):
        # write your code here
        coordinates.sort(key = lambda x:x[0])
        length = len(coordinates)
        index = 0
        gap = 1
        distance = 0
        if length % 2 == 0:
            index = length // 2
        else:
            index = (length+1) // 2
            gap = 2
        for i in range(index,length):
            distance += (coordinates[i][0]-coordinates[i-gap][0])
            gap += 2
        return distance