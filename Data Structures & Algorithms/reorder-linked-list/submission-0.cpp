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
public:
    void reorderList(ListNode* head) {

        ListNode* fast = head->next;
        ListNode* slow = head;

        while (fast != nullptr && fast->next != nullptr) {

            fast = fast->next->next;
            slow = slow->next;
        }

        ListNode* second = slow->next;
        ListNode* prev = slow->next = nullptr;

        while (second != nullptr) {

            ListNode* nxt = second->next;
            second->next = prev;
            prev = second;
            second = nxt;
        }

        ListNode* first = head;
        second = prev;

        while (second != nullptr) {

            ListNode* second_next = second->next;
            ListNode* first_next = first->next;

            first->next = second;
            second->next = first_next;
            first = first_next;
            second = second_next;

        }

        
    }
};
