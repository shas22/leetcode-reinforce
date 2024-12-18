class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk = []
        
        for i, price in enumerate(prices):
            while stk and prices[stk[-1]] >= price:
                prices[stk.pop()] -= price

            stk.append(i)

        return prices