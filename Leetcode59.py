class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # row = [0 for i in range(0, n)]
        # matrix = [row[:] for i in range(0, n)]
        #
        # side, i = 0, 1
        # while side < n:
        #     # top    [row = 0 + x, col = range(0 + x, n - x)]
        #     # right  [row = range(0+1+x, n-x), col = n -x]
        #     # bottom [row = n - x, col = range(n-1-x, 0, -1)]
        #     # left   [row = range(n-1-x, 0+1, -1), col = 0 + x]
        #
        #     for j in range(side, n-side):
        #         matrix[side][j] = i
        #         i += 1
        #     for j in range(side+1, n-side):
        #         matrix[j][(n-1)-side] = i
        #         i += 1
        #     for j in range(n-1-(side+1), side-1, -1):
        #         matrix[n-1-side][j] = i
        #         i += 1
        #     for j in range(n-1-(side + 1), side+1-1, -1):
        #         matrix[j][side] = i
        #         i += 1
        #     side += 1
        #
        # return matrix

        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [range(lo, hi)] + map(list, zip(*A[::-1]))
        return A

if __name__ == '__main__':
    print(Solution().generateMatrix(4))
