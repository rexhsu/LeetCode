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
        count = 1
        curNode = head
        while curNode.next != None:
            count += 1
            curNode = curNode.next
        nth = count - n
        print "nth:%d" % nth
        idx = 0
        preNode = None
        curNode = head
        while curNode.next != None:
            print "idx:%d" % idx
            if idx == nth:
                if preNode == None:
                    return curNode.next
                else:
                    print "preNode:%d curNode:%d" % (preNode.val, curNode.val)
                    preNode.next = curNode.next
                    return head
            else:
                idx += 1
                preNode = curNode
                curNode = curNode.next
        if idx == nth:
            if preNode != None:
                preNode.next = None
                return head
            else:
                return None
        else:
            return None
