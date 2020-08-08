#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # inorder: 左-根-右
        # # recursive
        # res = []
        # if root:
        #     res.extend(self.inorderTraversal(root.left))
        #     res.append(root.val)
        #     res.extend(self.inorderTraversal(root.right))
        # return res

        # iterative：一路找到最左边的叶子节点
        res, stack, cur = [], [], root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop() # 注意，此时cur必然为空，弹出cur parent叶子节点
            res.append(top.val)
            cur = top.right
        return res
            

# @lc code=end
