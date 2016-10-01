class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        res = [1] * size

        def helper(output, list, start, end, step=1):
            p = 1
            for i in range(start, end, step):
                output[i] *= p
                p *= list[i]
            return output

        # left
        res = helper(output=res, list=nums, start=0, end=size)
        # right
        res = helper(output=res, list=nums, start=size-1, end=-1, step=-1)

        return res

    # def productExceptSelf(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     product = 1
    #     counter = 1
    #     for num in nums:
    #         if num != 0:
    #             product *= num
    #         else:
    #             counter -= 1
    #
    #     if counter < 0:
    #         return [0] * len(nums)
    #     elif counter == 0:
    #         return [ product if num == 0 else 0 for num in nums]
    #     return [product/num for num in nums]


print(Solution().productExceptSelf([1, 2, 3, 4, 1]))
