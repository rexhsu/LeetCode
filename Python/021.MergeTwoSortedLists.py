# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rNode = ListNode(0)
        tNode = rNode
        
        while l1 and l2:
            if l1.val < l2.val:
                curNode = ListNode(l1.val)
                tNode.next = curNode
                tNode = curNode
                l1 = l1.next
            else:
                curNode = ListNode(l2.val)
                tNode.next = curNode
                tNode = curNode
                l2 = l2.next
        if l1:
            tNode.next = l1
        if l2:
            tNode.next = l2
            
        return rNode.next
