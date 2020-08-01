#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {(target-m): i for i, m in enumerate(nums)}
        for j, x in enumerate(nums):
            if x in mem and j != mem[x]:
                return [mem[x], j]
        return []
# @lc code=end

