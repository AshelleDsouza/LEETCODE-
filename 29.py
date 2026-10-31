class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)

        q = 0
        for shift in range(31, -1, -1):
            if (a >> shift) >= b:   # same as (b << shift) <= a
                a -= b << shift
                q += 1 << shift

        return -q if negative else q