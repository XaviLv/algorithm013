class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parents = [i for i in range(n)]
    
    def find(self, p):
        root = p
        # find root
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
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M: return 0
        n = len(M)
        friends = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    friends.union(i, j)
        return friends.count
