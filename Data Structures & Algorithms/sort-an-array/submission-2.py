class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def conqueror(arr, l, m, r):

            left_arr, right_arr = arr[l : m + 1], arr[m + 1 : r + 1]
            read_left, read_right, write = 0, 0, l
            len_left, len_right = len(left_arr), len(right_arr)

            while read_left < len_left and read_right < len_right:

                if left_arr[read_left] <= right_arr[read_right]:

                    arr[write] = left_arr[read_left]
                    read_left += 1
                
                else:

                    arr[write] = right_arr[read_right]
                    read_right += 1
                
                write += 1

            while read_left < len_left:

                arr[write] = left_arr[read_left]
                read_left += 1
                write += 1
            
            while read_right < len_right:

                arr[write] = right_arr[read_right]
                read_right += 1
                write += 1
        
        def divide(arr, l, r):

            if l >= r:
                return
            
            m = (l + r) // 2
            divide(arr, l, m)
            divide(arr, m + 1, r)

            conqueror(arr, l, m, r)
        
        def merge_sort(arr):

            divide(arr, 0, len(arr) - 1)
        
        merge_sort(nums)
        return nums