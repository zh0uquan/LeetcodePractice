class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        low, high = 1, num
        while low < high:
            mid = (low + high) / 2
            square = mid * mid
            if square == num:
                return True
            if square < num:
                low = mid + 1
            if square > num:
                high = mid
        return False

print(Solution().isPerfectSquare(17))
