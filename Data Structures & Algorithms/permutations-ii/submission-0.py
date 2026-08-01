class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        L = len(nums)
        # 'perm' keeps track of the current permutation we are building.
        # 'visited' is a set used to automatically filter out duplicate permutations.
        # ('result' is initialized but not actually used in this approach).
        result, perm, visited = [], [], set()
        
        # 'used' tracks which INDICES from the 'nums' array are currently in 'perm'.
        # We track indices instead of values because 'nums' 
        # can contain duplicate numbers.
        used = [False] * L

        def backtrack():

            # Base Case: If our current permutation is the same length as 'nums',
            # it means we have successfully built a full permutation.
            if len(perm) == L:
                # Convert the list to a tuple (since lists can't 
                # be added to sets in Python)
                # and add it to our 'visited' set. 
                # The set automatically ignores duplicates!
                visited.add(tuple(perm.copy()))
                return 
            
            # Iterate through every index in the 'nums' array
            for i in range(L):
                
                # If we haven't already included the number at this specific index...
                if not used[i]:
                    
                    # --- TAKE BRANCH ---
                    # 1. Add the number to our current permutation
                    perm.append(nums[i])
                    # 2. Mark this exact index as 'True' so 
                    # we don't reuse it down the tree
                    used[i] = True
                    
                    # Recursively build the rest of the permutation
                    backtrack()

                    # --- BACKTRACK (UNDO) ---
                    # Remove the number we just added so the next loop iteration 
                    # starts with a clean slate to try a different number.
                    perm.pop()
                    used[i] = False
        
        # Start the recursive backtracking process
        backtrack()
        
        # Our 'visited' set contains unique tuples like: 
        # {(1, 1, 2), (1, 2, 1), (2, 1, 1)}
        # We need to convert them back into lists to match the required return type.
        return [list(s) for s in visited]