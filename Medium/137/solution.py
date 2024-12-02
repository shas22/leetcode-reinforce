class Solution(object):
    def singleNumber(self, nums):

        new_lst = list(set(nums)) 
        
        for num in new_lst:

            if nums.count(num) == 1:
                return num
        return None