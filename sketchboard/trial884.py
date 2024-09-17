from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter = {}


        for word in s.split():
            counter[word] = 1 + counter.get(word, 0)

        for word in s.split():
            counter[word] = 1 + counter.get(word, 0)


        ans = []
        for key, value in counter.items():
            if value == 1:
                ans.append(key)
        
        return ans


sol = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"

ans = sol.uncommonFromSentences(s1, s2)
print(ans)