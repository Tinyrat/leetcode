import copy
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        rotMat = copy.deepcopy(matrix)
        for i in range(length):
            for j in range(length):
                matrix[j][length - i - 1] = rotMat[i][j]
