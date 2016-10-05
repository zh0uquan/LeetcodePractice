import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = collections.Counter(s).values()
        return sum(ch & ~1 for ch in cnt) + any(ch & 1 for ch in cnt)

print(Solution().longestPalindrome("abccccddjknkjhkbjhvhcccc"))
