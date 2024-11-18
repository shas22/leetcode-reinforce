class Solution:
    def decrypt(self, code, k):
        if k == 0: 
            return [0] * len(code)

        if k < 0: 
            return self.decrypt(code[::-1], -k)[::-1]

        repeat = code * 2

        n = len(code)

        answer = []

        for i in range(n):
            answer.append(sum(repeat[i+1:i+k+1]))

        return answer