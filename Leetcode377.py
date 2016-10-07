class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, combs = sorted(nums), [1] + [0] * target
        for i in range(target+1):
            for num in nums:
                if num > i:
                    break
                elif num == i:
                    combs[i] += 1
                elif num < i:
                    combs[i] += combs[i-num]
        return combs[target]


print(Solution().combinationSum4([1,2,3,1,1,1,1], 1))
