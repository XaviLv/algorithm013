#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针
        # p指向可以放置的位置，q指向非0元素
        p, q, n = 0, 0, len(nums)
        while q < n:
            if nums[q] != 0:
                nums[p], nums[q] = nums[q], nums[p]
                p += 1
            q += 1
# @lc code=end

