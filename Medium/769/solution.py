class Solution(object):
    def maxChunksToSorted(self, arr):
        result, imax = 0, 0

        for i, j in enumerate(arr):
            imax = max(imax, j)

            if imax == i:
                result += 1

        return result