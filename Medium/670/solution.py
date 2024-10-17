class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))


        maxrn = "0"
        mxi = -1
        swap_i = -1 
        swap_j = -1

        for i in reversed(range(len(num))):
            if num[i] > maxrn:
                maxrn = num[i]
                mxi = i

            if num[i] < maxrn:
                swap_i, swap_j = i, mxi
        
        #the swap needs to happen in this manner if not you have to swap using a temp variable
        num[swap_i], num[swap_j] = num[swap_j], num[swap_i]


        return int("".join(num))
