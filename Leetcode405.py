class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # return "{:0x}".format(num) if num >= 0 else "{:0x}".format((1 << 32) + num)
        # return hex(num)[2:] if num >= 0 else hex((1<<32)+num)[2:]

        d = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

        num = num if num >= 0 else (4294967296 + num)
        res = ''
        while num:
            mod, num = num % 16, num / 16
            res = str(mod) + res if mod < 10 else str(d[mod]) + res

        return res

print(Solution().toHex(-1))
