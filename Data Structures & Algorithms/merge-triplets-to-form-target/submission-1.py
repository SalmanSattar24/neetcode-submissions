class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        stack = deque()
        res = [0, 0, 0]

        for a, b, c in triplets:

            t1, t2, t3 = target[0], target[1], target[2]

            if a <= t1 and b <= t2 and c <= t3:

                # stack.append([a, b, c])
                res[0] = max(res[0], a)
                res[1] = max(res[1], b)
                res[2] = max(res[2], c)
        


        # while stack:

        #     a, b, c = stack.popleft()

        #     res[0] = max(res[0], a)
        #     res[1] = max(res[1], b)
        #     res[2] = max(res[2], c)



        # print(stack)
        return res == target