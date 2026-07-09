class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        monotonic_decreasing_deque = deque()
        res = deque()

        for index in range(len(nums)):

            out_of_window_boundary = index - k
            if (
                monotonic_decreasing_deque and 
                monotonic_decreasing_deque[0] == out_of_window_boundary
            ):
                monotonic_decreasing_deque.popleft()
            
            while (
                monotonic_decreasing_deque and
                nums[index] >= nums[monotonic_decreasing_deque[-1]]
            ):
                monotonic_decreasing_deque.pop()

            monotonic_decreasing_deque.append(index)

            if index + 1 >= k:
                res.append(nums[monotonic_decreasing_deque[0]])

        return list(res)