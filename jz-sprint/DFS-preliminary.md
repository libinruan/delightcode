# Intro
DFS
1. divide and conquer
2. recursive

Its purpose: to translate a big probelm into many small problems.

The three elements of DFS:
1. Definition.
```python
def dfs(self, root):
```
2. Exception (exit condition).
```pytohn
def dfs(self, root):
    if not root: return [0, 0]  # the max length of chain, the max diameter.
```
3. Subquestion.