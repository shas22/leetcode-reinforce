class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        

        for i in range(len(nums) - 1):
            current_num = nums[i]
            next_num = nums[i + 1]
            

            current_even = (current_num % 2 == 0)
            next_even = (next_num % 2 == 0)

            if current_even == next_even:
                return False

        return True