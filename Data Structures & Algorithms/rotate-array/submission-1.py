class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def rotateArray(start, end):

            left, right = start, end

            while left < right:

                nums[left], nums[right] = nums[right], nums[left]

                left += 1
                right -= 1
        

        n = len(nums)
        k = k % n

        rotateArray(0, n - 1)
        rotateArray(0, k - 1)
        rotateArray(k, n - 1)