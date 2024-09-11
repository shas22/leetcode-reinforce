import math

def twocrystalball(breaks: list) -> int:
    jumpPointer = int(math.sqrt(len(breaks)))

    i = jumpPointer

    while i < len(breaks):
        if breaks[i] == True:
            break
        i += jumpPointer
    
    i -= jumpPointer

    for j in range(i, min(i + jumpPointer, len(breaks))):
        if breaks[j]:
            return j
    return -1


def test_twocrystalball():
    # Test Case 1: True is in the middle
    assert twocrystalball([False, False, False, True, True]) == 3, "Test case 1 failed"

    # Test Case 2: True is at the end
    assert twocrystalball([False, False, False, False, True]) == 4, "Test case 2 failed"

    # Test Case 3: True is at the beginning
    assert twocrystalball([True, True, True, True]) == 0, "Test case 3 failed"

    # Test Case 4: No True value
    assert twocrystalball([False, False, False, False, False]) == -1, "Test case 4 failed"

    # Test Case 5: True is exactly at the square root jump point
    assert twocrystalball([False, False, False, True]) == 3, "Test case 5 failed"

    # Test Case 6: Large list with True at the very end
    assert twocrystalball([False] * 999 + [True]) == 999, "Test case 6 failed"

    print("All test cases pass")

test_twocrystalball()
