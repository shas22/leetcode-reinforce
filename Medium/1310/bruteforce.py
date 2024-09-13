class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []

        # loop through queries
                # gather the numbers in index of array and xor them
                #do i need another array other than ans

        for left, right in queries:
            xor_result = 0
            # Perform XOR operation on the range [left, right]
            for i in range(left, right + 1):
                xor_result ^= arr[i]
            ans.append(xor_result)

        return ans


#this solution ultimately takes too long for constraint 1 <= arr.length, queries.length <= 3 * 104 and we need a more optimized solution

