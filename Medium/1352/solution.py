class ProductOfNumbers:
    def __init__(self):
        self.saved = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.saved = [1]
            return
        self.saved.append(num * self.saved[-1])

    def getProduct(self, k: int) -> int:
        if len(self.saved) <= k:
            return 0

        curr = self.saved[-1]
        
        prev = self.saved[-k - 1]
        
        return curr // prev
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)