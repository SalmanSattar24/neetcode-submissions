class MyHashSet:
    def __init__(self):
        # Initialize an empty list to store unique keys
        self.data = []

    def add(self, key: int) -> None:
        # Only add the key if it is not already present in the set
        if key not in self.data:
            self.data.append(key)

    def remove(self, key: int) -> None:
        # If the key exists in the set, remove it
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        # Check if the key is present in the set
        return key in self.data



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)