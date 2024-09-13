class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        count = [for i in range(len(nums)+1)]

        for i in range(len(nums)):
            frequency[nums[i]] = 1 + frequency.get(nums[i], 0)

        # index position to be frequency and the number at the position
        for num, freq in freq.items():
            count[freq].append(num)



        res = []
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res
            


