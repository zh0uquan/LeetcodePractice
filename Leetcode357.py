import math

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        n = n if n <= 10 else 10
        f = math.factorial
        def factor(n, r):
            return f(n) / f(n-r)
        return factor(10, n) + sum(i * factor(9, i-1) for i in xrange(n))
