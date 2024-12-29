class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0

        for i, j in sorted(boxTypes, key=lambda x: -x[1]):
            res += j * min(truckSize, i)

            truckSize -= i

            if 0 >= truckSize:
                break

        return res