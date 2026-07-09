from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Sorts an array of integers in ascending order using the Merge Sort algorithm.
        Ensures O(n log n) time complexity and minimal space complexity.
        
        Args:
            nums (List[int]): The list of integers to be sorted.
        
        Returns:
            List[int]: The sorted list of integers.
        """

        def merge(array, left, right, mid):
            """
            Merges two sorted subarrays into a single sorted array.
            
            Args:
                array (List[int]): The original array containing the subarrays.
                left (int): The starting index of the left subarray.
                right (int): The ending index of the right subarray.
                mid (int): The midpoint index separating the two subarrays.
            """
            # Extract left and right portions of the array
            left_portion = array[left : mid + 1]
            right_portion = array[mid + 1 : right + 1]

            # Get lengths of both portions
            LEN_LEFT, LEN_RIGHT = len(left_portion), len(right_portion)

            # Initialize pointers for reading and writing
            read_left, read_right, write = 0, 0, left

            # Merge elements from both portions in sorted order
            while read_left < LEN_LEFT and read_right < LEN_RIGHT:
                if left_portion[read_left] <= right_portion[read_right]:
                    array[write] = left_portion[read_left]
                    read_left += 1
                else:
                    array[write] = right_portion[read_right]
                    read_right += 1
                write += 1

            # Copy any remaining elements from the left portion
            while read_left < LEN_LEFT:
                array[write] = left_portion[read_left]
                read_left += 1
                write += 1

            # Copy any remaining elements from the right portion
            while read_right < LEN_RIGHT:
                array[write] = right_portion[read_right]
                read_right += 1
                write += 1

        def mergeSort(array, left, right):
            """
            Recursively sorts the array using the Merge Sort algorithm.
            
            Args:
                array (List[int]): The array to be sorted.
                left (int): The starting index of the current subarray.
                right (int): The ending index of the current subarray.
            """
            if left >= right:
                return  # Base case: single element is already sorted

            # Find the midpoint
            mid = (left + right) // 2

            # Recursively sort left and right halves
            mergeSort(array, left, mid)
            mergeSort(array, mid + 1, right)

            # Merge the sorted halves
            merge(array, left, right, mid)

        # Start the merge sort process
        mergeSort(nums, 0, len(nums) - 1)

        return nums
