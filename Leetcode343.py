# max(2) = 1 * 1
# max(3) = 1 * 2

# max(4) = 3 * 4 1
# max(5) = 3 * 2 2
# max(6) = 3 * 3

# max(7) = 3 * 4 1
# max(8) = 3 * 3 * 2 ^1
# max(9) = 3 * 3 * 3
# max(10) = 3 * 3 * 4

# max(11) = 3 * 3 * 3 * 2
# max(12) = 3 * 3 * 3 * 3
# max(13) = 3 * 3 * 3 * 4

# max(14) = 3 * 3 * 3 * 3 * 2


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n - 1
        div, mod = n / 3, n % 3
        if mod == 0:
            return 3 ** (div)
        elif mod == 1:
            return 3 ** (div - 1) * 4
        elif mod == 2:
            return 3 ** (div) * 2

        # refactor
        # return n - 1 if n < 4 else 3 ** ((n - 2) / 3) * ((n - 2) % 3 + 2)  
