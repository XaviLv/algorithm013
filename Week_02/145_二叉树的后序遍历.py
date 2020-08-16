#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 左-右-根
        # recursive
        stack, res = [root], []
        while stack:
            top = stack.pop()
            if top:
                res.insert(0, top.val)
                stack.append(top.left)
                stack.append(top.right)
        return res

        # # recursive
        # res = []
        # if root:
        #     res.extend(self.postorderTraversal(root.left))
        #     res.extend(self.postorderTraversal(root.right))
        #     res.append(root.val)
        # return res
# @lc code=end
