#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """1/5"""
        def DFS(i, j):
            nonlocal count
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0': return
            grid[i][j] = '0'    # 直接修改grid就不再需要visited记录了
            DFS(i, j+1)
            DFS(i, j-1)
            DFS(i+1, j)
            DFS(i-1, j)

        count, m = 0, len(grid)
        if m == 0: return 0
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    DFS(i, j)                    
                    count += 1  # 注意记录的是岛屿的数量，不是1的数量
        return count



# @lc code=end

