class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        si = 0

        res = []

        for i in range(len(nums)):

            if i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                continue

            if si == i:
                res.append(str(nums[si]))
            else:
                res.append(str(nums[si]) + "->" + str(nums[i]))

            si = i + 1

        return res