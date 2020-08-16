#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        ans = []
        for i in range(len(nums)):
            ans.extend([m + [nums[i]] for m in self.permute(nums[:i] + nums[i+1:])])
        return ans
# @lc code=end

