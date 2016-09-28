class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # brute force
        # return [bin(i).count('1') for i in range(num+1)]
        # d(0) 000
        # d(1) 001
        # d(2) 010
        # d(3) 011
        # d(4) 100
        # d(5) 101

        res = [0] * (num+1)
        for i in range(num+1):
            # add previous counted 1 and last bit
            res[i] = res[i >> 1] + (i & 1)
        return res

print(Solution().countBits(5))
