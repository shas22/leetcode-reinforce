def range_over_nums_sum(nums: list) -> int:
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]

def recursion_sum(nums: list) -> int:
    # recursion 
    if not nums:
        return 0

    return nums[0] + recursion_sum(nums[1:])

    
