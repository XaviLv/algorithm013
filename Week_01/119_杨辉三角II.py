#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # array = [0] * (k+1)
        if rowIndex == 0:
            return [1]
        array = [1]
        for i in range(rowIndex):
            array = [m[0] + m[1] for m in zip(array + [0], [0] + array)]
        return array


# @lc code=end

