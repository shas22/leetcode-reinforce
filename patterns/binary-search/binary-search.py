def binary_search(nums: list, target: int):
    low = 0
    high = len(nums) - 1

   

    while high >= low:
        mid = (low + (high-low)) // 2
        if target > nums[mid]: 
            low = mid + 1
        elif target < nums[mid]:
            high = mid - 1
        else:
            return mid



def test_binary_search():
    # Test case 1: Target is in the middle of the list
    assert binary_search([1, 2, 3, 4, 5], 3) == 2, "Test case 1 failed"
    
            # Test case 2: Target is at the beginning of the list
    assert binary_search([1, 2, 3, 4, 5], 1) == 0, "Test case 2 failed"
    
    # Test case 3: Target is at the end of the list
    assert binary_search([1, 2, 3, 4, 5], 5) == 4, "Test case 3 failed"
    
    # Test case 4: Target is not in the list
    assert binary_search([1, 2, 3, 4, 5], 6) == -1, "Test case 4 failed"
    
    # Test case 5: Empty list
    assert binary_search([], 3) == -1, "Test case 5 failed"
    
    # Test case 6: List with one element, target is present
    assert binary_search([3], 3) == 0, "Test case 6 failed"
    
    # Test case 7: List with one element, target is not present
    assert binary_search([3], 1) == -1, "Test case 7 failed"
    
    # Test case 8: List with duplicate elements, target is present
    assert binary_search([1, 2, 2, 2, 3], 2) == 2, "Test case 8 failed"
    
    print("All test cases pass")

test_binary_search()