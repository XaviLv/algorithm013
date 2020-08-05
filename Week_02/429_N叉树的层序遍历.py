#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """1/5
        注意：这里的 children 是一个 iterable 的结构
        切题四件套：clarification / possible solutions / code / test cases
        """
        if not root: return []
        q0, q1 = deque(), deque()
        q0.append(root)
        ans, tmp = [], []
        while len(q0) > 0:
            node = q0.popleft()
            if node:
                tmp.append(node.val)
                q1.extend(node.children)
            if len(q0) == 0:
                ans.append(tmp)
                tmp = []
                q0, q1 = q1, q0

        return ans
# @lc code=end

