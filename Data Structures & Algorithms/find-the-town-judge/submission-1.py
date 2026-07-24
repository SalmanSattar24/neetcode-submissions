class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trust_adj_list = {i : [0, 0] for i in range(1, n + 1)}
        # [0, 0] first val indicated how many tursts him and second indicates how many does he trust

        for ai, bi in trust:

            trust_adj_list[bi][0] += 1
            trust_adj_list[ai][1] += 1
        
        for key, val in trust_adj_list.items():

            if val[0] == n - 1 and val[1] == 0:
                return key

        print(trust_adj_list)

        return -1
