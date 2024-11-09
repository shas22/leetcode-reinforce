class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        previous = float('-inf')
        
        erased = 0

        for interval in sorted(intervals, key= lambda x: x[1]):
            start = interval[0]

            if start >= previous:
                previous = interval[1]
            else:
                erased += 1

        return erased