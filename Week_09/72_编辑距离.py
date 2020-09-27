class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """字符串匹配 DP
        通常，把两个要比较的字符串写在矩阵的行列两侧，以此构造2维状态方程
        """
        # 边界条件
        m, n = len(word1), len(word2)
        if m * n == 0: return m + n
        # 定义状态数组并初始化
        dp = [[0] * (n + 1) for _ in range(m+1)]
        for i in range(m+1): dp[i][0] = i
        for j in range(n+1): dp[0][j] = j
        # 定义状态方程
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:    # 不要越界
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]