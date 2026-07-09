# Time Complexity: O(n), where n is the number of nodes in the linked list.
# The algorithm performs a single pass through the list to find the reversal
# segment and then reverse it in-place.
#
# Space Complexity: O(1).
# The solution uses a constant number of pointers regardless of the input size,
# performing all operations in-place.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node to simplify handling the case where left = 1.
        # This dummy node points to the head of the original list.
        dummy_head = ListNode(0, head)

        # Find the node right before the sublist to be reversed.
        # We start from the dummy node and move 'left - 1' steps forward.
        node_before_left = dummy_head
        for _ in range(left - 1):
            node_before_left = node_before_left.next

        # 'start_of_sublist' is the first node of the sublist to be reversed.
        start_of_sublist = node_before_left.next
        
        # 'current_node' will be the pointer we use to traverse and reverse the sublist.
        current_node = start_of_sublist
        
        # 'previous_node' will track the reversed part of the sublist. It is initialized to None.
        previous_node = None
        
        # Reverse the sublist from 'left' to 'right'. The loop runs 'right - left + 1' times.
        for _ in range(right - left + 1):
            # Temporarily store the next node.
            next_node = current_node.next
            
            # Reverse the pointer of the current node to point to the previous node.
            current_node.next = previous_node
            
            # Move the 'previous_node' pointer forward to the current node.
            previous_node = current_node
            
            # Move the 'current_node' pointer forward to the next node.
            current_node = next_node

        # At this point, the sublist is reversed. Now we need to connect the three parts:
        # 1. The part of the list before the reversed segment.
        # 2. The reversed segment.
        # 3. The part of the list after the reversed segment.

        # Connect the node before the reversed segment to the new head of the reversed segment.
        # 'previous_node' now holds the new head of the reversed sublist.
        node_before_left.next = previous_node

        # Connect the end of the original sublist (which is now the tail) to the
        # rest of the list. 'current_node' now points to the node after the reversed segment.
        start_of_sublist.next = current_node

        # Return the head of the modified list, which is the node after the dummy.
        return dummy_head.next