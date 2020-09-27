class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] 表示 以i开头j结尾 的字符串是否为回文，Boolean
        # dp[i][j] = (s[i] == s[j]) && (j - i < 2 || dp[i+1][j-1])
        ans, size, n = '', 0, len(s)
        dp = [[0] * n for _ in range(n)]
        if n < 2: return s
        for i in range(n, -1, -1):
            for j in range(i, n):
                dp[i][j] = (s[i] == s[j]) and (j - i < 2 or dp[i+1][j-1])
                if dp[i][j]:
                    if size < j-i+1:
                        size = j - i + 1
                        ans = s[i:j+1]
        return ans