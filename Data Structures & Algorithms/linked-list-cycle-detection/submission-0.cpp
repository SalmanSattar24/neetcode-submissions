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
    bool hasCycle(ListNode* head) {

        if (head == nullptr || head->next == nullptr) {
            return false;
        }
        
        ListNode* fast = head->next;
        ListNode* slow = head;

        while (fast != slow) {
            
            if (fast == nullptr || fast->next == nullptr) {
                return false;
            }

            slow = slow->next;
            fast = fast->next->next;
            
        }

        return true;
    }
};
