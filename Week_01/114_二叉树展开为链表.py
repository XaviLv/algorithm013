#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """ 25%
        Do not return anything, modify root in-place instead.
        """
        
        def _preorder(node) -> TreeNode:
            if not node:
                return None
            if not node.left and not node.right:
                return node
            if node.left:
                rear_l = _preorder(node.left)
            if node.right:
                rear_r = _preorder(node.right)
            if not node.left:
                return rear_r
            if not node.right:
                node.right = node.left
                node.left = None
                return rear_l
            rear_l.right = node.right
            node.right = node.left
            node.left = None
            return rear_r

        _preorder(root)
        return root

        
# @lc code=end

