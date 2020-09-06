class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """字符串匹配 DP
        通常，把两个要比较的字符串写在矩阵的行列两侧，以此构造2维状态方程
        """
        m, n = len(word1), len(word2)
        if m * n == 0: return m + n

        # 定义状态数组
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # 初始化状态数组
        for r in range(m+1): dp[r][0] = r
        for c in range(n+1): dp[0][c] = c

        # 定义状态转移方程
        for r in range(1, m+1):
            for c in range(1, n+1):
                if word1[r-1] != word2[c-1]:
                    dp[r][c] = min(dp[r-1][c-1]+1, min(dp[r][c-1]+1, dp[r-1][c]+1))
                else:
                    dp[r][c] = min(dp[r-1][c-1], min(dp[r][c-1]+1, dp[r-1][c]+1))
        return dp[m][n]
