class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        length = len(arr)

        left, right = 0, length - 1
        
        while left + 1 < length and arr[left] <= arr[left + 1]:
            left += 1
            
        while right - 1 >= 0 and arr[right - 1] <= arr[right]:
            right -= 1
            
        if left >= right:
            return 0
            
        result = min(length - left - 1, right)
        
        for start in range(left + 1):
            end = bisect_left(arr, arr[start], lo=right)

            result = min(result, end - start - 1)
            
        return result