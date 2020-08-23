#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board: return board
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        rows, cols = len(board), len(board[0])

        def valid_pos(r, c):
            return rows > r >= 0 and cols > c >= 0

        def BFS():
            queue = deque()
            queue.append(click)
            while queue:
                r, c = queue.popleft()
                # visited or search condition unqualified
                if board[r][c] != 'E':
                    continue
                m_cnt = 0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if (i == 0 and j == 0) or not valid_pos(r+i, c+j):
                            continue
                        if board[r+i][c+j] == 'M':
                            m_cnt += 1
                if m_cnt == 0:
                    board[r][c] = 'B'
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            if (i == 0 and j == 0) or not valid_pos(r+i, c+j):
                                continue
                            if board[r+i][c+j] == 'E':
                                queue.append([r+i, c+j])
                else:
                    board[r][c] = str(m_cnt)
            return board
        return BFS()


        # visited
        def DFS(r, c):
            # terminator & visited
            if not valid_pos(r, c) or board[r][c] != 'E':
                return
            # process current level
            m_cnt = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if (i == 0 and j == 0) or not valid_pos(r+i, c+j):
                        continue
                    if board[r+i][c+j] == 'M':
                        m_cnt += 1
            if m_cnt == 0:
                board[r][c] = 'B'
                # drill down, 注意！！只有当点周围没有雷时才继续递归
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if (i == 0 and j == 0) or not valid_pos(r+i, c+j):
                            continue
                        if board[r+i][c+j] == 'E':
                            DFS(r+i, c+j)
            else:
                board[r][c] = str(m_cnt)
            
            return board
        return DFS(click[0], click[1])

        
# @lc code=end

