class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = set()

        for i in range(len(nums)):
            if nums[i] in count:
                count.remove(nums[i])
            else:
                count.add(nums[i])

        return count.pop()