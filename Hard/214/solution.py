class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # characters after the pivot point in reverse should be monitored 
        # count from the back and read frontward aft privot??
        # can also just reverse the whole thing and read from there
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s
        