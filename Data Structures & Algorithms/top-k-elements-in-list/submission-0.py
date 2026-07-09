class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_counter = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in nums_counter.items():

            bucket[freq].append(num)
        

        res = []

        for i in reversed(range(len(bucket))):

            for num in bucket[i]:

                res.append(num)

                if len(res) == k:

                    return res
        