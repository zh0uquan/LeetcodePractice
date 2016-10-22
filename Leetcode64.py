class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # m, n = len(grid), len(grid[0])
        # matrixS = [[0 for i in range(n)] for i in range(m)]
        #
        # # boundary
        # matrixS[0][0] = grid[0][0]
        # for i in range(1, m):
        #     matrixS[i][0] = matrixS[i-1][0] + grid[i][0]
        # for j in range(1, n):
        #     matrixS[0][j] = matrixS[0][j-1] + grid[0][j]
        #
        # for i in range(1, m):
        #     for j in range(1, n):
        #         matrixS[i][j] = min(matrixS[i-1][j], matrixS[i][j-1]) + grid[i][j]
        # return matrixS[m-1][n-1]

        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]




if __name__ == '__main__':
    pass
