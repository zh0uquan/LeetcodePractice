# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#
def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(lst, path, length, res):
            if len(path) == length:
                res.append(path)
                return
            for i in lst:
                if i not in path:
                    helper(lst, [i] + path, length, res)
        res = []
        helper(nums, [], len(nums), res)
        return res

permute([1,2,3])
