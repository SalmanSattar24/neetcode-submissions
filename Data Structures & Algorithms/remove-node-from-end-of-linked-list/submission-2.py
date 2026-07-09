# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle the edge case of removing the head.
        dummy = ListNode(0, head)
        left = dummy
        right = dummy

        # Move the right pointer 'n' steps ahead.
        # This creates the required gap between the left and right pointers.
        # It's 'n' steps because both pointers start at the dummy node.
        for _ in range(n):
            right = right.next
        
        # Move both pointers simultaneously until the right pointer reaches the end.
        # The condition 'while right.next' ensures the right pointer
        # stops at the last node, not after it, preventing the error.
        while right.next:
            left = left.next
            right = right.next
        
        # At this point, the 'left' pointer is at the node just before the one to remove.
        # Update the 'next' pointer to skip the target node.
        left.next = left.next.next

        # The new head is the node after the dummy node.
        return dummy.next