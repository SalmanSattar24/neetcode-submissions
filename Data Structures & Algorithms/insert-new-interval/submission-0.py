class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):

            newStart = newInterval[0]
            newEnd = newInterval[1]
            curStart = intervals[i][0]
            curEnd = intervals[i][1]

            if newEnd < curStart:

                res.append([newStart, newEnd])
                return res + intervals[i:]
            
            elif curEnd < newStart:

                res.append(intervals[i])
            
            else:

                newInterval[0] = min(newInterval[0], curStart)
                newInterval[1] = max(newInterval[1], curEnd)
        
        res.append([newInterval[0], newInterval[1]])
        
        return res