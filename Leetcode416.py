class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # if sum(nums) % 2 != 0:
        #     return False
        #
        # halfSum = sum(nums) / 2
        # if halfSum in nums:
        #     return True
        #
        # def helper(start, target):
        #     if target < 0:
        #         return
        #     if target == 0:
        #         return True
        #     for i in range(start, len(nums)):
        #         if helper(i+1, target - nums[i]):
        #             return True
        #     return False
        # return helper(0, halfSum)

        # slow dp

        if sum(nums) & 1 != 0:
            return False

        halfSum = sum(nums) / 2
        dpSet = set([0])
        for n in nums:
            for m in dpSet.copy():
                if m + n <= halfSum:
                    dpSet.add(m + n)

        return halfSum in dpSet


if __name__ == '__main__':
    print(Solution().canPartition([1,2,5]))
