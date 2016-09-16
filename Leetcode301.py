class Solution(object):
    """
    The most amazing code in the book!
    Enuermate all the possible answer.
    """
    def removeInvalidParentheses(self, s):
        def isvalid(s):
            s = filter('()'.count, s)
            while '()' in s:
                s = s.replace('()', '')
            return not s
        level = {s}
        while True:
            valid = filter(isvalid, level)
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

print(Solution().removeInvalidParentheses("s()()))))))))))ss()"))
