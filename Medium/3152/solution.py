class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)

        disjoint = list(range(n))
        
        for i in range(1, n):
            if nums[i] % 2 != nums[i - 1] % 2:

                disjoint[i] = disjoint[i - 1]

        return [disjoint[to_index] <= from_index for from_index, to_index in queries]