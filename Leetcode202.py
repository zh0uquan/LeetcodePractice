class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # unhappy numbers: 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4
        # lst = [str(n)]
        # while lst:
        #     new = str(sum((int(i) ** 2 for i in str(lst[-1]))))
        #     if int(new) == 1:
        #         return True
        #     if new in lst:
        #         return False
        #     lst.append(new)

        # while n != 42:
        #     prev, n = n, sum(d*d for d in map(int, str(n)))
        #     if prev == n:
        #         return True
        # return False

        happyset = set()
        while n > 1 and n not in happyset:
            happyset.add(n)
            n = sum(map(lambda x: int(x) ** 2, list(str(n))))
        return n == 1

if __name__ == '__main__':
    print(Solution().isHappy(7))
