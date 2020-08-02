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
        if not root:
            return []

        # iterative
        # DFS：使用 Stack 后进先出；BFS：使用 Queue 先进先出
        my_stack, output = [root], []
        while my_stack:
            node = my_stack.pop()
            output.append(node.val)
            if node.right:
                my_stack.append(node.right)
            if node.left:
                my_stack.append(node.left)
        return output

        # # recursive
        # output = [root.val]
        # output.extend(self.preorderTraversal(root.left))
        # output.extend(self.preorderTraversal(root.right))
        # return output
# @lc code=end

