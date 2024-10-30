class Solution:
   def minimumMountainRemovals(self, nums: List[int]) -> int:
       n = len(nums)

       increasing = [1] * n
       decreasing = [1] * n

       dp = [nums[0]]

       def binary_search(arr, target):
           l, r = 0, len(arr) - 1

           while l <= r:
               mid = (l + r) // 2
               if arr[mid] == target:
                   return mid
               elif arr[mid] < target:
                   l = mid + 1
               else:
                   r = mid - 1
           return l

       for i in range(1, n):
           if dp[-1] < nums[i]:
               dp.append(nums[i])
               increasing[i] = len(dp)
           else:
               idx = binary_search(dp, nums[i])
               dp[idx] = nums[i]
               increasing[i] = idx + 1

       dp = [nums[-1]]

       for i in range(n - 2, -1, -1):
           if dp[-1] < nums[i]:
               dp.append(nums[i])
               decreasing[i] = len(dp)
           else:
               idx = binary_search(dp, nums[i])
               dp[idx] = nums[i]
               decreasing[i] = idx + 1

       result = n + 1
       
       for i in range(1, n - 1):
           if increasing[i] != 1 and decreasing[i] != 1:
               count = n - (increasing[i] + decreasing[i] - 1)
               result = min(count, result)

       return result if result != n + 1 else 0