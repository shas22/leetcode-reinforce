# find left and right points and mid points and compare against L and R and iterate through them. 

def binarySearch(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l+r) // 2

        if target > arr[mid]:
            l = mid + 1
        elif target < arr[mid]
            r = mid - 1
        else:
            return mid
    return -1