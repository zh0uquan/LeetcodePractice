class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self.nums = nums


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = self.nums[:]
        for _, n in enumerate(res):
            i = random.randint(0, _)
            res[_], res[i] = res[i], res[_]
        return res
