/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }
    slow, fast := head, head
    for slow.Next != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
        if fast == nil {
            return nil
        }
        if slow == fast {
            fast = head
            for slow != fast {
                slow = slow.Next
                fast = fast.Next
            }
            return slow
        }
    }
    return nil
}
