
# C(n,k)=C(n-1,k-1)+C(n-1,k)

from itertools import combinations

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # STD LIB
        # return [l for l in itertools.combinations((i for i in range(1, n+1)), k)]
        return list(combinations(range(1, n+1), k))

        # Recursive
        res = []
        def helper(nums, k, index, path):
            if k == 0:
                res.append(path)
            return
            for i in xrange(index, len(nums)):
                helper(nums, k-1, i+1, path+[nums[i]])

        helper(xrange(1, n+1), k, 0, [])
        return res
