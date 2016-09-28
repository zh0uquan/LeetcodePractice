class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 1111
        # 1010
        # 10001
        return (a | b) + ((a & b) << 1) - (a & b)


print(Solution().getSum(-211,1))
