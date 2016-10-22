import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # tails = [0] * len(nums)
        # size = 0
        # for i in range(len(nums)):
        #     lo, hi = 0, size
        #     while lo < hi:
        #         mid = (lo + hi) / 2
        #         if tails[mid] > nums[i]:
        #             hi = mid
        #         else:
        #             lo = mid + 1
        #     # (1) if x is larger than all tails, append it, increase the size by 1
        #     # (2) if tails[i-1] < x <= tails[i], update tails[i]
        #     tails[lo] = nums[i]
        #     size = max(size, lo+1)  # start from 0
        #
        # return size

        # simplified answers
        tails = [0] * len(nums)
        size = 0
        for i in range(len(nums)):
            index = bisect.bisect_left(tails, nums[i], 0, size)
            tails[index] = nums[i]
            size = max(size, index+1)
        return size

        # even simplier
        tails = [float('inf')] * (len(nums) + 1)
        for n in nums:
            tails[bisect.bisect_left(tails, n)] = n
        return tails.index(float('inf'))


if __name__ == '__main__':
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
