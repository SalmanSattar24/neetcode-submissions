class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        n = len(arr)
        sub_arr_sum = sum(arr[:k])
        target_sum = threshold * k
        l = 0
        res = 1 if sub_arr_sum >= target_sum else 0

        for r in range(k, n):

            sub_arr_sum -= arr[l]
            sub_arr_sum += arr[r]

            
            if sub_arr_sum >= target_sum:
                res += 1
            

            l += 1
        
        return res