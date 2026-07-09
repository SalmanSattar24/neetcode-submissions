class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(array, left, right, mid):

            left_portion = array[left : mid + 1]
            right_portion = array[mid + 1 : right + 1]
            LEN_LEFT, LEN_RIGHT = len(left_portion), len(right_portion)

            read_left, read_right, write = 0, 0, left

            while read_left < LEN_LEFT and read_right < LEN_RIGHT:

                if left_portion[read_left] <= right_portion[read_right]:
                    
                    array[write] = left_portion[read_left]
                    read_left += 1
                
                else:

                    array[write] = right_portion[read_right]
                    read_right += 1
                
                write += 1
            
            while read_left < LEN_LEFT or read_right < LEN_RIGHT:

                if read_left < LEN_LEFT:

                    array[write] = left_portion[read_left]
                    read_left += 1
                
                if read_right < LEN_RIGHT:

                    array[write] = right_portion[read_right]
                    read_right += 1
                
                write += 1
        
        def mergeSort(array, left, right):

            if left == right:
                return
            
            mid = (left + right) // 2

            mergeSort(array, left, mid)
            mergeSort(array, mid + 1, right)
            merge(array, left, right, mid)

            return
        
        mergeSort(nums, 0, len(nums))
        return nums