class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        maxProduct = minProduct = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > 0:
                maxProduct = max(maxProduct * nums[i], nums[i])
                minProduct = min(minProduct * nums[i], nums[i])
            else:
                lastMax = maxProduct
                maxProduct = max(minProduct * nums[i], nums[i])
                minProduct = min(lastMax * nums[i], nums[i])

            res = max(res, maxProduct)
        return res


print(Solution().maxProduct([-4, -2, -1, -6]))
