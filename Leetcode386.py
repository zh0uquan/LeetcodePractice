class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # return sorted(range(1, 1+n), key=str)

        def dfs(i):
            if i <= n:
                res.append(i)
                t = 10 * i
                if t <= n:
                    for j in range(10):
                        dfs(t + j)
        res = []
        for i in range(1, 10):
            dfs(i)
        return res



        # < 10 (1-9)
        # < 20 1 10+range(10) ... 2-9
        # < 30 1 10+range(10) 2 2(0-9) ... 3-9
        # ...
        # < 100 1 10+range(10) 2 ... 9 9(0-9)
        # < 110 1 10 100+range(10) 2 ... 9 9(0-9)
        # < 120 1 10 100+range(10) 11 11(0-9) ... 9 9(0-9)
        #
        # < 200 1 10 100+range(10) ... 2 20 200+range(10)



if __name__ == '__main__':
    print(Solution().lexicalOrder(49999))
