class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        f(i,j) = f(i-1,j) + f(i,j-1)    if grid(i,j) == 0
        f(i,j) = 0
        """
        if not obstacleGrid or 1 in [obstacleGrid[0][0], obstacleGrid[-1][-1]]: 
            return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        # define dp
        dp = [[0] * cols for _ in range(rows)]
        # init dp
        dp[0][0] = 1
        for i in range(1, rows): dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
        for j in range(1, cols): dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
                else:
                    dp[r][c] = 0
        return dp[-1][-1]
