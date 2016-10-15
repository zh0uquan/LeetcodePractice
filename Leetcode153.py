class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        pivot = nums[-1]
        low, high = 0, len(nums)

        while low < high:
            mid = (low + high) / 2
            if nums[mid] > pivot:
                low = mid + 1
            else:
                high = mid

        return nums[high]

if __name__ == '__main__':
    print(Solution().findMin([7,8,9, 0, 1, 2, 5]))
