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
        # 关键：通过inorder确定左右子树的长度
        inorder_mem = {v: i for i, v in enumerate(inorder)}

        def traverse(prelist, in_begin, in_end):
            if not prelist: return None
            root = prelist[0]
            in_idx = inorder_mem[root]
            # leftLength + 1 == idx - inBegin + 1
            left_len = in_idx - in_begin
            # leftLength + rightLength + 1 = inEnd - inBegin + 1
            right_len = in_end - in_begin - left_len
            node = TreeNode(root)
            node.left = traverse(prelist[1:left_len+1], in_begin, in_idx-1)
            node.right = traverse(prelist[left_len+1:], in_idx+1, in_end)
            return node

        return traverse(preorder, 0, len(inorder)-1)
            

# @lc code=end

