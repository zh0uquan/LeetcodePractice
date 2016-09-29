class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda p: p[1])
        people.sort(key=lambda p: -p[0])
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
