class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        counter_t = Counter(t)
        window_counter = defaultdict(int)

        have, need = 0, len(counter_t)

        res, min_len = [-1, -1], float('inf')

        left = 0
        for right in range(len(s)):

            char = s[right]

            window_counter[char] = 1 + window_counter.get(char, 0)

            if char in counter_t and counter_t[char] == window_counter[char]:
                have += 1
            
            while have == need:

                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    res = [left, right]

                char_left = s[left]
                window_counter[char_left] -= 1

                if char_left in counter_t and window_counter[char_left] < counter_t[char_left]:
                    have -= 1
                
                left += 1
            
        print(res)
        start, end = res
        return s[start: end + 1] if min_len != float('inf') else ''