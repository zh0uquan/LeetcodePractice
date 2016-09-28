class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid
            if nums[mid] < target:
                low = mid + 1
        if target > nums[low]:
            return low + 1
        return low

print(Solution().searchInsert([1], 0))
