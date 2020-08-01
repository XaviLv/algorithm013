#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 双指针
        p, q, n = 1, 1, len(nums)
        while q < n:
            if nums[q-1] != nums[q]:
                nums[p] = nums[q]
                p += 1
            q += 1
        return p
# @lc code=end

