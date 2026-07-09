class MyHashSet:

    def __init__(self):
        
        self.array = [False] * 1000001

    def add(self, key: int) -> None:
        
        self.array[key] = True

    def remove(self, key: int) -> None:
        
        self.array[key] = False

    def contains(self, key: int) -> bool:
        
        if self.array[key] != False:

            return True
        
        else:

            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)