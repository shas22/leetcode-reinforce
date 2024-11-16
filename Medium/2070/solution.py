class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()

        prices = [price for price, _ in items]

        mb = [items[0][1]] 
        for index in range(1, len(items)):
            mb.append(max(mb[-1], items[index][1]))

        answers = [0] * len(queries)

        for i, budget in enumerate(queries):
            index = bisect_right(prices, budget)

            if index:
                answers[i] = mb[index - 1]

        return answers