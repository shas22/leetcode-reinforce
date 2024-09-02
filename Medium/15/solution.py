class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #3 pointers?
        # if the result of 3 is further in negative (meaning away from 0 on left) move 
        
        result = []
        nums.sort() # (nlogn)

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and nums[i-1] == a:
                continue 
            

            l, r = i+1, len(nums) - 1

            while l < r:
                if a + nums[l] + nums[r] > 0:
                    r -= 1
                elif a + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result

