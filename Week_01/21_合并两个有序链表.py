#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1. recursive
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

        # # 2. iterative
        # head = p = ListNode()
        # while l1 and l2:
        #     if l1.val > l2.val:
        #         l1, l2 = l2, l1
        #     p.next = l1
        #     l1 = l1.next
        #     p = p.next
        # p.next = l1 or l2
        # return head.next
        
# @lc code=end

