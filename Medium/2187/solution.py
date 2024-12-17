class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        ans = []

        j = 24

        for i in range(25, -1, -1):
            j = min(i - 1, j)

            while 1:
                x = min(repeatLimit, count[i])
                count[i] -= x
                ans.append(ascii_lowercase[i] * x)

                if count[i] == 0:
                    break

                while j >= 0 and count[j] == 0:
                    j -= 1
                    
                if j < 0:
                    break

                count[j] -= 1

                ans.append(ascii_lowercase[j])
                
        return "".join(ans)