class Solution:
    def jump(self, nums: List[int]) -> int:
        
        queue = collections.deque([(0, 0)])
        min_jumps = float('inf')

        visited = {0}

        while queue:

            index, jumps_taken = queue.popleft()

            if index >= len(nums) - 1:
                return jumps_taken

            jumps_available = nums[index]
            
            for i in range(1, jumps_available + 1):

                next_index = index + i

                if next_index not in visited:

                    visited.add(next_index)
                    queue.append((next_index, jumps_taken + 1))

        return 0