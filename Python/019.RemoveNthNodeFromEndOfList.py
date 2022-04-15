# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tNode = ListNode(0)
        tNode.next = head
        iNode, jNode, rHead = tNode, tNode, tNode
        for i in xrange(0, n):
            ''' Go n steps '''
            iNode = iNode.next 
        '''print "iNode:", iNode.val'''
        ''' Go (all - n) steps '''
        while iNode.next:
            iNode = iNode.next
            jNode = jNode.next
        jNode.next = jNode.next.next
        return rHead.next
