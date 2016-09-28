class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # low, high = 0, len(nums) - 1
        # while low < high:
        #     mid = (low + high) / 2
        #     if nums[mid] == target:
        #         low = high = mid
        #         break
        #     elif nums[mid] > target:
        #         high = mid
        #     elif nums[mid] < target:
        #         low = mid + 1
        #
        # mid = (low + high) / 2
        # if nums[mid] != target:
        #     return [-1, -1]
        #
        #
        # while low - 1 >= 0 and nums[low-1] == target:
        #     low -= 1
        #
        # while high + 1 < len(nums) and nums[high+1] == target:
        #     high += 1
        #
        # return [low, high]

        def binarySearchLeft(li, target):
            left, right = 0, len(li) - 1
            while left <= right:
                mid = (left + right) / 2
                if target > li[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left


        def binarySearchRight(li, target):
            left, right = 0, len(li) - 1
            while left <= right:
                mid = (left + right) / 2
                if target >= li[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

            left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
            return [left, right] if left <= right else [-1, -1]
