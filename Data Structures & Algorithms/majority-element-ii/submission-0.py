class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = defaultdict(int)

        for num in nums:

            count[num] += 1

            if len(count) <= 2:
                continue
            
            new_count = defaultdict(int)

            for val, freq in count.items():
                
                if freq > 1:
                    new_count[val] = freq - 1

            count = new_count
        

        res = []

        for num in count:

            if nums.count(num) > len(nums) // 3:
                res.append(num)

        return res