class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == "":
            return 0

        i, sign, ret = 0, 1, 0
        MaxInt = (1 << 31) - 1

        # get
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            sign = -1

        for i in range(i, len(str)):
            if str[i] < '0' or str[i] > '9':
                break
            ret = ret * 10 + int(str[i])

        ret *= sign
        if ret >= MaxInt:
            return MaxInt
        if ret < (-1) * MaxInt:
            return (-1) * MaxInt - 1

        return ret



print(Solution().myAtoi("1"))
