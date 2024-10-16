class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []
        if a > 0:
            heappush(h, [-a, 'a'])

        if b > 0:
            heappush(h, [-b, 'b'])
            
        if c > 0:
            heappush(h, [-c, 'c'])

        res = []

        while len(h) > 0:

            cur = heappop(h)

            if len(res) >= 2 and res[-1] == cur[1] and res[-2] == cur[1]:

                if len(h) == 0:
                    break

                nxt = heappop(h)

                res.append(nxt[1])

                if -nxt[0] > 1:
                    nxt[0] += 1
                    heappush(h, nxt)
                heappush(h, cur)

            else:
                res.append(cur[1])
                if -cur[0] > 1:
                    cur[0] += 1
                    heappush(h, cur)

        return ''.join(res)