from sortedcontainers import SortedList
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = i = 0

        sorted1 = SortedList()

        for x in nums:
            sorted1.add(x)

            while sorted1[-1] - sorted1[0] > 2:
                sorted1.remove(nums[i])
                i += 1

            ans += len(sorted1)

        return ans