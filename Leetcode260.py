class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # -xor = ~(xor - 1) the complemation of the last bit
        # xor & -xor equals last 1 bit
        # still bit of confused
        xor = reduce(operator.xor, nums)
        ans = reduce(operator.xor, (x for x in nums if x & xor & -xor))
        return [ans, ans ^ xor]
