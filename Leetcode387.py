from collections import Counter, OrderedDict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # slow
        # class MyDict(Counter, OrderedDict):
        #     pass
        # for ch, val in MyDict(s).items():
        #     if val == 1:
        #         return s.find(ch)
        # else:
        #     return -1

        # average
        d = []
        for i in xrange(len(s)):
            ch = s[i]
            if ch not in d:
                if s.count(ch) == 1:
                    return i
                d.append(ch)

        return -1

print(Solution().firstUniqChar("sdadasdsadav"))
