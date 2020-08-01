#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """50%
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        if k >= 0:
            while i >= 0:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            while j >= 0:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
# @lc code=end

