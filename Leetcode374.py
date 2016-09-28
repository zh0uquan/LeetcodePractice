# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # def helper(mid, start, end):
        #     tmp = guess(mid)
        #     if tmp == 0:
        #         return mid
        #     elif tmp == 1:
        #         new = (mid + 1 + end) / 2
        #         return helper(new, mid, end)
        #     elif tmp == -1:
        #         new = (start + mid - 1) / 2
        #         return helper(new, start, mid)
        #
        # return helper((1+n)/2, 1, n)

        low, high = 1, n
        while low < high:
            mid = (low + high) / 2
            g = guess(mid)
            if g == 1:
                low = mid + 1
            elif g == -1:
                high = mid
            elif g == 0:
                return mid
        return low
