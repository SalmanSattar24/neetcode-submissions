class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Helper function to reverse a portion of the array in-place.
        # It takes a start and an end index and reverses the elements
        # within that range (inclusive).
        def rotateArray(start, end):
            left, right = start, end
            while left < right:
                # Swap elements at the left and right pointers
                nums[left], nums[right] = nums[right], nums[left]
                # Move pointers towards the center
                left += 1
                right -= 1

        # Get the length of the array
        n = len(nums)

        # Normalize k: If k is greater than the array length,
        # rotating by k steps is equivalent to rotating by k % n steps.
        # This handles cases where k is larger than the array size and
        # prevents unnecessary full rotations.
        k = k % n

        # Step 1: Reverse the entire array.
        # This brings the elements that should eventually be at the end
        # to the beginning, and vice-versa.
        # Example: [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1] (for k=3)
        rotateArray(0, n - 1)

        # Step 2: Reverse the first k elements.
        # These k elements are the ones that will form the beginning
        # of the rotated array. After the full reversal, they are at the
        # start, but in reverse order. This step puts them in the correct
        # relative order.
        # Example: [7,6,5,4,3,2,1] and k=3 -> reverse [7,6,5] to [5,6,7]
        # Array becomes: [5,6,7,4,3,2,1]
        rotateArray(0, k - 1)

        # Step 3: Reverse the remaining n - k elements (from index k to n-1).
        # These are the elements that will form the end of the rotated array.
        # After the first two reversals, they are in place but in reverse order.
        # This step corrects their relative order.
        # Example: [5,6,7,4,3,2,1] and k=3 -> reverse [4,3,2,1] to [1,2,3,4]
        # Final array: [5,6,7,1,2,3,4]
        rotateArray(k, n - 1)
