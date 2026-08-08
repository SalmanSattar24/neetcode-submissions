class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        L1, L2, L3 = len(s1), len(s2), len(s3)

        if L1 + L2 != L3:
            return False

        memo = {(L1, L2) : True}


        # if k == L3:
        #     return i == L1 and j == L2
            
        for i in reversed(range(L1 + 1)):
            for j in reversed(range(L2 + 1)):
                # for k in reversed(range(L3)):

                key = (i, j)
                # if key in memo:
                #     return memo[key]

                if key == (L1, L2):
                    continue

                k = i + j
                
                take_s1 = False
                if i < L1 and s1[i] == s3[k]:
                    take_s1 = memo.get((i + 1, j), False)

                take_s2 = False
                if j < L2 and s2[j] == s3[k]:
                    take_s2 = memo.get((i, j + 1), False)

                memo[key] = take_s1 or take_s2
        
        
        return memo.get((0, 0), False)
