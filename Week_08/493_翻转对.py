class Solution:
    def reversePairs(self, nums):
        """ way1: 偷懒用 sorted 实现归并，用 bisect.bisect 搜索又侧数字的两倍在左侧的位置，
        被左侧数组长度一减就等于相对右侧某个数字的重要翻转对数
        """
        ans = 0
        def merge_sort(nums):
            nonlocal ans
            if len(nums) <= 1: # 不能写 == 0 否则死循环
                return nums
            mid = len(nums) >> 1
            left, right = merge_sort(nums[:mid]), merge_sort(nums[mid:])
            for i in right:
                add = len(left) - bisect.bisect(left, i * 2)
                if not add: # 说明 right 剩下的元素的 2 倍都不可能在 left 里
                    break
                ans += add
            return sorted(left + right) # left+right 和 nums 不同的是前者两部分已排过序，后者为排序，这对 sorted 效率影响较大
        merge_sort(nums)
        return ans
