class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        size = len(candidates)

        def helper(candidates, index, plist, target):
            if target == 0:
                res.append(plist)
                return
            for i in range(index, size):
                num = candidates[i]
                if num <= target:
                    helper(candidates, i, plist + [num], target-num)

        helper(candidates, index=0, plist=[], target=target)
        return res

print(Solution().combinationSum([1], 1))
