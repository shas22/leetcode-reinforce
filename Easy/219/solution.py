class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in pos and i - pos[nums[i]] <= k:
                return True

            pos[nums[i]] = i
            
        return False