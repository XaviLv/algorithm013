class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        1. brute force: 列举所有连续子数组，比较最大值 O(N^2)
        2. DP
            a. 分治（找重复性）
            b. 定义状态数组：dp[i] 表示以 nums[i] 结尾或开头的子序列的最大和
            c. 写状态方程：
                以 nums[i] 结尾：dp[i] = max(dp[i-1] + nums[i], nums[i])
                以 nums[i] 开头：dp[i] = max(dp[i+1] + nums[i], nums[i])
        """
        if not nums: return 0

        # bottom-up：dp[i] 表示以 nums[i] 开头的子序列
        # 自底向上就是分治（递归）直接到最底层，然后人肉向上递推。
        ans = dp = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            dp = max(dp+nums[i], nums[i])
            ans = max(dp, ans)
        return ans

        # # top-down：dp[i] 表示以 nums[i] 结尾的子序列
        # ans = dp = nums[0]
        # for i in range(1, len(nums)):
        #     dp = max(dp+nums[i], nums[i])
        #     ans = max(dp, ans)
        # return ans
