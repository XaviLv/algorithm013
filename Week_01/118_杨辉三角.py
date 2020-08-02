#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        # # 1. 二位数组记忆
        # output = list()
        # for i in range(numRows):
        #     tmp = []
        #     for j in range(i+1):
        #         if j == 0:
        #             tmp.append(1)
        #         elif j == i:
        #             tmp.append(1)
        #         else:
        #             tmp.append(output[i-1][j-1] + output[i-1][j])
        #     output.append(tmp)
        # return output

        # 2. 错位相加：其实这种方法只是利用python语言对上一种方案的另一种写法而已
        output = [[1]]
        for i in range(0, numRows-1):
            output.append([m[0]+m[1] for m in zip(output[i]+[0], [0]+output[i])])
        return output
# @lc code=end

