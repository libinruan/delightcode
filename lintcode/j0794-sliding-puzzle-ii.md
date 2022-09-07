![9-6-6-54](https://i.postimg.cc/rFpcmpF2/2022-09-06-at-06-54-34.png)
For convenience, we tranlate 2D array into one-dimentional array, either string or integer.

![9-6-6-56](https://i.postimg.cc/gj7Yd9hZ/2022-09-06-at-06-56-43.png)
Create a subfunction to obtain the neighboring nodes.

![](https://i.postimg.cc/bJzTMLND/2022-09-06-at-16-51-43.png)

2:07:15

```python
def minMoveStep(self, init_state, final_state):
    source = self.matrix_to_string(init_state)
    target = self.matrix_to_string(final_state)

    from collections import deque
    queue = deque([soure])
    distance = {source: 0}

    while queue:
        current = queue.popleft()
        if current == target:
            return distance[current]

        for next in self.get_next(current):
            if next in distance:
                continnue
            queue.append(next)
            distance[next] = distance[current] + 1
    return -1

def matrix_to_string(self, state):
    str_list = []
    for i in range(3):
        for j in range(3):
            str_list.append(str(state[i][j]))
    return "".join(str_list) 


def get_next(self, state):
    states = []
    direction = ((0, 1), (1, 0), (-1, 0), (0, -1))
    zero_index = state.find('0')
    x, y = zero_index // 3, zero_index % 3

    for i in range(4):
        next_x, next_y = x + direction[i][0], y + direction[i][1]
        if 0 <= next_x < 3 and 0 <= next_y < 3:
            next_state = list(state)
            next_state[x * 3 + y] = next_state[next_x * 3 + next_y]
            next_state[next_x * 3 + next_y] = '0'
            states.append("".join(next_state))
    return states
```

# Bidirectional BFS
![](https://i.postimg.cc/MTX3S36L/2022-09-07-at-00-07-01.png)
![](https://i.postimg.cc/B6xLX4nP/2022-09-07-at-00-08-15.png)
![](https://i.postimg.cc/MTf5ksBt/2022-09-07-at-06-41-22.png)

面试的时候，一定要由简入繁，bidirectional BFS要会但不要一上来就用，除非面试关主动要求，毕竟变形比较复杂，从简单的做起，稳扎稳打。

![](https://i.postimg.cc/65f2YDqw/2022-09-07-at-06-49-11.png)

Complexity: $$O(\sqrt{k})$$. It's becasue the original complexity is $$O(1+k+K^2+...+K^n) \sim O(k^n).$$ The improved version's complexity is $$O(1+k+K^2+...+K^{n/2})\sim O(k^{n/2}).$$

![](https://i.postimg.cc/yxmmhjkN/2022-09-07-at-06-51-46.png)


