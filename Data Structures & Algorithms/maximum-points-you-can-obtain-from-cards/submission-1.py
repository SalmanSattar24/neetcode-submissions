class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        l, r = 0, k - 1
        n = len(cardPoints)
        win_size = n - k
        min_window = sum(cardPoints[: win_size])
        cur_win = min_window

        for i in range(win_size, n):

            cur_win = cur_win + cardPoints[i] - cardPoints[i - win_size]

            min_window = min(min_window, cur_win)

        return sum(cardPoints) - min_window