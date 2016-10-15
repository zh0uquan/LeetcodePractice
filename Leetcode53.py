class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # before optimization
        # Fn = [0] * len(nums)
        # FnMax = float('-inf')
        #
        # for i in range(len(nums)):
        #     for n in range(i+1):
        #         Fn[n] = Fn[n] + nums[i]
        #         FnMax = max(FnMax, Fn[n])
        #
        # return FnMax

        # after optimization
        last, res = 0, float('-inf')

        for i in nums:
            last = max(last+i, i)
            res = max(last, res)

        return res

if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
