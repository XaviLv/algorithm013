class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        dp
        1. 分治，找重复性
        2. 定义状态数组，找最优子结构
        3. 写状态方程
        fmax = max(fmax * cur, fmin * cur, cur)
        fmin = min(fmax * cur, fmin * cur, cur)
        """
        if not nums: return 0
        ans = dpmax = dpmin = nums[0]
        for i in range(1, len(nums)):
            fmax, fmin = dpmax, dpmin
            dpmax = max(fmax * nums[i], max(fmin * nums[i], nums[i]))
            dpmin = min(fmax * nums[i], min(fmin * nums[i], nums[i]))
            ans = max(dpmax, ans)
        return ans
