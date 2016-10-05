class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = 0
        for ch in s:
            index = t.find(ch, index) + 1
            if not index:
                return False
        return True
