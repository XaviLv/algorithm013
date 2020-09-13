class UnionFind:
    def __init__(self, m, n, grid):
        self.count, self.parents = 0, dict()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    self.parents[r * n + c] = r * n + c
                    self.count += 1

    def find(self, p):
        # find root
        root = p
        while root != self.parents[root]:
            root = self.parents[root]
        # 路径压缩
        while p != self.parents[p]:
            p, self.parents[p] = self.parents[p], root
        return root

    def union(self, p, q):
        p0 = self.find(p)
        p1 = self.find(q)
        if p0 != p1:
            self.parents[p0] = p1
            self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        dx = [0, 1]
        dy = [1, 0]
        islands = UnionFind(m, n, grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                cur = i * n + j
                for x, y in zip(dx, dy):
                    nb = (x + i) * n + (y + j)
                    if m > x+i >= 0 and n > y+j >=0 and grid[x+i][y+j] == '1':
                       islands.union(cur, nb)

        return islands.count

