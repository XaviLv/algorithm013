#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def walk(pos, steps, direction):
            nonlocal dist
            for _ in range(steps):
                pos[0] += direction[0]
                pos[1] += direction[1]
                if tuple(pos) in obstacles:
                    pos[0] -= direction[0]
                    pos[1] -= direction[1]
                    break
            # many people ignore it's the max-distance that asked for
            dist = max(dist, pos[0]**2 + pos[1]**2)

        # [North, East, South, West], I think it's more clear to put in one line
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pos, dist, dir_idx = [0, 0], 0, 0
        obstacles = {tuple(m) for m in obstacles}
        for cmd in commands:
            if cmd == -1:
                dir_idx = (dir_idx + 1) % 4
            elif cmd == -2:
                dir_idx = (dir_idx + 3) % 4
            else:
                walk(pos, cmd, directions[dir_idx])       
        return dist     

        
# @lc code=end

