class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if(n == 0):
            return []

        queue = [["(", n-1, n]]

        while(True):
            remain = queue.pop()
            l = remain[1]
            r = remain[2]

            if(r > 0):
                if(l < r):
                    queue = [[remain[0] + ")", l, r-1]] + queue
                if(l > 0):
                    queue = [[remain[0] + "(", l-1, r]] + queue
            else:
                queue.append(remain)

                return [s[0] for s in queue]