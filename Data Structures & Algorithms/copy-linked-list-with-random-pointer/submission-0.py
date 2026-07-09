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
        
        nodes_map = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            nodes_map[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = nodes_map[cur]
            copy.next = nodes_map[cur.next]
            copy.random = nodes_map[cur.random]
            cur = cur.next
        
        return nodes_map[head]