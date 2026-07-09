"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
                
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        sp, ep = 0, 0
        max_meet, count = 0, 0
        while sp != len(intervals):
            if starts[sp] < ends[ep]:
                count += 1
                sp += 1
                max_meet = max(count, max_meet)
            else:
                count -= 1
                ep += 1

        return max_meet

