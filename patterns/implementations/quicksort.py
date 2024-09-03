def quicksort(nums: list, start: int, end: int):
    #base case
    if end - start + 1 <= 1:
        return nums

    pivot = nums[end]
    left = s 


    for i in range(start, end):
        if nums[i] < pivot:
            tmp = nums[left]
            nums[left] = arr[i]
            nums[i] = tmp
            left += 1

    nums[end] = nums[left]
    nums[left] = pivot
    
    
    quickSort(nums, start, left - 1)


    quickSort(nums, left + 1, end)

    return nums


#implmentation example using array of numbers