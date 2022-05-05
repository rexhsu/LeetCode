# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # empty list, one node list or zero rotation
        if not head or not head.next or k == 0: return head
        tail = head
        # count list size first
        siz = 1
        while tail.next:
            siz, tail = siz+1, tail.next
        k = k%siz # overround
        if k == 0: return head # no rotation
        #print(siz, k)
        pre, cur = None, head
        for i in range(siz-k):
            pre, cur = cur, cur.next
        pre.next = None # the new tail point to nil
        tail.next = head
        
        return cur