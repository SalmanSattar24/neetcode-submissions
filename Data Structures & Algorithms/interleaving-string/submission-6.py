class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        L1, L2, L3 = len(s1), len(s2), len(s3)
        
        # Early termination: lengths must match
        if L1 + L2 != L3:
            return False
            
        # We only need a 2D state since k is always i + j
        memo = {(L1, L2): True}
        
        # Loop through L1 and L2 INCLUSIVELY down to 0
        for i in range(L1, -1, -1):
            for j in range(L2, -1, -1):
                
                # Skip the base case since it's already initialized
                if i == L1 and j == L2:
                    continue
                    
                # Derive k directly from i and j
                k = i + j
                
                take_s1 = False
                if i < L1 and s1[i] == s3[k]:
                    take_s1 = memo.get((i + 1, j), False)
                    
                take_s2 = False
                if j < L2 and s2[j] == s3[k]:
                    take_s2 = memo.get((i, j + 1), False)
                    
                memo[(i, j)] = take_s1 or take_s2
                
        # The answer is the state where we are at index 0 for both strings
        return memo.get((0, 0), False)