import bisect


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # a bit hack
        # return any(target in row for row in matrix if target <= row[-1])

        # bisect
        i = bisect.bisect(matrix, [target])
        if i < len(matrix) and matrix[i][0] == target:
            return True
        row = matrix[i-1]
        j = bisect.bisect_left(row, target)
        return j < len(row) and row[j] == target

if __name__ == '__main__':
    pass
