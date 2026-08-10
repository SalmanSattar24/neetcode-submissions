class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        if s[0] == '1' or s[-1] == '1':
            return False
        
        n = len(s)
        queue = deque()
        visited  = set()
        queue.append(0)

        while queue:

            reach = queue.popleft()

            start = reach + minJump
            end = min(reach + maxJump, n - 1)

            for i in range(start, end + 1):

                if s[i] == '0':

                    if i == n - 1:
                        return True
                    
                    if i not in visited:
                        queue.append(i)
                        visited.add(i)
        
        return False