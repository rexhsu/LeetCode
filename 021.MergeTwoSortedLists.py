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
        
        h1, h2 = l1, l2
        
        while h1 and h2:
            if h1.val < h2.val:
                curNode = ListNode(h1.val)
                tNode.next = curNode
                tNode = curNode
                h1 = h1.next
            else:
                curNode = ListNode(h2.val)
                tNode.next = curNode
                tNode = curNode
                h2 = h2.next
        if h1:
            tNode.next = h1
        if h2:
            tNode.next = h2
            
        return rNode.next
