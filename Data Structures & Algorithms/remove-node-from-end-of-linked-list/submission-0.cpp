/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {

private:

    ListNode* reverseLinkedList(ListNode* head) {
        
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

        if (head->next == nullptr and n == 1) {
            return nullptr;
        }

        ListNode* reversed_head = reverseLinkedList(head);

        if (n == 1) {
            ListNode* new_head = reversed_head->next;
            return reverseLinkedList(new_head);
        }

        ListNode* current = reversed_head;

        for (int i = 1; i < n - 1; i++) {
            current = current->next;
        }

        current->next = current->next->next;

        return reverseLinkedList(reversed_head);
        
    }
};
