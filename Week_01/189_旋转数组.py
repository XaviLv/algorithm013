#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # 1. 3次旋转
        def swap(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        swap(nums, 0, len(nums)-1)
        swap(nums, 0, k-1)
        swap(nums, k, len(nums)-1)
# @lc code=end

