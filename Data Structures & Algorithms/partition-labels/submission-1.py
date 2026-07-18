class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        end_index_map = {}
        res = []
        size = 0
        start, end = 0, 0

        for i, char in enumerate(s):
            end_index_map[char] = i
        
        for i, char in enumerate(s):

            end = max(end, end_index_map[char])

            if i == end:
                res.append(end - start + 1)
                start = i + 1
                end = end_index_map[char]
        
        print(end_index_map)
        return res

            