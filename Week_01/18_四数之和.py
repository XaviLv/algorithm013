class Solution:
    def fourSum(self, nums, target):
        """注意多层循环的区间
        """
        if not nums: return []
        # 升序排列方便后续去重计算
        nums.sort()
        ans, n = [], len(nums)
        # 注意区间边界 n-3，正常是 range(0, n)，由于后面还有三个数字，因此要至少留三个位置，即 n-3
        for i in range(0, n-3):
            # 去重，注意有效边界 n-3 > i > 0
            while n-3 > i > 0 and nums[i] == nums[i-1]: i += 1
            # 如果当前值重复4次的和大于target，说明有序数组nums后面不可能有解
            if nums[i] * 4 > target: break
            # 注意左边界是 i+1
            for j in range(i+1, n-2):
                while n-2 > j > i+1 and nums[j] == nums[j-1]: j += 1
                if nums[j] * 3 > target - nums[i]: break
                # 左右边界夹逼操作
                l, r = j+1, n-1
                tmp = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == tmp:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        # 注意添加 l < r，跳过连续相同值
                        while l < r and nums[l+1] == nums[l]: l += 1
                        while l < r and nums[r-1] == nums[r]: r -= 1
                        l, r  = l + 1, r - 1
                        # 根据结果相对于target的大小，移动left or right
                    elif nums[l] + nums[r] < tmp:
                        l = l + 1
                    else:
                        r = r - 1
        return ans  


if __name__ == "__main__":
    sol = Solution()
    test_cases = [[-2,-1,-1,1,1,2,2]]
    for case in test_cases:
        print(case, sol.fourSum(case, 0))