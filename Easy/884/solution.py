class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter = {}


        for word in s1.split():
                counter[word] = 1 + counter.get(word, 0)

        for word in s2.split():
                counter[word] = 1 + counter.get(word, 0)


        ans = []
        for key, value in counter.items():
            if value == 1:
                ans.append(key)
        
        return ans