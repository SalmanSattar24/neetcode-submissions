class MyHashMap:
    def __init__(self):
        # Initialize an array to store key-value pairs.
        # The array size is 1000001 to accommodate keys in the range [0, 1000000].
        # We use -1 as a default value to indicate that a key has no associated value.
        self.array = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        # Inserts a (key, value) pair into the HashMap.
        # If the key already exists, it updates the corresponding value.
        # Directly assigns the value to the index corresponding to the key.
        self.array[key] = value

    def get(self, key: int) -> int:
        # Retrieves the value associated with the given key.
        # If the key is not found (i.e., value is still -1), return -1.
        if self.array[key] == -1:
            return -1
        else:
            return self.array[key]

    def remove(self, key: int) -> None:
        # Removes the key and its corresponding value from the HashMap.
        # This is done by resetting the value at the key's index to -1.
        self.array[key] = -1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)