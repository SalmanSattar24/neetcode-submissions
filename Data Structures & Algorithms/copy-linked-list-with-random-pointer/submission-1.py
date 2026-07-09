"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # This is a classic two-pass approach using a hash map.
        #
        # First Pass: Create all the new nodes (the deep copies)
        # without worrying about their 'next' or 'random' pointers.
        # Store a mapping from the original nodes to their newly created copies.
        
        # Handle the base case where the input list is empty.
        if not head:
            return None
        
        # The hash map to store the mapping from original nodes to their copies.
        # We pre-add a mapping for `None` to `None` to simplify
        # pointer assignments later, as both `next` and `random`
        # pointers can be `None`.
        old_to_new_map = { None: None }
        
        # 'current_node' is our pointer to traverse the original list.
        current_node = head
        while current_node:
            # Create a new node with the same value as the original.
            new_node = Node(current_node.val)
            # Store the mapping in our hash map.
            old_to_new_map[current_node] = new_node
            # Move to the next node in the original list.
            current_node = current_node.next
            
        # Second Pass: Iterate through the original list again
        # to connect the 'next' and 'random' pointers of the new nodes.
        
        # Reset 'current_node' to the head of the original list.
        current_node = head
        while current_node:
            # Get the copy of the current node from our hash map.
            new_node = old_to_new_map[current_node]
            
            # Use the hash map to find the correct copies for the 'next' and 'random' pointers.
            # - `current_node.next` is a pointer to an original node.
            # - `old_to_new_map[current_node.next]` gives us the corresponding copy of that node.
            new_node.next = old_to_new_map[current_node.next]
            
            # Repeat the process for the 'random' pointer.
            new_node.random = old_to_new_map[current_node.random]
            
            # Move to the next node in the original list to continue the process.
            current_node = current_node.next
            
        # After the loops complete, all nodes and their pointers are correctly
        # copied. We can now return the head of the new list, which is
        # the copy of the original head.
        return old_to_new_map[head]