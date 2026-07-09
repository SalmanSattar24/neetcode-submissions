class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        N = len(temperatures)
        result = [0] * N
        stack = []

        for idx, temp in enumerate(temperatures):

            if not stack or stack[-1][0] >= temp:
                stack.append((temp, idx))
                continue
            
            while stack and stack[-1][0] < temp:

                prev_temp, prev_idx = stack.pop()

                result[prev_idx] = idx - prev_idx
            
            stack.append((temp, idx))
        
        return result