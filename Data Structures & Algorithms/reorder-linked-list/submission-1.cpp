/**
 * Definition for singly-linked list.
 * struct ListNode {
 * int val;
 * ListNode *next;
 * ListNode() : val(0), next(nullptr) {}
 * ListNode(int x) : val(x), next(nullptr) {}
 * ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        /*
         * Time Complexity: O(n)
         * We traverse the list three times:
         * 1. To find the middle using a fast and slow pointer (O(n)).
         * 2. To reverse the second half of the list (O(n)).
         * 3. To merge the two halves (O(n)).
         * Overall time is dominated by these linear operations.
         *
         * Space Complexity: O(1)
         * The solution is in-place and uses a constant number of extra pointers
         * to perform the operations, regardless of the list size.
         */

        // Handle edge cases: if the list is empty, has one node,
        // or has two nodes, it's already in the correct order.
        if (!head || !head->next || !head->next->next) {
            return;
        }

        // --- Step 1: Find the middle of the linked list ---
        // We use a slow and a fast pointer to find the middle.
        // The slow pointer moves one step at a time.
        // The fast pointer moves two steps at a time.
        // When the fast pointer reaches the end, the slow pointer will be at the middle.
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // --- Step 2: Split the list into two halves and reverse the second half ---
        // 'second' will be the head of the second half of the list.
        ListNode* second = slow->next;
        // The first half ends at 'slow'. We set 'slow->next' to 'nullptr' to
        // terminate the first list and separate it from the second.
        slow->next = nullptr;
        
        // We now reverse the second half of the list.
        ListNode* prev = nullptr;
        ListNode* curr = second;
        while (curr) {
            ListNode* nextTemp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextTemp;
        }
        
        // After this loop, 'prev' is the new head of the reversed second half.
        // Let's re-name our pointers for clarity in the next step.
        // 'first' is the head of the first list (head of the original list).
        // 'second' is the head of the reversed second list.
        ListNode* first = head;
        second = prev;
        
        // --- Step 3: Merge the two halves alternating nodes ---
        // We iterate while the second list has nodes to merge.
        while (second) {
            // Save the next nodes for both lists before we modify the pointers.
            ListNode* first_next = first->next;
            ListNode* second_next = second->next;

            // Reorder the pointers:
            // 1. Point the current node of the first list to the current node of the second list.
            first->next = second;
            // 2. Point the current node of the second list back to the saved next node of the first list.
            second->next = first_next;

            // Move both pointers to their next positions to continue the merge.
            first = first_next;
            second = second_next;
        }
    }
};