# 学习笔记 / Week04

|Time|Version|Note|
|---|---|---|
|08/21|0.0.1|draft|

<br/>

> Keep每天看100遍，肌肉也长不起来！重复遍数最重要！
> <p align="right">—— week4 五毒神掌</p>

<br/>

## 代码模版

### 1. DFS - 深度优先搜索

**<p align="middle">DFS != 递归</p>**

深度优先只是一种搜索的方式，或者说遍历的方向，而递归是一种编程范式。DFS可以用递归和非递归（**栈**）两种方法来实现。

```python
# DFS / Recursion
visited = set()
def DFS(node):
    if node in visited: return  # terminator
    visited.add(node)  # update visited
    process(node)  # current level
    for next_node in node.children():  # drill down
        if next_node not in visited:
            DFS(next_node)
```
```python
# DFS / Iteration
def DFS(tree)
    if tree.root is None: return []
    visited, stack = [], [tree.root]
    while stack:
        node = stack.pop()
        visited.add(node)
        process(node)
        nodes = generated_related_nodes(node)
        stack.push(nodes)   # 栈尾插入，和BFS不同
    process_output()
```

### 2. BFS - 广度优先搜索

广度优先搜索一般用非递归（**队列**）实现。

```python
# BFS / iteration
def BFS(graph, start, end):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop()
        visited.add(node)
        process(node)
        nodes = generate_related_nodes(node)
        queue.insert(0, nodes)  # 队首插入，和DFS不同
    process_output()
```