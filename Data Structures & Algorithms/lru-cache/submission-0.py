class Node:
    
    def __init__(self, key=None, value = None, right = None, left = None):

        self.key = key
        self.value = value
        self.right = right
        self.left = left


class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.size = 0
        self.key_value_map = {}
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head
    
    def addNode(self, key, val):

        mru_node = self.head.right
        
        new_node = Node(key, val, mru_node, self.head)

        self.head.right = new_node
        mru_node.left = new_node

        self.key_value_map[key] = new_node
        self.size += 1
    
    def removeNode(self, node):

        key = node.key

        left_node = node.left
        right_node = node.right

        left_node.right = right_node
        right_node.left = left_node
        
        del self.key_value_map[key]

        self.size -= 1

    def get(self, key: int) -> int:
        
        if key not in self.key_value_map:
            return -1
        
        node = self.key_value_map[key]
        val = node.value
        self.removeNode(node)
        self.addNode(key, val)

        return val

    def put(self, key: int, value: int) -> None:
        
        if key in self.key_value_map:
            node = self.key_value_map[key]
            self.removeNode(node)
        
        self.addNode(key, value)
        
        if self.size > self.capacity:

            lru_node = self.tail.left
            self.removeNode(lru_node)