class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        N = len(ratings)
        candies = [1] * N

        for i in range(1, N):

            if ratings[i] > ratings[i - 1]:
                candies[i] = 1 + candies[i - 1]

        for i in reversed(range(N - 1)):

            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        print(candies)
        return sum(candies)