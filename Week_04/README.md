# 学习笔记 / Week04

|Time|Version|Note|
|---|---|---|
|08/21|0.0.1|draft|

<br/>

> Keep每天看100遍，肌肉也长不起来！重复遍数最重要！
> <p align="right">—— week4 五毒神掌</p>

<br/>

---

<br/>

### DFS / BFS

**1. 要点**

BFS(Breadth First Search) 和 DFS(Depth First Search) 的本质：**找重复性！找重复性！找重复性！**

*<p align="middle">DFS != 递归</p>*

深度优先只是一种搜索的方式，或者说遍历的方向，而递归是一种编程范式。DFS可以用递归和非递归（**栈**）两种方法来实现。

看到下面的模板，我的第一反应就是：这和前两周说的递归模板怎么这么像？有啥不同的吗？！！仔细一看发现最大的不同有两部分：

Visited

* 作用：防止重复访问（树的遍历不需要该变量，图检索时需要）

* 技巧：visited 通常是会造成 O(N) 的额外存储开销，因此有时可以直接修改题目的源数据，替代 visited，起到防止重复访问的作用。经典案例：岛屿数量。

Drill down

* 不同：注意到模板中的 node.children 以及 generated_related_nodes() 不再是 node.left, node.right。也就是在递归或迭代的过程中，要根据条件判断的结果决定下一层要访问的节点。

* 思考：<font color="yellow">DFS是一种搜索思想，递归是一种编程范式。前者是思维，后者是工具。</font>

**2. 模板（DFS）**

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

**3. 模板（BFS）**

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

<br/>

### 贪心算法

在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的算法。

**1. 贪心算法 vs 动态规划**

贪心对于每个子问题的解决方案都做出选择，不能回退；动规则会**保存以前的运算结果**，并根据以前的结果对当前进行选择，有回退功能。

* 贪心：当下做局部最优判断
* 回溯：能够回退
* 动规：最优判断 + 回退（带最优判断的回溯）

**2. 要点**

贪心算法，尤其最基础的贪心，每次找当前情况的最优并不能达到全局最优。但某些时候可以用贪心解决一些最优化问题，比如：求图中的最小生成树、求哈夫曼编码等。或者，有时可以局部使用贪心，配合全局的其他策略。

一旦一个问题可通过贪心来解决，那贪心一般是解决这个问题的最好办法。由于贪心算法的高效性以及其求解的答案比较接近最优结果，因此也可以用作辅助算法或直接解决一些要求结果不特别精确的问题。

<font color="yellow">**难点：怎么证明目标问题可以通过贪心解决，以及贪心的角度（有时需要把问题转换一下；有时从前往后贪心，有时从后往前贪心）**</font>

比如跳跃游戏1、2，需要对贪心算法的使用稍加变形：

* [55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/)：从数组的尾部向前贪婪寻找；

* [45. 跳跃游戏II](https://leetcode-cn.com/problems/jump-game-ii/)：从数组的头部向后贪婪寻找，但每次都要找当前位置可达的区间内，能够二次阶跃到的最远跳。

**3. 使用贪心算法的场景**

问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。—— 最优子结构

**再次强调**

* 贪心对于它的每个子问题的解决方案都做出选择，且不能回退；
* 动态规划会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

### 其他

有些题目未必会问得那么直接，我们训练眼力迅速联想到本质问题。比如：

* 括号生成 - *联想* - 递归状态树
* 一般问题 - <font color="yellow">抽象</font> - 特殊问题



