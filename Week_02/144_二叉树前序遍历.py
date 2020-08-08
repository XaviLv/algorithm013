#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # # recursive: 根-左-右，注意用 extend 连接返回的数组
        # res = []
        # if root:
        #     res.append(root.val)
        #     res.extend(self.preorderTraversal(root.left))
        #     res.extend(self.preorderTraversal(root.right))
        # return res

        # iterative
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

# @lc code=end

