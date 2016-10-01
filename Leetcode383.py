class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # return not collections.Counter(ransomNote) - collections.Counter(magazine)
        return all(magazine.count(c) <= ransomNote.count(c) for c in set(ransomNote))
