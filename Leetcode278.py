# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version)

class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return findFirstBadVersion(1, n)

def findFirstBadVersion(start, end):
    if start == end:
        return start

    middle = int((start + end) / 2)

    if isBadVersion(middle):
        return findFirstBadVersion(start, middle)
    else:
        return findFirstBadVersion(middle+1, end)
