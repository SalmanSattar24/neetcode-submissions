# Time Complexity: O(1) for all operations (enQueue, deQueue, Front, Rear, isEmpty, isFull)
# because they involve a constant number of pointer manipulations.
#
# Space Complexity: O(k), where k is the maximum capacity of the circular queue.
# This is because we are storing at most k nodes in the linked list.

class ListNode:
    """A node in a doubly linked list."""
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:
    """
    A circular queue implemented using a doubly linked list.
    The list wraps around, connecting the head and tail.
    """
    def __init__(self, k: int):
        # k is the maximum capacity of the queue.
        self.k = k
        # space represents the number of available slots in the queue.
        self.space = k
        # Pointers to the head and tail of the linked list.
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        """Adds an element to the rear of the queue."""
        # If the queue is full (no remaining space), we cannot add a new element.
        if self.isFull():
            return False

        # Create a new node with the given value.
        new_node = ListNode(value)

        # Handle the case where the queue is currently empty.
        if self.isEmpty():
            # The new node is both the head and the tail.
            self.head = self.tail = new_node
            # To make it a circular list, its next and previous pointers
            # point to itself.
            self.head.next = self.head
            self.head.prev = self.head
        else:
            # If the queue is not empty, link the new node at the tail.
            # The new node's next pointer points to the head.
            new_node.next = self.head
            # The new node's previous pointer points to the current tail.
            new_node.prev = self.tail
            # Update the current head's previous pointer to the new node.
            self.head.prev = new_node
            # Update the current tail's next pointer to the new node.
            self.tail.next = new_node
            # The new node becomes the new tail.
            self.tail = new_node

        # Decrease the available space count.
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        """Deletes an element from the front of the queue."""
        # If the queue is empty, there is nothing to dequeue.
        if self.isEmpty():
            return False
        
        # Handle the case where the queue has only one element.
        if self.head == self.tail:
            # Both head and tail are set to None.
            self.head = self.tail = None
        else:
            # Move the head pointer to the next node.
            self.head = self.head.next
            # Update the new head's previous pointer to the tail.
            self.head.prev = self.tail
            # Update the tail's next pointer to the new head.
            self.tail.next = self.head
            
        # Increase the available space count.
        self.space += 1
        return True

    def Front(self) -> int:
        """Gets the front item from the queue."""
        # If the queue is empty, return -1.
        if self.isEmpty():
            return -1
        # Otherwise, return the value of the head node.
        return self.head.val

    def Rear(self) -> int:
        """Gets the last item from the queue."""
        # If the queue is empty, return -1.
        if self.isEmpty():
            return -1
        # Otherwise, return the value of the tail node.
        return self.tail.val

    def isEmpty(self) -> bool:
        """Checks whether the circular queue is empty."""
        # The queue is empty if the remaining space is equal to the capacity.
        return self.space == self.k

    def isFull(self) -> bool:
        """Checks whether the circular queue is full."""
        # The queue is full if there is no remaining space.
        return self.space == 0