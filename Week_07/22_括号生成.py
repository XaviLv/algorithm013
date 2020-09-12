class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """way2: DP 找重复性（分治）、最优子结构（定义状态数组）、写状态方程
        求 i 个括号对，可以分解如下：
        先提取一对括号（），剩下 i-1 对括号，我们可以在预先提取的括号内放置 x 对括号，在它右边放置 y 对括号，显然：
        x + y == i-1，其中 x 从 0～i-1
        我们定义 dp[i] 为 i 对括号对所有可能有效组合
        """
        # 1. 初始化dp数组
        dp = [[] for _ in range(n+1)]
        dp[0] = ['']
        # 2. 状态方程
        for i in range(1, n+1):  # n 对括号
            for j in range(i):  # i-1 对括号所有可能的组合
                for x in dp[j]:
                    for y in dp[i-1-j]:
                        dp[i].append('(' + x + ')' + y)
        return dp[n]

        """way1: 回溯+剪枝
        """
        ans = []
        def gen(tmp, l, r):
            if l + r == n * 2:
                ans.append(tmp)
                return
            if l < n:
                gen(tmp + '(', l + 1, r)
            if r < n and r < l:
                gen(tmp + ')', l, r + 1)
        gen('', 0, 0)
        return ans

