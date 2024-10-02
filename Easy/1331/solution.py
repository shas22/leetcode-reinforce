class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Create a sorted version of the array
        sorting = sorted(set(arr))  # set to remove dupes

        #  dictionary to store ranks
        rank = {}
        for i, num in enumerate(sorting):
            if num not in rank:
                rank[num] = i + 1  # ranking starts from 1

        # create the result array
        res = []

        for num in arr:
            res.append(rank[num])
        
        return res