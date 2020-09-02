class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # way2: dp: optimized 滚动数组
        if not obstacleGrid: return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols
        dp[0] = 1
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1: # 所有的grid都要接受此最基本条件的约束
                    dp[c] = 0
                elif c > 0:
                    dp[c] += dp[c-1]
        return dp[cols-1]


        # way1: dp: not optimized
        if not obstacleGrid: return 0
        if obstacleGrid[0][0] == 1: return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1
        for i in range(1, rows): 
            dp[i][0] = 0 if obstacleGrid[i][0] == 1 else dp[i-1][0]
        for j in range(1, cols):            
            dp[0][j] = 0 if obstacleGrid[0][j] == 1 else dp[0][j-1]
        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[rows-1][cols-1]