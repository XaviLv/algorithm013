class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """建议对照测试用例理解：
        [
                [2],
                [3,4],
                [6,5,7],
            [4,1,8,3]
        ]
        """
        if not triangle: return 0

        # way4: DP top-down 反过来考虑问题，从上到下的最小值，可以理解为：
        # 从最后一层任意位置到顶层的路径的最小值
        dp = [triangle[0][0]] * len(triangle[-1])
        for i in range(1, len(triangle)):
            # for j in range(0, i+1):
            for j in range(i, -1, -1):  # 此处一定要逆序访问！否则之前计算会覆盖上一步的状态值！
                if j == 0:
                    dp[j] = triangle[i][j] + dp[j]
                elif j == i:
                    dp[j] = triangle[i][j] + dp[j-1]
                else:
                    dp[j] = triangle[i][j] + min(dp[j], dp[j-1])
        return sorted(dp)[0]

        # way3: DP bottom-up 降维 dp 1维
        dp = triangle[-1]    # 联想fibonacci数列，仅需要保存上一层的状态，实现降维
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]

        # way2: DP bottom-up
        # 1. 找重复性（分治）2. 定义状态数组 3. 写DP方程
        # dp[i][j] = dp[i+1][j] + dp[i+1][j+1]
        dp = triangle
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + dp[i][j]
        return dp[0][0]

        # # way1: O(2^N), [超时] brute force, 每一层下探可以往左走、往右走
        # rows, cols = len(triangle), len(triangle[-1])
        # max_sum = float('inf')
        # def recursion(r, c, t):
        #     nonlocal max_sum
        #     if r == rows:
        #         max_sum = min(max_sum, t)
        #         return
        #     if c < 0 or c == cols:
        #         return
        #     recursion(r+1, c, t+triangle[r][c])
        #     recursion(r+1, c+1, t+triangle[r][c])
        # recursion(0, 0, 0) 
        # return max_sum