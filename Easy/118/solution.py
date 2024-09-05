class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # constraints suggest i only need to care about 1 len array

        total_rows = [[1]]

        for i in range(numRows-1):
            temp = [0] + total_rows[-1] + [0]
            row = []

            for j in range(len(total_rows[-1]) + 1):
                row.append(temp[j]+temp[j+1])
            total_rows.append(row)
        return total_rows
