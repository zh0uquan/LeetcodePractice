import operator
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # def toMinBits(string):
        #     return
        #
        # # words.sort(key=lambda s: len(s), reverse=True)
        # size = len(words)
        # res = 0
        # for i in range(size):
        #     for j in range(i+1, size):
        #         w1, w2 = words[i], words[j]
        #         tmp = len(w1) * len(w2)
        #         if tmp <= res:
        #             break
        #         if not (toMinBits(w1) & toMinBits(w2)):
        #             res = max(tmp, res)
        #             break
        #
        # return res
        d = {}
        for word in words:
            mask = reduce(operator.or_, (1 << (ord(ch)-97) for ch in set(word)))
            d[mask] = max(len(word), d.get(mask, 0))
        return max([d[x] * d[y] for x in d for y in d if x & y == 0] or [0])

print(Solution().maxProduct([]))
