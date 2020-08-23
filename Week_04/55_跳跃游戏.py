#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1: return True
        endReachable = len(nums) - 1
        i = len(nums) - 2
        while i >= 0:
            if nums[i] + i >= endReachable:
                endReachable = i
            i -= 1
        return endReachable == 0

# @lc code=end

