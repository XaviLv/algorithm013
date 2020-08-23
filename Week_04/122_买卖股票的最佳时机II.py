#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """已开天眼，直到第二天的价格"""
        if not prices: return 0
        n, cnt = len(prices), 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                cnt += prices[i] - prices[i-1]
        return cnt

        
# @lc code=end

