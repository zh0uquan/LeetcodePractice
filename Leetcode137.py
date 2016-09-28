class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            bits = 0
            for num in nums:
                if num & (1 << i):
                    bits += 1
            if bits % 3 != 0:
                # decide by the sign (int32)
                if i != 31:
                    res |= 1 << i
                else:
                    res -= (1 << i)
        return res

print(Solution().singleNumber([1,1,1,4,5,5,5,6,6,6]))
