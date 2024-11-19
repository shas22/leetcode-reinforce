class Solution:
   def maximumSubarraySum(self, nums: List[int], k: int) -> int:
       frequency = Counter(nums[:k])

       total_sum = sum(nums[:k])

       maximum = total_sum if len(frequency) == k else 0

       for j in range(k, len(nums)):
           frequency[nums[j]] += 1

           frequency[nums[j - k]] -= 1

           if frequency[nums[j - k]] == 0:
               frequency.pop(nums[j - k])

           total_sum += nums[j] - nums[j - k]

           if len(frequency) == k:
               maximum = max(maximum, total_sum)
               
       return maximum