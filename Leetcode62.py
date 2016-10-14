class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # slow recursive
        # def robotPath(m, n):
        #     if m == 0 and n == 0:
        #         return 1
        #     if m > 0 and n > 0:
        #         return robotPath(m-1, n) + robotPath(m, n-1)
        #     if m > 0 and n == 0:
        #         return robotPath(m-1, n)
        #     if n > 0 and m == 0:
        #         return robotPath(m, n-1)
        #
        # return robotPath(m-1, n-1)

        # dp
        row = [0 for i in range(n)]
        matrix = [row[:] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[-1][-1]

if __name__ == '__main__':
    print(Solution().uniquePaths(22, 20))
