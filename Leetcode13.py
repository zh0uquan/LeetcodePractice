class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ROMAN_DICT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res, num = 0, 0
        for ch in s[::-1]:
            tmp = ROMAN_DICT[ch.upper()]
            res += tmp if tmp >= num else -tmp
            num = tmp

        return res


        # return reduce(lambda x, y: x + y if x < y else y - x, [ROMAN_DICT[ch.upper()] for ch in s[::-1]])

print(Solution().romanToInt('DCXXI'))

print('DCXXI'[::-1])
