class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_counter = Counter(s1)
        window_counter = defaultdict(int)
        left = 0

        for right in range(len(s2)):

            char_right = s2[right]
            window_counter[char_right] += 1
            
            while right - left + 1 > len(s1):
                
                char_left = s2[left]
                window_counter[char_left] -= 1

                if window_counter[char_left] == 0: 
                    del window_counter[char_left]
                
                left += 1
            
            if s1_counter == window_counter:
                return True
        
        return False