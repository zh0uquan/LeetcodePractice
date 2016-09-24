class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        one = 0
        while n:
            print(n)
            n &= n - 1
            one += 1
        return one

print(Solution().reverseBits(11))
