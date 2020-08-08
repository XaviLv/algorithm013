#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # postOrder: 左-右-根
        # 关键：通过inorder确定左右子树的长度
        inorder_mem = {v:i for i,v in enumerate(inorder)}

        def traverse(postorder, in_begin, in_end):
            if not postorder: return None
            root = postorder[-1]
            in_idx = inorder_mem[root]
            # 以下4句是最容易出错的地方
            left_len = in_idx - in_begin
            right_len = in_end - in_begin - left_len
            node = TreeNode(root)
            node.right = traverse(postorder[-1-right_len:-1], in_idx+1, in_end)
            node.left = traverse(postorder[:-1-right_len], in_begin, in_idx-1)
            return node

        return traverse(postorder, 0, len(postorder)-1)



# @lc code=end

