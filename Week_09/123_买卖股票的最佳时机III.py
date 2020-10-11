class Solution:
    def maxProfit(self, prices):
        """股票问题通用dp解法

        状态定义：
            dp[i][j][0]  # 在第 i 天剩余可交易次数 j 且持有股票数为 0 时，所能获取的最大利润；
            dp[i][j][1]  # 在第 i 天剩余可交易次数 j 且持有股票数为 1 时，所能获取的最大利润。
        操作选择：
            买入、卖出、休息（buy, sell, rest）
        转移方程：
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
            dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][1] - prices[i])
            解释：
            dp[i][j][1] + prices[i] 表示在第 i 天卖出股票（一支），所以进账 prcies[i]；
            dp[i][j-1][1] - prices[i] 表示在第 i 天买入股票（一支），所以出账 prices[i]，且因为消耗了一次交易，因此前 i-1 天仅剩 j-1 次交易次数。
        状态初始化：
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]
            dp[i][0][0] = 0
            dp[i][0][1] = -prices[0]
            解释：# 如果在 j==0 天卖出，则利润 +prices[0]，而实际上不可能第 0 天卖出任何股票，所以利润只能为 0。为保证状态转移的完整性，当 i == 0 or j == 0 且持有股票数为 1 时，状态值初始化为 -prices[0]。

            针对不同的股票问题，可对状态方程做简化处理。
        """
        if not prices: return 0
        n, k = len(prices), 2
        # 定义状态数组
        dp = []
        for i in range(n):
            dp.append([])
            for j in range(k+1):
                dp[-1].append([0, 0])
        # 初始化状态数组
        for j in range(1, k+1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]
        # 定义状态方程
        for i in range(1, n):
            for j in range(k, 0, -1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[-1][-1][0]


sol = Solution()
test_cases = [
     [3,3,5,0,0,3,1,4],
     [1,2,3,4,5],
     [7,6,4,3,1]
]
for case in test_cases:
    print(case, sol.maxProfit(case))
