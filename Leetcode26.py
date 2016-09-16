class Solution(object):
    def removeDuplicates(self, nums):
        if nums == []: return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        return i + 1

print(Solution().removeDuplicates([1,2,2,3,3,4]))
