/*
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *node, *prev, *head = NULL;
    char carry = 0;
    while (l1 || l2) {
            node = malloc(8);
            node->val = carry;
            carry = 0;
            
            if (head) prev->next = node;
            else head = node;
            prev = node;
            
            if (l1) {
                        node->val += l1->val;
                        l1 = l1->next;
                    }
            
            if (l2) {
                        node->val += l2->val;
                        l2 = l2->next;
                    }
            
            if (node->val >= 10) {
                        node->val -= 10;
                        carry = 1;
                    } 
    
        }

    if (carry) {
            node = malloc(8);
            node->val = 1;
            node->next = NULL;
            prev->next = node;
        } else {
                prev->next = NULL;
            }
    
    return head;
}
