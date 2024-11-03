class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
            

        if not s or s == goal:
            return True
            

        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            

            if rotated == goal:
                return True
                
        return False