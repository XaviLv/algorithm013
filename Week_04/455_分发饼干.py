#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        m, n = len(g), len(s)
        while i < m and j < n:
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i
# @lc code=end

