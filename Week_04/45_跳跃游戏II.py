#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums: return 0
        
        # way1: 从数组的头部向后贪婪寻找，
        # 但每次都要找当前位置可达的区间内，能够二次阶跃到的最远跳。
        end, max_pos, step = 0, 0, 0
        for i in range(len(nums)-1):
            max_pos = max(max_pos, nums[i] + i)
            if i == end: # 已检索完当前可达区间的二次阶跃情况
                step += 1
                end = max_pos
        return step

        # way2: time exceeded
        # 每个位置向后可达的坐标
        nexts = [i+nums[i] for i in range(len(nums))]
        i = len(nums) - 1
        step = 0
        while i > 0:
            for j in range(0, i):
                if j + nums[j] >= i:
                    i = j
                    step += 1
                    break
        return step
        
# @lc code=end

