# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def reverseLinkedList(node):
            
            prev = None

            for _ in range(right - left + 1):
                
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            
            return prev
        
        dummy = ListNode(0, head)

        left_prev = dummy
        for _ in range(left - 1):
            left_prev = left_prev.next

        start_node = left_prev.next

        end_node = start_node
        for _ in range(right - left):
            end_node = end_node.next
        
        right_next = end_node.next
        
        reversed_head = reverseLinkedList(start_node)

        left_prev.next = reversed_head
        start_node.next = right_next

        return dummy.next