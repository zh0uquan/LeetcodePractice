class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area, left, right = 0, 0, len(height) - 1
        while left < right:
            hl, hr = height[left], height[right]
            area = max(area, min(hl, hr) * (right - left))
            if hl <= hr:
                left += 1
            else:
                right -= 1
        return area
