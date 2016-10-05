class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        row = [0] * len(n)

        for i, j in zip(range(len(n)), range(len(n))):
            count = n
            matrix = [row] * len(n)
            while i < len(n):

                while j < len(n):
                    if matrix[i][j] == 0:
                        matrix[i][j] = 'Q'
                    elif matrix[i][j] == '.':
                        break
                    j += 1
                i += 1
