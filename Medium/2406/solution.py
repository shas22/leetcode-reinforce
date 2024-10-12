class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        

        endPointer = 0
        group = 0

        for front in start:
            if front > end[endPointer]:
                endPointer += 1
            else:
                group += 1
        
        return group