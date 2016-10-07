class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # res = []
        # def helper(index, plist, target):
        #     if target == 0:
        #         if len(plist) == k:
        #             res.append(plist)
        #         return
        #     for i in range(index, 10):
        #         if i not in plist and i <= target:
        #             helper(i, plist + [i], target-i)
        #
        # helper(index=1, plist=[], target=n)
        # return res
        return [lst for lst in itertools.combinations(range(1, 10), k) if sum(lst) == k]


print(Solution().combinationSum3(3, 7))
