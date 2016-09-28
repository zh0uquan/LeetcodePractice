class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # N=(a[0] * 1 + a[1] * 10 + ...a[n] * 10 ^n),and a[0]...a[n] are all between [0,9]
        # we set M = a[0] + a[1] + ..a[n]
        # and another truth is that:
        # 1 % 9 = 1
        # 10 % 9 = 1
        # 100 % 9 = 1
        # so N % 9 = a[0] + a[1] + ..a[n]
        return 1 + (num - 1) % 9
