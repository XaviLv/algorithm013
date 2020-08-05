#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return[]
        sdict = dict()
        for m in nums:
            sdict[m] = sdict.get(m, 0)
            sdict[m] += 1
        # 1. 统计词频，排序 O(NlogN)，不满足题目对于时间复杂度的要求
        # 2. 统计词频，堆 O(logN)
        h = []
        for key, val in sdict.items():
            heappush(h, (val, key))
            if len(h) > k:
                heappop(h)
        return [m[1] for m in h]
# @lc code=end

