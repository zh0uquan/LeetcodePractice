class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # me win: 1, 2, 3, 5, 6, 7, 9,
        # me lose: 4, 8
        return not n % 4 == 0
