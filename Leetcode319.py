class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # O(n * n) 9999
        # bulbs = [0] * n
        # for r in range(1, n + 1):
        #     for i in range(n):
        #         if (i + 1) % r == 0:
        #             bulbs[i] += 1
        # return sum(i & 1 for i in bulbs)

        # O(n * n) 999999
        # bulbs = [0] * n
        #
        # for r in range(1, n+1):
        #     i = 1
        #     while i * r <= n:
        #         bulbs[i * r - 1] += 1
        #         i += 1
        #
        # return sum(i & 1 for i in bulbs)
        ####
        # A bulb ends up on iff it is switched an odd number of times.
        # Call them bulb 1 to bulb n. Bulb i is switched in round d if and only if d divides i.
        # So bulb i ends up on if and only if it has an odd number of divisors.
        # Divisors come in pairs, like i=12 has divisors 1 and 12, 2 and 6, and 3 and 4.
        # Except when i is a square, like 36 has divisors 1 and 36, 2 and 18, 3 and 12, 4 and 9, and double divisor 6. So bulb i ends up on if and only if i is a square.
        # So just count the square numbers.
        ###
        bulbs = collections.defaultdict(int)

        for r in

        for r in range(1, n+1):
            i = 1
            while i * r <= n:
                bulbs[i * r - 1] += 1
                i += 1

        return sum(i & 1 for i in bulbs.values())

        # return math.sqrt(n)

print(Solution().bulbSwitch(999999))
