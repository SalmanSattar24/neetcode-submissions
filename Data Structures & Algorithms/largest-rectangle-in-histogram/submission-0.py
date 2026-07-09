class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [(0, -1)]
        max_area = 0
        heights.append(0)

        for index, height in enumerate(heights):

            while stack[-1][0] > height:

                prev_height, prev_index = stack.pop()

                right_limit = index
                left_limit = stack[-1][1]
                width = right_limit - left_limit - 1

                area = width * prev_height

                max_area = max(max_area, area)
            
            stack.append((height, index))
        
        return max_area