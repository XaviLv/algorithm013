#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # # way 1: recursion
        # if root in [None, p, q]:
        #     return root
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if left and right: 
        #     return root
        # return left or right

        # way 2: hash store parents 
        stack, parents = [root], {root: None}
        # 1. create hash map (stop if both p & q tracked)
        while p not in parents or q not in parents:
            top = stack.pop()
            if top.right:
                parents[top.right] = top
                stack.append(top.right)
            if top.left:
                parents[top.left] = top
                stack.append(top.left)
        # 2. backtrace p and q separately
        trace_p = set()
        while p:
            trace_p.add(p)
            p = parents[p]
        while q not in trace_p:
            q = parents[q]
        return q
        

# @lc code=end

