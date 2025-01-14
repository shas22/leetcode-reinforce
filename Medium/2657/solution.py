class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        c1 = Counter()
        c2 = Counter()

        for a, b in zip(A, B):
            c1[a] += 1
            c2[b] += 1
            t = 0

            for x, v in c1.items():
                minimum_value = min(v, c2[x])
                t += minimum_value

            res.append(t)

        return res