class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = n < 0
        if neg:
            n = -n

        result = 1.0
        base = x
        while n:
            if n & 1:
                result *= base
            base *= base
            n >>= 1

        return 1 / result if neg else result