# 学习笔记 / week09

|Time|Version|Note|
|---|---|---|
|09/27|0.1.0|stable|

## 一、习题

[63. 不同路径II](https://leetcode-cn.com/problems/unique-paths-ii/)
```python
# 状态转移方程
f(i,j) = f(i-1,j) + f(i,j-1) if grid(i,j) == 0 else 0
```

## 二、模板（动规/递归/分治）

**Recursion / 递归**
```python
def recursion(level, param):
    # terminator
    if level > MAX_LEVEL:
        # process result
        return
    # current level
    process(level, param)
    # drill down
    recursion(level+1, param)
    # revert current status (if necessary)

```

**Divide&Conquer / 分治**

典型应用：merge sort

```python
def divide_conquer(problem, param1, param2, ...):
    # terminator
    if problem is None:
        # process result
        return
    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)
    # conquer subproblems
    subresult1 = divide_conquer(subproblems[0], param1, ...)
    subresult2 = divide_conquer(subproblems[1], param1, ...)
    subresult3 = divide_conquer(subproblems[2], param1, ...)
    ...
    # process and generate the final result
    result = process_result(subresult1, subresult2, ...)
    # revert
```

**Dynamic Programming / 动态规划**

本质：分治+最优子结构

方式：bottom-up（顺推）；从子问题的最优解推导整个问题的最优解。[*PS: 记忆化搜索：top-down*]

难点：
1. dp状态数组的定义，需要经验把实际问题抽象成保存状态的数组；
2. 状态转移方程怎么写。

DP vs. Recursion/DivideConquer
* 共性：找重复性；
* 差异：DP有最优子结构，中途可以淘汰次优解。

```python
def DP_func():
    # define dp array, n-dimension
    dp = [][]
    # write dp formula
    for i in range(0, m):
        for j in range(0, n):
            dp[i][j] = _func(dp[i-x][j-y], ...)
    # return result
    return dp[-1][-1]
```

## 字符串

**基础**

* Python/Java/JS/Go/C# 中字符串是 immutable（不可变） 的，当添加或删除一个字符时，实际上是新创建了一个字符串，原来的 string 还是原来的内容；
* C++/Ruby/PHP/Swift 中字符串是 mutable（可变）的，C++ 中可以通过 const 实现不可变，Swift 中类似可通过 let 关键字使其 immutable；
* immutable 的好处是线程安全；
* Java 中两个字符串x、y，用 x == y 判断的是 x 和 y 的引用是否相等，不是判断 x 和 y 的内容是否相等；


**字符串匹配高级算法**

* 在暴力搜索（brute force）的基础上优化：枚举每个起点时，txt 的片段和整个 pattern 如何快速比较，并且 pattern 能够快速移动，而不用按字符挨个移动。
* Rabin-Karp：hash(txt.substring(i, M)) == hash(pat)
* KMP：Knuth-Morris-Prat，当子串与模式串不匹配时，利用已知的信息尽可能的往后移动。