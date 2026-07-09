class Solution {
private:
    ListNode* reverseLinkedList(ListNode* head) {
        // (your corrected helper function code here)
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr) {
            ListNode* nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
        }
        return prev;
    }
    
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Handle the case where the list has only one node and it's being removed.
        if (head->next == nullptr && n == 1) {
            return nullptr;
        }

        // Step 1: Reverse the list using the helper function.
        ListNode* reversed_head = reverseLinkedList(head);

        // Step 2: Traverse and remove the nth node from the beginning of the reversed list.
        // We handle the edge case where the head of the reversed list needs to be removed.
        if (n == 1) {
            ListNode* new_head = reversed_head->next;
            // Step 3: Reverse back to the original order.
            return reverseLinkedList(new_head);
        }

        // For all other cases, we need to find the node *before* the one to be removed.
        ListNode* current = reversed_head;
        for (int i = 0; i < n - 2; ++i) {
            current = current->next;
        }
        
        // Remove the target node.
        ListNode* node_to_remove = current->next;
        current->next = node_to_remove->next;
        
        // Step 3: Reverse the list back to its original order.
        return reverseLinkedList(reversed_head);
    }
};