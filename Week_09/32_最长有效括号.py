class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        dp[i] 表示以 i 位置结尾的有效括号数量
        """
        def find_max(sequence, left_sign):
            # i 表示每个匹配序列中第一个左括号，j 表示最后一个右括号
            ans, left, right, i = 0, 0, 0, 0
            for j, c in enumerate(sequence):
                if c == left_sign: 
                    left += 1
                else: 
                    right += 1
                if left == right:
                    ans = max(ans, j - i + 1)
                elif right > left:
                    left = right = 0
                    i = j + 1
            return ans

        x = find_max(s, left_sign='(')
        y = find_max(s[::-1], left_sign=')')
        return max(x, y)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [")()())", '(()', '())', '(())())', '()(())', '', '(', '))', '((']
    for s in test_cases:
        res = sol.longestValidParentheses(s)
        print(s, res)