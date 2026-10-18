class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute combinations
        comb = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            comb[i][0] = comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] +
                              comb[i - 1][j]) % MOD

        def count_ways(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            left_ways = count_ways(left)
            right_ways = count_ways(right)

            # Interleave left and right subtree elements
            return (comb[len(left) + len(right)][len(left)] *
                    left_ways % MOD * right_ways) % MOD

        # Subtract 1 to exclude the original ordering
        return (count_ways(nums) - 1) % MOD