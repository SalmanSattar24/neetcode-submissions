# Time Complexity: O(1) for both put and get operations on average.
#   - This is achieved by using a hash map for immediate O(1) lookups of nodes
#     and a doubly linked list for O(1) insertions and deletions of nodes.
# Space Complexity: O(capacity)
#   - The space is used to store the key-value pairs in both the hash map
#     and the doubly linked list, up to the specified cache capacity.


# Node class for the doubly linked list.
# Each node stores a key-value pair, allowing for quick access to the key when evicting.
class Node:
    """A node in a doubly linked list."""
    def __init__(self, key=None, value=None, right=None, left=None):
        self.key = key
        self.value = value
        self.right = right  # Pointer to the next (more recently used) node.
        self.left = left    # Pointer to the previous (less recently used) node.


class LRUCache:
    """
    An implementation of a Least Recently Used (LRU) Cache.
    
    This cache uses a combination of a hash map and a doubly linked list
    to achieve O(1) average time complexity for both `get` and `put` operations.
    """

    def __init__(self, capacity: int):
        """
        Initializes the LRU cache with a given capacity.
        """
        self.capacity = capacity
        self.size = 0
        
        # Maps keys to their corresponding Node objects for O(1) access.
        # Note: Although named `key_value_map`, it stores entire Node objects
        # to allow for O(1) list manipulation.
        self.key_value_map = {}
        
        # Sentinel nodes for the head and tail of the doubly linked list.
        # These sentinels simplify the logic for adding/removing nodes by removing
        # the need to check for null pointers at the ends of the list.
        self.head = Node()
        self.tail = Node()
        
        # Initially, the list is empty, so head and tail point to each other.
        self.head.right = self.tail
        self.tail.left = self.head
    
    def addNode(self, key, val):
        """
        Creates a new node and adds it to the front of the linked list (most recent).
        """
        # The current most recently used node is the one right after the head sentinel.
        mru_node = self.head.right
        
        # Create the new node. Its `left` will be the head sentinel and its `right`
        # will be the former most recently used node.
        new_node = Node(key, val, mru_node, self.head)

        # Insert the new node into the list by updating the pointers of its neighbors.
        # 1. Point the head sentinel's `right` to the new node.
        self.head.right = new_node
        # 2. Point the former most recent node's `left` to the new node.
        mru_node.left = new_node

        # Add the new node to our map for O(1) lookup.
        self.key_value_map[key] = new_node
        self.size += 1
    
    def removeNode(self, node):
        """
        Removes a node from the linked list.
        """
        key = node.key

        # Get the node's neighbors.
        left_node = node.left
        right_node = node.right

        # Unlink the node by connecting its neighbors to each other.
        left_node.right = right_node
        right_node.left = left_node
        
        # Remove the corresponding key from the map.
        del self.key_value_map[key]

        self.size -= 1

    def get(self, key: int) -> int:
        """
        Retrieves the value for a given key. If found, the item is marked as
        most recently used.
        Returns -1 if the key is not in the cache.
        """
        if key not in self.key_value_map:
            return -1
        
        # Retrieve the node from the map.
        node = self.key_value_map[key]
        val = node.value
        
        # To mark it as most recently used, we move it to the front of the list.
        # This is done by removing it from its current position and adding it back.
        self.removeNode(node)
        self.addNode(key, val)

        return val

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates a key-value pair. If the key already exists, its value
        is updated, and it's marked as most recently used. If the key is new,
        it's added. If adding the new item exceeds capacity, the least
        recently used item is evicted.
        """
        # If the key already exists, we must remove its old version first
        # before adding the updated version to the front.
        if key in self.key_value_map:
            node = self.key_value_map[key]
            self.removeNode(node)
        
        # Add the new or updated key-value pair to the front of the list.
        self.addNode(key, value)
        
        # If adding this new node has made the cache exceed its capacity...
        if self.size > self.capacity:
            # ...we must evict the least recently used item.
            # The LRU node is the one just before the tail sentinel.
            lru_node = self.tail.left
            self.removeNode(lru_node)