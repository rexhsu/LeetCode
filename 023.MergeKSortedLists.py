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

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []
        elif len(lists) == 1: 
            return lists[0]
        elif len(lists) == 2: 
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            return self.mergeTwoLists(self.mergeKLists(lists[:len(lists)/2]), self.mergeKLists(lists[len(lists)/2:]))
