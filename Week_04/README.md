# 学习笔记 / Week04

|Time|Version|Note|
|---|---|---|
|08/21|0.0.1|draft|

<br/>

> Keep每天看100遍，肌肉也长不起来！重复遍数最重要！
> <p align="right">—— week4 五毒神掌</p>

<br/>

---

## 1. 代码模版

BFS(Breadth First Search) 和 DFS(Depth First Search) 的本质：**找重复性！找重复性！找重复性！**

*<p align="middle">DFS != 递归</p>*

深度优先只是一种搜索的方式，或者说遍历的方向，而递归是一种编程范式。DFS可以用递归和非递归（**栈**）两种方法来实现。

看到下面的模板，我的第一反应就是：这和前两周说的递归模板怎么这么像？有啥不同的吗？！！仔细一看发现最大的不同有两部分：

1. visited

* 作用：防止重复访问（树的遍历不需要该变量，图检索时需要）

* 技巧：visited 通常是会造成 O(N) 的额外存储开销，因此有时可以直接修改题目的源数据，替代 visited，起到防止重复访问的作用。经典案例：岛屿数量。

2. drill down

* 不同：注意到模板中的 node.children 以及 generated_related_nodes() 不再是 node.left, node.right。也就是在递归或迭代的过程中，要根据条件判断的结果决定下一层要访问的节点。

* 思考：<font color="yellow">DFS是一种搜索思想，递归是一种编程范式。前者是思维，后者是工具。</font>


### DFS - 深度优先搜索

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
def DFS(root)
    if root is None: return []
    visited, stack = [], [root]
    while stack:
        node = stack.pop()
        visited.add(node)
        process(node)
        nodes = generated_related_nodes(node)
        stack.push(nodes)   # 栈尾插入，和BFS不同
    process_output()
```

### BFS - 广度优先搜索

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

## 2. 习题心得

有些题目未必会问得那么直接，我们训练眼力迅速联想到本质问题。比如：

* 括号生成 - *联想* - 递归状态树
* 一般问题 - <font color="yellow">抽象</font> - 特殊问题



