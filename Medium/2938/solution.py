class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0 
        res = 0 

        for i in range(len(s)-1, -1, -1):
            if s[i] == '1':
                res += count
            else:
                count += 1
        return res