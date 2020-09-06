# 学习笔记 / Week06

|Time|Version|Note|
|---|---|---|
|09/02|0.0.1|draft|
|09/06|0.1.0|stable|

<br/>

> Dynamic Programming 三步走:
> 1. 分治，找重复子问题（最优子结构）
> 2. 画状态图，表示状态空间（状态数组）
> 3. 归纳状态方程
> <p align="right">—— week6 动态“递推”</p>

一把辛酸一把泪啊，搞不过遗忘曲线！过遍数真的是最重要的！

<br/>

### 谈谈这周学习 DP 后的重新认知

- 动态规划，实则动态递推，即动态地构建状态数组并用前一层的状态（归纳地）递推当前层的状态。顺序，优先考虑 bottom-up 方法，也不懒于锻炼 top-down 的思维。勤加练习，方能烂熟于心。面试的难点一般是 定义状态数组 和 构建状态方程（组）。一般可根据问题直接抽象状态数组，优化时通常可将状态数组降一维。相关题目：爬楼梯（fibonacci）、不同路径。

- 动规三步走：1. 分治（找重复性）；2. 定义状态数组（找最优子结构)；3. 写状态方程。

- 其中，第一步分治有两种思路：top-down 和 bottom-up。后者（bottom-up）如果习惯分治思路的话很自然地可以理解。分治的思想是利用下一层的子问题解决当前层的问题，为了避免递归，降低复杂度（如果是二分问题，则时间复杂度是O(2^N)），直接一步到位下探到最底层，然后逐层向上递推，就像在模拟函数出栈或者递归返回。这样做，因前一层的状态已知，则可以直接计算当前层。1维问题，时间复杂度一般可以优化到 O(N)；2维问题，时间复杂度则可至 O(M*N)。


### 第一次写题解：最大子序和

[最大子序和](https://leetcode-cn.com/problems/maximum-subarray/solution/dp-top-downbottom-up-by-lw2406/)

Dynamic Programming：动态规划，如果进一步翻译成“动态递推”，再结合它的三板斧就能逐渐理解其含义：
- 分治：找重复性；
- 定义状态数组，找最优子结构；
- 写状态方程。

DP 与分治没有本质的区别，我理解 DP 是分治的优化思路，不用保存所有的状态，用上一层的状态计算当前层，并不断淘汰次优解。一般可使用 top-down 或 bottom-up 思路完成。其中：

**top-down**：相当于直接下探到分治的最底层，再一层层往上递推；
**bottom-up**：则反过来考虑问题，比如这题可定义 dp[i] 为以 nums[i] 结尾。

- Top-down
```python
# top-down：dp[i] 表示以 nums[i] 结尾的子序列
def maxSubArray(self, nums: List[int]) -> int:
    if not nums: return 0
    ans = dp = nums[0]
    for i in range(1, len(nums)):
        dp = max(dp+nums[i], nums[i])
        ans = max(dp, ans)
    return ans
```

- Bottom-up
```python
# bottom-up：dp[i] 表示以 nums[i] 开头的子序列
# 自底向上就是分治（递归）直接到最底层，然后人肉向上递推。
def maxSubArray(self, nums: List[int]) -> int:
    if not nums: return 0
    ans = dp = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        dp = max(dp+nums[i], nums[i])
        ans = max(dp, ans)
    return ans
```
DP 是一种思维，结合分治和数学归纳法，多练多想。

![动态规划](xmind/动态规划.png)

[--> 图片加载不出来看这里](https://blog.csdn.net/outman_1921/article/details/106595472)