class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        numlist = []
        minus = 0
        for i in s:
            if i == "-" and (not numlist):
                minus = 1
                numlist.append(0)
                continue
            if i == "+" and (not numlist):
                numlist.append(0)
                continue
            if i == " " and (not numlist):
                continue
            try:
               numlist.append(int(i))
            except ValueError:
                break
        if not numlist:
            return 0
        result = int("".join(map(str, numlist)))
        if minus == 1:
            result = result * -1
        if result < -2147483648:
            return -2147483648

        if result > 2147483647:
            return 2147483647

        return result