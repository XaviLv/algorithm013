#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]
        i, j, k = 0, 0, 0
        while n > 1:
            a, b, c = 2*ans[i], 3*ans[j], 5*ans[k]
            tmp = min([a, b, c])
            if tmp == a: i += 1
            if tmp == b: j += 1
            if tmp == c: k += 1
            ans.append(tmp)
            n -= 1
        return ans[-1]
# @lc code=end

