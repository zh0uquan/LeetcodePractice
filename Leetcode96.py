class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # https://www.youtube.com/watch?v=JrTKVvYhT_k
        # def helper(n):
        #     if n == 0 or n == 1:
        #         return 1
        #     return sum(helper(i-1) * helper(n-i) for i in range(1, n+1))
        # return helper(n)
        return 1 if n == 0 or n == 1 else \
                                    sum(self.numTrees(i-1) * self.numTrees(n-i)
                                        for i in range(1, n+1))


if __name__ == '__main__':
    print(Solution().numTrees(4))