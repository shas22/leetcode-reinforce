class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)
        for number in sorted_arr:
            if number == 0 and sorted_arr.count(0) < 2:
                continue
            
            if number * 2 in sorted_arr or number / 2 in sorted_arr:
                return True
        
        return False