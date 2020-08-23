#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """way1: DFS"""
        res = []
        def DFS(level, node):
            # terminator
            if not node: return
            # current level
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            # drill down
            DFS(level+1, node.left)
            DFS(level+1, node.right)
        # 好几次了！不要忘记总的调用入口！
        DFS(0, root)
        return res

        # """BFS"""
        # def BFS():
        #     if not root:  return []
        #     # initialize queue
        #     queue, res = deque(), []
        #     queue.append(root)
        #     # while not empty
        #     while queue:
        #         q, t = deque(), []
        #         # pop one queue-1 and push to queue-2
        #         while queue:
        #             node = queue.popleft()
        #             t.append(node.val)
        #             if node.left: q.append(node.left)
        #             if node.right: q.append(node.right)
        #         # process current level
        #         res.append(t)
        #         # seitch queue
        #         queue = q
        #     return res
        # return BFS()
# @lc code=end

