class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
    def find(self, p):
        # find root
        root = p
        while root != self.parents[root]:
            root = self.parents[root]
        # compress path
        while p != self.parents[p]:
            p, self.parents[p] = self.parents[p], root
        return root
    def union(self, p, q):
        p0 = self.find(p)
        p1 = self.find(q)
        if p0 != p1:
            self.parents[p0] = p1
    def connected(self, p, q):
        return self.find(p) == self.find(q)



class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
                
        def index(i, j):
            return i * n + j + 1

        # union find
        if not board: return
        m, n = len(board), len(board[0])
        # 多创建一个 dummy node，作为所有边界上的 'O' 的虚拟节点
        disjoint = UnionFind(m * n + 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i in [0, m-1] or j in [0, n-1]:
                        disjoint.union(index(i, j), 0)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            _x, _y = x + i, y + j
                            if board[_x][_y] == 'O':
                                disjoint.union(index(i, j), index(_x, _y))
        # result
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if not disjoint.connected(index(i, j), 0):
                        board[i][j] = 'X'

