class Solution:
    def minOperations(self, nums):
        n = len(nums)

        def costA(a):
            k = a[0]
            for i in range(n):
                if a[i] != (i + k) % n:
                    return -1
            return 0 if k == 0 else min(n - k, k + 2)

        best = float('inf')

        c = costA(nums)
        if c != -1:
            best = min(best, c)

        rev = nums[::-1]
        c = costA(rev)
        if c != -1:
            best = min(best, 1 + c)
            best = min(best, nums.index(n - 1) + 1)

        return -1 if best == float('inf') else best