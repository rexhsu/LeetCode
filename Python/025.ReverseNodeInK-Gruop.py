# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2: return head
        node = head
        for _ in range(k):
            if not node: return head
            node = node.next
        prev = self.reverseKGroup(node, k)
        for _ in range(k):
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
