class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {'(': ')', '[': ']', '{': '}'}
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            if ch in [')', '}', ']']:
                if not stack or match[stack.pop()] != ch:
                    return False
        return not stack
