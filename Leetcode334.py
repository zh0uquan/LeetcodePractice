class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if not nums:
        #     return False
        # first = mid = float('inf')
        # for i in nums:
        #     first = i if i < first else first
        #     mid = i if i < mid and i > first else mid
        #     if i > mid:
        #         return True
        # return False
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

if __name__ == '__main__':
    #print(Solution().increasingTriplet([9,8,7,6,12,11,10,9,7]))
    print(Solution().increasingTriplet([1,0,10,0,0,0,0]))
    print(Solution().increasingTriplet([5,1,5,5,2,5,4]))
