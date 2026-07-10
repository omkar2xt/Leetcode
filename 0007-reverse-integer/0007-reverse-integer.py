class Solution(object):
    def reverse(self, x):
        ans = 0

        while x != 0:
            digit = int(x % 10) if x > 0 else -int((-x) % 10)
            x = int(x / 10)

            if ans > 214748364 or (ans == 214748364 and digit > 7):
                return 0

            if ans < -214748364 or (ans == -214748364 and digit < -8):
                return 0

            ans = ans * 10 + digit

        return ans