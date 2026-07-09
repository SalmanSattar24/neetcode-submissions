class TimeMap:
    # Time Complexity:
    # - __init__: O(1) - Simply initializes an empty dictionary.
    # - set: O(1) - Dictionary operations (lookup, insertion) are average O(1). Appending to a list is O(1) amortized.
    # - get: O(log N) - Where N is the number of timestamps associated with a specific key.
    #                  This is due to the binary search performed on the list of (value, timestamp) tuples.

    # Space Complexity: O(M * N)
    # - M is the total number of unique keys stored.
    # - N is the total number of values/timestamps associated with a specific key.
    # - In the worst case, each key could have many timestamps, and we store all of them.
    #   The dictionary stores keys, and each key maps to a list of (value, timestamp) pairs.

    def __init__(self):
        # Initializes the TimeMap object.
        # As suggested by Hint 1 and Hint 2, a hash-based data structure (dictionary in Python)
        # is used to store key-value pairs.
        # Each 'key' will map to a list of (value, timestamp) tuples.
        # This allows storing multiple values for the same key, each with a different timestamp.
        self.store = {} # Example: self.store = {"foo": [("bar", 1), ("baz", 2)], "alice": [("happy", 1), ("sad", 3)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Stores the given 'key' with its 'value' at the specified 'timestamp'.
        # This method is designed to be O(1) on average, as recommended by the problem.

        # If the 'key' does not already exist in our store,
        # initialize an empty list for it. This list will hold (value, timestamp) tuples.
        if key not in self.store:
            self.store[key] = []

        # Append the new (value, timestamp) tuple to the list associated with the 'key'.
        # The problem statement notes that "For all calls to set, the timestamps are in strictly increasing order."
        # This is a crucial property: it means the list of (value, timestamp) tuples for any given key
        # will always be sorted by timestamp. This sorted property is essential for the O(log N) 'get' method.
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # Retrieves the most recent value of 'key' such that its timestamp
        # is less than or equal to the given 'timestamp'.
        # If no such value exists, or the key is not found, it returns an empty string "".
        # This method aims for O(log N) time complexity, as suggested by Hint 3 and Hint 4,
        # by leveraging binary search on the sorted timestamps.

        # First, check if the 'key' exists in our store.
        # If the key is not present, no values have been stored for it, so return "".
        if key not in self.store:
            return ""

        # Retrieve the list of (value, timestamp) tuples associated with the 'key'.
        # This list is guaranteed to be sorted by timestamp due to the 'set' method's behavior.
        values = self.store.get(key)

        # Initialize 'result' to an empty string. This will hold the found value.
        # If no suitable value is found, this empty string will be returned.
        result = ""

        # Initialize 'left' and 'right' pointers for the binary search.
        # 'left' starts at the beginning of the list.
        # 'right' starts at the end of the list.
        left, right = 0, len(values) - 1

        # Perform binary search to find the largest timestamp <= the given 'timestamp'.
        # The loop continues as long as the search space [left, right] is valid.
        while left <= right:
            # Calculate the middle index.
            mid = (left + right) // 2

            # Access the timestamp of the middle element.
            current_timestamp = values[mid][1]

            # If the current_timestamp is less than or equal to the target 'timestamp':
            # This 'mid' element is a potential candidate for our answer (it satisfies the timestamp condition).
            # Since we want the *most recent* (largest) timestamp that is <= the given timestamp,
            # we store this value as our current best `result`.
            # We then try to find a *newer* (larger) timestamp by searching in the right half.
            if current_timestamp <= timestamp:
                result = values[mid][0] # Store the value at this 'mid' index.
                left = mid + 1           # Move 'left' to search in the right half for a potentially better (newer) timestamp.
            # If the current_timestamp is greater than the target 'timestamp':
            # This 'mid' element's timestamp is too new.
            # We need to look for an older timestamp, so we discard the right half and search in the left half.
            else:
                right = mid - 1          # Move 'right' to search in the left half.

        # After the binary search loop completes, 'result' will hold the value
        # corresponding to the largest timestamp that was less than or equal to the
        # given 'timestamp'. If no such timestamp was found (e.g., all timestamps
        # for the key are greater than the target), 'result' remains "".
        return result