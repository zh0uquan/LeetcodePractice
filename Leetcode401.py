class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # slow
        # def timeFormat(hour=0, min=0):
        #     return "{:01}:{:02}".format(hour, min)
        #
        # return [timeFormat(hour, min) for hour in range(12) for min in range(60) if (bin(hour) + bin(min)).count(1) == num]

        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]

        def getTime(time, n, limit):
            res = []
            for comb in itertools.combinations(time, n):
                tmp = sum(comb)
                if tmp < limit:
                    res.append(tmp)
            return res

        res = []
        for i in range(num + 1):
            for h in getTime(hours, i, 12):
                for m in getTime(minutes, num-i, 60):
                    res.append("{:}:{:02}".format(h, m))
        return res
