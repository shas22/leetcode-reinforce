class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        maps, mapt = {},{}

        for i in range(len(s)):
            c1,c2 = s[i],t[i]

            if (c1 in maps and maps[c1] != c2) or (c2 in mapt and mapt[c2] != c1):
                return False

            maps[c1] = c2

            mapt[c2] = c1

        return True