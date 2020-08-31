#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # [North, East, South, West], I think it's more clear to put in one line
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        idx, pos, dist = 0, [0, 0], 0
        obstacles = set([tuple(m) for m in obstacles])
        for cmd in commands:
            if cmd == -1:
                idx = (idx + 1) % 4
            elif cmd == -2:
                idx = (idx + 3) % 4
            else:
                for _ in range(cmd):
                    pos[0] += directions[idx][0]
                    pos[1] += directions[idx][1]
                    if tuple(pos) in obstacles:
                        pos[0] -= directions[idx][0]
                        pos[1] -= directions[idx][1]
                        break
                dist = max(dist, pos[0]**2 + pos[1]**2)
        return dist
        
# @lc code=end
