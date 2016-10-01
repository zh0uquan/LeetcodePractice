
# N(-1) = 0
# N(0) = 1
# N(1) = N(1-2) + N(1-1)
# N(2) = N(2-2) + N(2-1) b = a + b
# N(3) = N(3-2) + N(3-1) b = a + b
# N(4) = N(4-2) + N(4-1)


# Recursive
def memoize(f):
    memo = {}

    def helper(this, x):
        if x not in memo:
            memo[x] = f(this, x)
        return memo[x]
    return helper


class Solution(object):
    @memoize
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

for i in range(10):
    print(Solution().climbStairs(i))


# Iterative
class Solution(object):
    def climbStairs(self, n):
        a, b = 0, 1
        i = 0
        while i < n:
            a, b = b, a + b
            i += 1
        return b

for i in range(10):
    print(Solution().climbStairs(i))
