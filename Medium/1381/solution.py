class CustomStack:

    def __init__(self, maxSize: int):
        self.current = 0
        self.addition = [0] * maxSize
        self.stk = [0]* maxSize


    def push(self, x: int) -> None:
        if self.current < len(self.stk):
            self.stk[self.current] = x
            self.current += 1

    def pop(self) -> int:
        if self.current <= 0:
            return -1
        self.current -= 1
        result = self.stk[self.current] + self.addition[self.current]

        if self.current > 0:
            self.addition[self.current - 1] += self.addition[self.current]
        
        self.addition[self.current] = 0
        return result

    def increment(self, k: int, val: int) -> None:
        ceiling = min(k, self.current)
        if ceiling > 0:
            self.addition[ceiling - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)