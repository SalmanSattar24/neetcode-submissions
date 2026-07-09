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
        
        # intervals.sort(key=lambda x: x.start)
        
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()
        
        L = len(intervals) 
        sp = 0
        ep = 0
        max_meet = 0
        count = 0
        while sp != L and ep != L:
            if starts[sp] < ends[ep]:
                count += 1
                sp += 1
                max_meet = max(count, max_meet)
            else:
                count -= 1
                ep += 1

        return max_meet

