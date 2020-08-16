#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # way1: recursion without list copy
        n = len(preorder)
        def recursion(length, i, j):
            if length == 0: return None
            root = TreeNode(preorder[i])
            idx = inorder.index(preorder[i])
            left_len = idx - j
            right_len = length - left_len - 1
            root.left = recursion(left_len, i+1, j)
            root.right = recursion(right_len, i+1+left_len, idx+1)
            return root
        return recursion(n, 0, 0)


        # # way2: recursion
        # if not preorder: return None
        # root = TreeNode(preorder[0])
        # idx = inorder.index(preorder[0])  # i == left_len
        # root.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        # root.right = self.buildTree(preorder[1+idx:], inorder[idx+1:])
        # return root

# @lc code=end

