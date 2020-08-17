#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # iteration
        ans = [[]]
        for n in nums:
            new_ans = []
            for i in ans:
                new_ans.append(i + [n])
            ans.extend(new_ans)
        return ans

        # # recursion
        # ans, n, tmp = [], len(nums), []
        # def recursion(i):
        #     if i == n:
        #         # 一定要注意，如果使用外部的变量tmp，这里必须要deep copy！！！
        #         # 选择在 recursion 外面定义tmp，是为了节省内存
        #         ans.append([m for m in tmp])
        #         return
        #     recursion(i+1)
        #     tmp.append(nums[i])
        #     recursion(i+1)
        #     tmp.pop()
        # recursion(0)
        # return ans


# @lc code=end

