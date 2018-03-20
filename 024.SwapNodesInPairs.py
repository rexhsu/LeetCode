# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rNode = ListNode(0)
        rNode.next = head

        n1 = rNode
        while n1.next and n1.next.next:
            """print "n1: %d" % n1.val"""
            n2 = n1.next
            n3 = n1.next.next
            n1.next = n3
            n2.next = n3.next
            n3.next = n2
            n1 = n2

        return rNode.next
