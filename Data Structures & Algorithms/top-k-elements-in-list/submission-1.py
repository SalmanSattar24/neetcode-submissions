from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each unique number in the list
        nums_counter = Counter(nums)  # Returns a dict-like object with num: frequency

        # Step 2: Create a list of empty buckets to group numbers by their frequency
        # Index i in 'bucket' will hold a list of numbers that appear i times
        bucket = [[] for _ in range(len(nums) + 1)]  # Max frequency could be len(nums)

        # Step 3: Fill the buckets based on frequency
        for num, freq in nums_counter.items():
            bucket[freq].append(num)  # Append the number to the bucket at index 'freq'

        # Step 4: Collect the top k frequent elements starting from the highest frequency
        res = []

        # Iterate backwards through the bucket list to start with the highest frequencies
        for i in reversed(range(len(bucket))):
            for num in bucket[i]:
                res.append(num)  # Add number to result
                if len(res) == k:  # Stop when we've collected k elements
                    return res
