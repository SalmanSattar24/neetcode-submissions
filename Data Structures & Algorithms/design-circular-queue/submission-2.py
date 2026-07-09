class ListNode:

    def __init__(self, val, nxt, prev):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):

        self.space = k
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False
        
        new_node = ListNode(value, None, None)

        if self.head == self.tail == None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next

            new_node.next = self.head
            self.head.prev = new_node

        self.space -= 1

        return True


    def deQueue(self) -> bool:

        if self.isEmpty():
            return False
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        else:
            new_head = self.head.next
            self.tail.next = new_head
            new_head.prev = self.tail

            self.head = new_head

        self.space += 1

        return True
        

    def Front(self) -> int:

        if self.isEmpty():
            return -1
        
        return self.head.val
        

    def Rear(self) -> int:

        if self.isEmpty():
            return -1
        
        return self.tail.val
        

    def isEmpty(self) -> bool:

        if self.head == self.tail == None:
            return True
        
        return False
        

    def isFull(self) -> bool:

        if self.space == 0:
            return True
        
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()