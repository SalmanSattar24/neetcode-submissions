class Solution:
    def trap(self, height: List[int]) -> int:
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:

            if left_max < right_max:

                left += 1
                
                if height[left] >= left_max:
                    left_max = height[left]
                
                else:
                    water += left_max - height[left]
            
            else:

                right -= 1

                if height[right] >= right_max:
                    right_max = height[right]
                
                else:
                    water += right_max - height[right]
        
        return water