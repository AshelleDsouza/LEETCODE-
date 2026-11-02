class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1

        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i

        res = []

        for i in range(n, 0, -1):
            idx = k // fact[i - 1]
            res.append(nums.pop(idx))
            k %= fact[i - 1]

        return "".join(res)