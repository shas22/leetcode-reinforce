# https://www.designgurus.io/course-play/grokking-data-structures-for-coding-interviews/doc/problem-3-row-with-maximum-oneseasy
class Solution:
    def findMaxOnesRow(self, mat):
        currentmax = 0
        count = 0

        for i in range(len(mat)):
            loopmax = 0
            loopcount = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    loopmax += 1
                

            currentmax = max(loopmax, currentmax)