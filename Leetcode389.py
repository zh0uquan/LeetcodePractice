import operator
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # i = 0
        # table = {}
        # while i < len(s):
        #     table[s[i]] = table.setdefault(s[i], 0) + 1
        #     table[t[i]] = table.setdefault(t[i], 0) - 1
        #     i += 1
        # table[t[i]] = table.setdefault(t[i], 0) - 1
        # for k, v in table.iteritems():
        #     if v != 0:
        #         return k
        # xor much more faster than lambda a, b: a ^ b
        return chr(reduce(operator.xor, map(ord, s+t)))



print(Solution().findTheDifference('1213', 'a2311'))
