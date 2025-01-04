
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set() 
        left = set()
        right = Counter(s)

        for char in s: #char is a middle char
            right[char] -= 1
            for c in left:
                if right[c] > 0:
                    res.add((char, c))
            left.add(char)


        return len(res)