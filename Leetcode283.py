import operator
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)-1):
        #     if nums[i] == 0:
        #         j = i + 1
        #         while j < len(nums) - 1 and nums[j] == 0:
        #             j += 1
        #         if j > len(nums) - 1:
        #             break
        #         nums[i], nums[j] = nums[j], nums[i]
        #
        # print(nums)

        # i = j = 0
        # while j < len(nums):
        #     if nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        #     j += 1

        # i = j = 0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         i += 1
        #         continue
        #     else:
        #         nums[i], nums[j] = nums[j], nums[i]
        #
        #     j += 1
        #
        # print(nums)
        nums.sort(key=operator.not_)


Solution().moveZeroes([0, 1, 0, 3, 12])
