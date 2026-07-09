# Time Complexity: O(max(m, n)), where m and n are the lengths of the two input linked lists,
# as we iterate through each list at most once.
# Space Complexity: O(max(m, n)) for the new linked list created to store the sum.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node. This is a common technique to simplify linked list operations,
        # as it serves as a starting point and avoids special-casing the creation of the head node.
        dummy_head = ListNode()

        # Initialize a pointer 'current_node' to the dummy head.
        # This pointer will be used to traverse and build the new result list.
        current_node = dummy_head

        # Initialize the carry-over value for the addition, similar to manual column addition.
        carry = 0

        # Loop until we have traversed both lists and processed any final carry-over.
        # The loop continues as long as there are nodes in either list or a carry value remains.
        while l1 or l2 or carry:
            # Get the value of the current node from l1. If l1 is None (end of list), use 0.
            val1 = l1.val if l1 else 0
            # Get the value of the current node from l2. If l2 is None (end of list), use 0.
            val2 = l2.val if l2 else 0

            # Calculate the total sum of the current digits and the carry from the previous step.
            total_sum = val1 + val2 + carry

            # Calculate the new carry-over value for the next iteration using integer division.
            carry = total_sum // 10

            # Get the digit for the current node of the result list using the modulo operator.
            new_digit = total_sum % 10

            # Create a new ListNode with the calculated digit.
            new_node = ListNode(new_digit)

            # Append the new node to the result list by setting the 'next' pointer of the current node.
            current_node.next = new_node

            # Move the 'current_node' pointer forward to the new node to prepare for the next digit.
            current_node = current_node.next

            # Advance the pointers for both input lists to their next nodes, if they exist.
            # This ensures we move to the next pair of digits in the next iteration.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # The first node of the actual result list is the one right after the dummy head.
        return dummy_head.next