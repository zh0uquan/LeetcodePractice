import re

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-zA-Z0-9]*)\]',
                       lambda pattern: int(pattern.group(1)) * pattern.group(2),
                       s)
        return s

if __name__ == '__main__':
    print(Solution().decodeString('3[c2[ab]]'))
