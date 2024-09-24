class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # sort by longest length of string for both array? 
        # hashset maybe
        # could try to compare backwards first 

        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        prefix = set()

        for number in arr1:
            while number and number not in prefix:
                prefix.add(number)
                number = number // 10

        res = 0
        for n in arr2:
            while n and n not in prefix:
                n = n // 10

            if n:
                res = max(res, len(str(n)))
        return res

            