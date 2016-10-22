import re


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        it = iter(re.findall(r'(?i)[aeiuo]', s[::-1]))
        return re.sub(r'(?i)[aeiuo]', lambda match: next(it), s)

if __name__ == '__main__':
    print(Solution().reverseVowels('leetcode'))
