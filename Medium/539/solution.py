class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()

    

        def hour_converter(t):
            h, m = map(int, t.split(":"))
            return 60 * h+m

    
        ans = (
            24*60 - hour_converter(timePoints[-1]) + 
            hour_converter(timePoints[0])
        )

        for i in range(len(timePoints)-1):
            curr = hour_converter(timePoints[i+1])
            prev = hour_converter(timePoints[i])
            diff = curr - prev

            ans = min(ans, diff)

        return ans
