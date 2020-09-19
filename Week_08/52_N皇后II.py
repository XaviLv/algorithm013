class Solution:
    def totalNQueens(self, n: int) -> int:
        """位运算
        用整数记录每一行哪些位置已被占用，注意递归时每一层只专注于当层数据的处理。
        整数：cols, pie, na，用bit位表示哪些位被占用
        """
        ans = 0
        def DFS(row, cols, pie, na):
            nonlocal ans
            if row == n:
                ans += 1
                return
            # 取反再截断，获得当前层（row）可以放置的位置
            bits = ~(cols | pie | na) & ((1 << n) - 1)
            while bits:
                # x & -x 表示从右往左数第一个 1 所在位置
                p = bits & -bits
                # x & (x-1) 表示从右往左数第一个 1 所在位置清零
                bits = bits & (bits - 1)
                # 递归调用，pie每往下一层其占用的列将左移一位，同理na占用的列将右移一位
                DFS(row+1, cols | p, (pie | p) << 1, (na | p) >> 1)
        DFS(0, 0, 0, 0)
        return ans